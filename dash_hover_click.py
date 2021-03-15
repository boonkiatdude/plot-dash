import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import json
import base64


df = pd.read_csv('../Data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


app = dash.Dash()


fig = go.Scatter(
    x=df['color'],
    y=df['wheels'],
    dy=1,
    mode='markers',
    marker={'size':15}
)

layout = go.Layout(
    title='Test',
    hovermode='closest'
)


app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id='wheels-plot',
                          figure={'data':[fig], 'layout':layout},
                          style={'width':'30%', 'float':'left'})
            ]
        ),
        html.Div(
            html.Img(id='hover-data', src='children', height=300),
            style={'paddingTop':35}
        )
    ]
)

@app.callback(
    Output('hover-data', 'src'),
    [Input('wheels-plot', 'clickData')]
)
def callback_image(hoverData):
    if hoverData:
        wheel = hoverData['points'][0]['y']
        color = hoverData['points'][0]['x']
        path = '../Data/Images/'
        
        wheel_filt = (df['wheels'] == wheel)
        color_filt = (df['color'] == color)
        
        return encode_image(path + df[wheel_filt & color_filt]['image'].values[0])


if __name__ == '__main__':
    app.run_server()