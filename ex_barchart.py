import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('../Data/mocksurvey.csv', index_col=0)


data = [go.Bar(y=df.index, x=df[response], name=response, orientation='h') for response in df.columns]

layout = go.Layout(title='Mock Survey Results', barmode='stack')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)