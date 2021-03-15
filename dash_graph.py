import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('../Data/gapminderDataFiveYear.csv')
print(df.head())


app = dash.Dash()


year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year), 'value':year})


app.layout = html.Div(
    [
        dcc.Graph(id='graph'),
        dcc.Dropdown(
            id='year-picker',
            options=year_options,
            value=df['year'].min()
        ),
    ]
)

@app.callback(
    Output('graph', 'figure'),
    [Input('year-picker', 'value')]
)
def update_figure(year_selected):
    df_byyear = df[df['year'] == year_selected]
    
    traces = []
    for continent in df_byyear['continent'].unique():
        df_bycontinent = df_byyear[df_byyear['continent'] == continent]
        traces.append(
            go.Scatter(
                x=df_bycontinent['gdpPercap'],
                y=df_bycontinent['lifeExp'],
                mode='markers',
                marker={'size':12},
                text=df_bycontinent['country'],
                name=continent
            )
        )
    
    layout = go.Layout(
        title='My Plot',
        xaxis={'title':'GDP Per Capita', 'type':'log'},
        yaxis={'title':'Life Expectancy'},
        hovermode='closest'
    )
    
    return {'data':traces, 'layout':layout}


if __name__ == '__main__':
    app.run_server()   