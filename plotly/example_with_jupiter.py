import plotly.graph_objects as go
import numpy as np
import math

t = np.arange(-10,10,0.1)
y = np.zeros(len(t))

for i in range(0,len(y)):
    y[i] = math.sin(t[i])

fig = go.Figure(data=go.Scatter(x=t, y=y))
fig.show()