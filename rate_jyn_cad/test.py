from plotly import graph_objs
from plotly import offline



trace0 = graph_objs.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = graph_objs.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

layout = graph_objs.Layout(
    width=590,
    height=395,
)

fig = dict(data=data, layout=layout)

offline.plot(fig, filename='basic-line', auto_open=True, show_link=False)

