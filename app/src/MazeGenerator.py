from sqlite3 import Date
from Cell import Cell

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from Visualizer import Visualizer

class MazeGenerator:
    def __init__(self, columns: int, rows: int) -> None:
        # TODO don't allow negative or 0 as size
        # TODO check type
        self.y = rows
        self.x = columns

        self.maze = [[0 for x in range(self.x)] for y in range(self.y)]

        for r in range(self.y):
            for c in range(self.x):
                self.maze[r][c] = Cell(c,r)

    def getShape(self):
        # TODO make it better
        print("getShape self.y:", self.y, "y:", len(self.maze), "self.x:", self.x, "x:", len(self.maze[0]))

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
