
from app.src.Cell import Cell

import plotly.graph_objects as go
from plotly.subplots import make_subplots



class Visualizer:
    def __init__(self) -> None:
        self.shapes = []

    def cell(self, cells):
        for cell in cells:
            self.shapes += cell.getVizShape()

        # Create Subplots
        fig = make_subplots(rows=1, cols=1)

        fig.add_trace(go.Scatter(x=[], y=[]), row=1, col=1)

        # Add shapes
        fig.update_layout(
            shapes=self.shapes)
        fig.show()

    def genericShapes(self, shapes):
        # Create Subplots
        fig = make_subplots(rows=1, cols=1)

        fig.add_trace(go.Scatter(x=[], y=[]), row=1, col=1)

        # Add shapes
        fig.update_layout(
            shapes=shapes)
        fig.show()
