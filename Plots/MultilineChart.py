import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df['Date'] = pd.to_datetime(df['Date'])

trace1 = go.Scatter(x=df['Date'], y=df['Death'], mode='lines', name='Deaths')
trace2 = go.Scatter(x=df['Date'], y=df['Recovered'], mode='lines', name='Recovered')
trace3 = go.Scatter(x=df['Date'], y=df['Unrecovered'], mode='lines', name='Unrecovered')
data = [trace1, trace2, trace3]

layout = go.Layout(title="Corona Virus Death and Recovered Cases From 2020-01-22 to 2020-03-17", xaxis_title="Date", yaxis_title="Number of cases")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')