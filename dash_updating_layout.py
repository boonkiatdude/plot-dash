import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import requests


app = dash.Dash()


app.layout = html.Div(
    [
        html.Div(
            [
                html.Iframe(src='https://www.flightradar24.com',
                            height=500, width=1200)
            ]
        ),
        html.Div(
            [
                html.Pre(id='counter-text',
                         children='Active Flights Wordlwide'),
                dcc.Graph(id='live-update-graph', style={'width':'1200'},
                dcc.Interval(id='interval-component', interval=6000, n_intervals=0)
            ]
        )
    ]
)

counter_list = []

@app.callback(
    Output('counter-text', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_layout(n):
    url = "radarbox24.com"
    res = requests.get(url, header={'User-Agent':'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data['stats']['total']:
        counter += data['stats']['total'][element]
    counter_list.append(counter)
    return 'Active flights Worldwide: {}'.format(counter)
    
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)  
def update_graph(n):
    fig = go.Scatter(x=list(range(len(counter_list))), 
                     y=counter_list, 
                     mode='lines+markers')
    figure = go.Figure(data=[fig])])
    return figure
    

if __name__ == '__main__':
    app.run_server()