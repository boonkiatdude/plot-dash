import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo


df = pd.read_csv('../Data/2010YumaAZ.csv')

days = df.DAY.unique()
# print(df.head())

data = [go.Scatter(x=df['LST_TIME'], y=df[df['DAY']==day]['T_HR_AVG'], 
                    mode='lines', name=day) for day in days]

layout = go.Layout(title='Daily temp avgs')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)