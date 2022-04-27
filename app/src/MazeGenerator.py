from sqlite3 import Date
from Cell import Cell

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from Visualizer import Visualizer

class MazeGenerator:
    def __init__(self, rows, collums) -> None:
        self.rows = rows
        self.collums = collums

        self.maze = [[0 for x in range(self.collums)] for y in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.collums):
                self.maze[r][c] = Cell(r,c)

    def getVizShape(self) -> list:
        shape = []

        for row in self.maze:
            for cell in row:
                shape += cell.getVizShape()
        
        return shape



# m = MazeGenerator(32,32)
# #print(m.maze)

# viz = Visualizer()
# viz.genericShapes(m.getVizShape())
