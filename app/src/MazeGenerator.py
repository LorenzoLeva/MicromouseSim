import random
import sys
from app.src.Cell import Cell
from app.src.ErrorRaiser import ErrorRaiser
from app.src.Visualizer import Visualizer

class MazeGenerator:
    """Object that represents a maze.

        Note: The coordinates of the maze start at 0 and go up.
        
        Args:
            columns (int): amount of columns of the maze.
            rows (int): amount of rows of the maze.

        Attributes:
            x (int): amount of columns of the maze.
            y (int): amount of rows of the maze.
            visited (bool[][]): Matrix describing if that field was visited.
            maze (Cell[][]): Matrix containing all the Cells of the maze.
    """
    def __init__(self, columns: int, rows: int, seed = None) -> None:
        # Checks
        if seed:
            ErrorRaiser.raiseErrorOnlyInt(seed)
        ErrorRaiser.raiseNoZeroNegativeInt(rows, "rows")
        ErrorRaiser.raiseNoZeroNegativeInt(columns, "columns")

        # Configs
        if seed is None:
            self.seed = random.randrange(sys.maxsize)
        else:
            self.seed = seed

        random.seed(self.seed)
        sys.setrecursionlimit(10**6) # TODO move to main class
       
        self.y = rows
        self.x = columns
        self.visited = [[False for x in range(self.x)] for y in range(self.y)]
        self.maze = [[0 for x in range(self.x)] for y in range(self.y)]

        for r in range(self.y):
            for c in range(self.x):
                self.maze[r][c] = Cell(c,r)
    
    # Raise exceptions
    @staticmethod
    def raiseCellsAreNotNeighborIfApplicable(cellStart: Cell, cellEnd: Cell):
        """Checks if two cells are neighbor and if returns the vector between them. Otherwise it throws an exception.

        Args:
            cellStart (tuple | Cell): First cell to check
            cellEnd (tuple | Cell): Second cell to check

        Returns:
            tuple: cellResult is the vector decribing how to come the cellStart to the cellEnd
        """
        cellStart = Cell.raiseIsNotCellIfApplicable(cellStart)
        cellEnd = Cell.raiseIsNotCellIfApplicable(cellEnd)

        # Allign to cell type to be able to use minus
        cellStart = Cell(cellStart[0], cellStart[1])
        cellEnd = Cell(cellEnd[0], cellEnd[1])

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
        """Checks if coordinate is in the Maze. Otherwise it throws an error
        Args:
            x (int): x coordinate to check
            y (int): y coordinate to check
        
        """
        # TODO check that coordinates are int
        if not self.isCoordinateInMaze(x, y):
            raise IndexError(f'Cell isn\'t within the maze. X has to be between 0 and {self.x - 1}(included) and Y has to be between 0 and {self.y - 1}(included). Got X:{x}, Y:{y}')

    # General maze methods
    def isCoordinateInMaze(self, x: int, y: int) -> bool:
        """Checks if coordinate is in Maze.

        Returns:
            bool: True if the coordinate is in the maze, and False if it is not.
        """
        if type(x) is not int or type(y) is not int:
            raise TypeError(f'Only ints are allowed for x and y. Received for x: {type(x)} of {x} and for y: {type(y)} of {y}')
        return (x >= 0 and x < self.x and y >= 0 and y < self.y)

    def getShape(self):
        """Prints the shape of the maze.
        """
        # TODO make it better
        print("getShape self.y:", self.y, "y:", len(self.maze), "self.x:", self.x, "x:", len(self.maze[0]))

    def getMazeCellFromTuple(self, cellTuple) -> Cell:
        """Returns the cell of the maze with the same coordinates as the inputted cell | tuple
        
        Returns:
            Cell: the cell of the maze with the same coordinates as the inputted cell | tuple
        """
        cellTuple = Cell.raiseIsNotCellIfApplicable(cellTuple)

        return self.maze[cellTuple[1]][cellTuple[0]]

    def deleteWallsBetween(self, cellStart, cellEnd):
        """Deletes the walls between to cells that are neighbors.

        Args:
            cellStart (Cell | tuple): First cell to remove wall from
            cellEnd (Cell | tuple): Second cell to remove wall from
        """

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
        """Gets all the not visited neighbors from a cell

        Args:
            cell (Cell): Cell from which to search the neighbors from.

        Returns:
            list: Returns a list of coordinates of all the neighbors, of the inputted cell, that weren't visited.
        
        """
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
        """Gets a random neighbor from a cell.

        Args:
            cell (Cell): Cell from which to search a neighbor from.

        Returns:
            tuple: Coordinates of randomly chosen neighbor.
        """
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
        """Generates all the shape objects needed to visualize the maze with plotly.

        Returns:
            list: Returns a list containing all the shapes needed to visualize the maze.
        """
        shape = []

        for row in self.maze:
            for cell in row:
                shape += cell.getVizShape()
        
        return shape

    def visualize(self):
        """Visualizes the maze with plotly."""
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
