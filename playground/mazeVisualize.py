import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create Subplots
fig = make_subplots(rows=1, cols=1)

fig.add_trace(go.Scatter(x=[], y=[]), row=1, col=1)

# Add shapes
fig.update_layout(
    shapes=[
        dict(type="line", xref="x", yref="y",
            x0=0, y0=0, x1=1, y1=0, line_width=3, line_color="green"),
        dict(type="line", xref="x", yref="y",
            x0=1, y0=0, x1=1, y1=1, line_width=3, line_color="red"),
        dict(type="line", xref="x", yref="y",
            x0=1, y0=1, x1=0, y1=1, line_width=3, line_color="blue"),
        dict(type="line", xref="x", yref="y",
            x0=0, y0=1, x1=0, y1=0, line_width=3, line_color="orange"),
        ])
fig.show()