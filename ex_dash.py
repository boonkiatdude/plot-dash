import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
from datetime import *
import pandas as pd


nsdq = pd.read_csv('../Data/NASDAQcompanylist.csv', index_col='Symbol')

options = []
for ind in nsdq.index:
    option = {'label':nsdq.loc[ind, 'Name'], 'value':ind}
    options.append(option)


app = dash.Dash()


app.layout = html.Div(
    [
        html.Div(html.H1('Stock Ticker Dashboard')),
        html.Div(
            [
                html.H3('Enter a stock symbol:'),
                dcc.Dropdown(id='stock-picker', options=options, multi=True)
            ],
            style={'width':'30%', 'display':'inline-block', 'verticalAlign':'top'}
        ),
        html.Div(
            [
                html.H3('Select start and end dates:'),
                dcc.DatePickerRange(id='date-slider', 
                                    start_date=date(2017, 1, 1), end_date=date(2017, 12, 31))
            ],
            style={'display':'inline-block', 'marginLeft':30}
        ),
        html.Div(
            [
                html.Button(id='my-button', n_clicks=0, children='Submit',
                            style={'fontSize':28})
            ],
            style={'display':'inline-block', 'marginLeft':30}
        ),
        dcc.Graph(id='my-graph')
    ]
)

@app.callback(
    Output('my-graph', 'figure'),
    [Input('my-button', 'n_clicks')],
    [State('stock-picker', 'value'),
     State('date-slider', 'start_date'),
     State('date-slider', 'end_date')]
)
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    
    traces = []
    for ticker in stock_ticker:
        df = web.DataReader(ticker, 'yahoo', start, end)
        trace = go.Scatter(x=df.index, y=df['Close'], mode='lines+markers', name=ticker)
        traces.append(trace)
    
    layout = go.Layout(title='Stock Market Plot', 
                       xaxis={'title':'Date'}, yaxis={'title':'Prices'})
    
    figure = {'data':traces, 'layout':layout}
    
    return figure


if __name__ == '__main__':
    app.run_server()