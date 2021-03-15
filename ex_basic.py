import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('../Data/OldFaithful.csv')
print(df.head())


app = dash.Dash()


app.layout = html.Div(
    dcc.Graph(
        id='scatterplot',
        figure={
            'data':[
                go.Scatter(
                    x=df['X'], 
                    y=df['Y'], 
                    mode='markers',
                    marker={
                        'size':12,
                        'color':'rgb(64, 152, 104)'
                    }
                )
            ],
            'layout':go.Layout(
                title='Old Faithful Eruptions',
                xaxis={'title':'Duration'},
                yaxis={'title':'Interval'}
            )
        }
    )
)

if __name__ == '__main__':
    app.run_server()