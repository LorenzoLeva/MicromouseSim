import random
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
        self.visited = [[False for x in range(self.x)] for y in range(self.y)]
        self.maze = [[0 for x in range(self.x)] for y in range(self.y)]

        for r in range(self.y):
            for c in range(self.x):
                self.maze[r][c] = Cell(c,r)
    
    # Raise exceptions
    @staticmethod
    def raiseCellsAreNotNeighborIfApplicable(cellStart, cellEnd):
        """Checks if two cells are neighbor and if returns the vector between them.

        Returns:
            cellResult is the vector decribing how to come the cellStart to the cellEnd
        """
        cellResult = cellEnd.minus(cellStart)

        if not (
            (cellResult[0] is 0  and cellResult[1] is 1 ) or 
            (cellResult[0] is 0  and cellResult[1] is -1) or 
            (cellResult[0] is 1  and cellResult[1] is 0 ) or 
            (cellResult[0] is -1 and cellResult[1] is 0 )
        ):
            raise IndexError(f'Cells aren\'t neighbor. The coordinate difference is {cellResult}, but its only accepted [(0,1), (0,-1), (1, 0), (-1,0)].')

        return cellResult

    def raiseNotInMazeIfApplicable(self, x, y):
            if not self.isCoordinateInMaze(x, y):
                raise IndexError(f'Cell isn\'t within the maze. X has to be between 0 and {self.x - 1}(included) and Y has to be between 0 and {self.y - 1}(included). Got X:{x}, Y:{y}')

    # General maze methods
    def isCoordinateInMaze(self, x, y):
        return (x >= 0 and x < self.x and y >= 0 and y < self.y)

    def getShape(self):
        # TODO make it better
        print("getShape self.y:", self.y, "y:", len(self.maze), "self.x:", self.x, "x:", len(self.maze[0]))

    def getMazeCellFromTuple(self, cellTuple):
        cellTuple = Cell.raiseIsNotCellIfApplicable(cellTuple)

        return self.maze[cellTuple[1]][cellTuple[0]]

    def deleteWallsBetween(self, cellStart, cellEnd):
        cellStart = Cell.raiseIsNotCellIfApplicable(cellStart)
        cellEnd = Cell.raiseIsNotCellIfApplicable(cellEnd)

        cellStart = self.maze[cellStart[1]][cellStart[0]]
        cellEnd = self.maze[cellEnd[1]][cellEnd[0]]

        cellResult = self.raiseCellsAreNotNeighborIfApplicable(cellStart, cellEnd)
        
        if cellResult[0] is 1 and cellResult[1] is 0:
            cellStart.deleteWall("right")
            cellEnd.deleteWall("left")
        
        if cellResult[0] is -1 and cellResult[1] is 0:
            cellStart.deleteWall("left") # cellStart
            cellEnd.deleteWall("right") # cellEnd

        if cellResult[0] is 0 and cellResult[1] is 1:
            cellStart.deleteWall("top") # cellStart
            cellEnd.deleteWall("bottom") # cellEnd

        if cellResult[0] is 0 and cellResult[1] is -1:
            cellStart.deleteWall("bottom") # cellStart
            cellEnd.deleteWall("top") # cellEnd
 
    # Manage Neighbors
    def getNotVisitedNeighbors(self, cell) -> list:
        cell = Cell.raiseIsNotCellIfApplicable(cell)

        x = cell[0]
        y = cell[1]
        del cell
        
        self.raiseNotInMazeIfApplicable(x, y)

        choices = []

        # top
        if self.isCoordinateInMaze(x, y + 1):
            if not self.visited[y+1][x]:
                choices.append((x, y + 1))

        # right
        if self.isCoordinateInMaze(x + 1, y):
            if not self.visited[y][x+1]:
                choices.append((x + 1, y))

        # bottom
        if self.isCoordinateInMaze(x, y - 1):
            if not self.visited[y-1][x]:
                choices.append((x, y - 1))

        # left
        if self.isCoordinateInMaze(x-1, y):
            if not self.visited[y][x-1]:
                choices.append((x-1, y))

        return choices

    def choseRandomNeighbor(self, cell) -> tuple:
        if type(cell) is Cell:
            cell = (cell.x, cell.y)
        
        if type(cell) is not tuple:
            raise TypeError(f'Only Cell or tuple are allowed. Received for cell: {type (cell)} of {cell}')

        x = cell[0]
        y = cell[1]
        del cell
        
        if not self.isCoordinateInMaze(x, y):
            raise IndexError(f'Cell isn\'t within the maze. X has to be between 0 and {self.x - 1}(included) and Y has to be between 0 and {self.y - 1}(included). Got X:{x}, Y:{y}')

        choices = self.getNotVisitedNeighbors((x,y))
        
        if len(choices) > 0:
            return random.choice(choices)
        else:
            return None
   
    # Visualize Maze
    def getVizShape(self) -> list:
        shape = []

        for row in self.maze:
            for cell in row:
                shape += cell.getVizShape()
        
        return shape

    def visualize(self):
        viz = Visualizer()
        viz.genericShapes(self.getVizShape())


# c1 = Cell(5,5)
# c2 = Cell(7,7)

# print(MazeGenerator.raiseCellsAreNotNeighborIfApplicable(c1, c2))

# m = MazeGenerator(11,11)
# print(m.maze)

# m.deleteWallsBetween((5,5), (5,6))
# m.deleteWallsBetween((5,5), (5,4))

# print(m.maze[5][5].walls)

# viz = Visualizer()
# viz.genericShapes(m.getVizShape())
