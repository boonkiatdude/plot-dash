import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
from datetime import date
from datetime import datetime
import pandas_datareader.data as web
import pandas as pd


app = dash.Dash()


nsdq = pd.read_csv('../Data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace=True)

# Create list of dictionaries with label and value as its keys
options = []

for tic in nsdq.index:
    mydict = {}
    mydict['label'] = nsdq.loc[tic]['Name'] + ' ' + tic
    mydict['value'] = tic
    options.append(mydict)


fig = go.Scatter(x=[1, 2, 3], y=[3, 2, 1], mode='lines')
layout = go.Layout(title='Default Title', 
                   xaxis={'title':'Date'}, yaxis={'title':'Prices'})

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1('Stock Ticker Dashboard'),
                html.Div(
                    [
                        html.H3('Enter a stock symbol:',
                                style={'paddingRight':'30px'}),
                        dcc.Dropdown(id='my-stock-picker', options=options, 
                                     value='TSLA', multi=True)
                    ],
                    style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}
                ),
                html.Div(
                    [
                        html.H3('Select start and end dates:'),
                        dcc.DatePickerRange(id='date-range-picker',
                                            min_date_allowed=date(2017, 1, 1),
                                            max_date_allowed=datetime.today(),
                                            start_date=date(2017, 1, 1),
                                            end_date=datetime.today())
                    ],
                    style={'display':'inline-block'}
                ),
                html.Div(
                    [
                        html.Button(id='submit-button', n_clicks=0, children='Submit',
                                    style={'fontSize':24, 'marginLeft':'30px'})
                    ],
                    style={'display':'inline-block'}
                ),
                dcc.Graph(id='my-graph', figure={'data':[fig], 'layout':layout})
            ]
        )
    ]
)


@app.callback(
    Output('my-graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my-stock-picker', 'value'), 
     State('date-range-picker', 'start_date'),
     State('date-range-picker', 'end_date')]
)
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic, 'yahoo', start, end)
        traces.append(go.Scatter(x=df.index, y=df['Close'], name=tic))
    
    
    layout = go.Layout(title='Stock Market Plot',
                       xaxis={'title':'Date'}, yaxis={'title':'Prices'})

    figure = {'data':traces, 'layout':layout}
    return figure


if __name__ == '__main__':
    app.run_server()