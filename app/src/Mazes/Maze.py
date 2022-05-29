from math import floor

import random
import sys
import abc

from Cells.Cell import Cell
from Tools.ErrorRaiser import ErrorRaiser
from Tools.Visualizer import Visualizer

class Maze(metaclass=abc.ABCMeta):
    """Object that represents a maze.

        Note: The coordinates of the maze start at 0 and go up.
        
        Args:
            columns (int): amount of columns of the maze.
            rows (int): amount of rows of the maze.
            seed (int): seed for the random module.
            startCell: Cell from which the bot starts
            endCell1, endCell2 (Cell): corner Cells that contain the finish area of the maze. Can be the same if the finish area is a single cell.

        Attributes:
            x (int): amount of columns of the maze.
            y (int): amount of rows of the maze.
            visited (bool[][]): Matrix describing if that field was visited.
            maze (Cell[][]): Matrix containing all the Cells of the maze.
    """
    def __init__(self, columns: int = 16, rows: int = 16, seed = None, startCell = (0,0), endCell1 = None, endCell2 = None) -> None:
        # Random function config
        if seed is None:
            self.seed = random.randrange(sys.maxsize)
        else:
            ErrorRaiser.raiseErrorOnlyInt(seed, "maze.seed")
            self.seed = seed

        random.seed(self.seed)
        
        # Maze size
        ErrorRaiser.raiseNoZeroNegativeInt(rows, "rows")
        ErrorRaiser.raiseNoZeroNegativeInt(columns, "columns")
        self.y = rows
        self.x = columns

        # Start Cell
        self.startCell = Cell.raiseIsNotCellIfApplicable(startCell)

        # Finish Area
        if endCell1 is not None:
            self.endCell1 = Cell.raiseIsNotCellIfApplicable(endCell1)
        else:
            x = Maze.getMiddleCoordinate(self.x)
            y = Maze.getMiddleCoordinate(self.y)

            self.endCell1 = (x["min"], y["min"])
            self.endCell2 = (x["max"], y["max"])

        if endCell2 is not None:
            self.endCell2 = Cell.raiseIsNotCellIfApplicable(endCell2)


        # Configs
        sys.setrecursionlimit(10**6) # TODO move to main class
       
        self.visited = [[False for x in range(self.x)] for y in range(self.y)]
        self.maze = [[0 for x in range(self.x)] for y in range(self.y)]

        for r in range(self.y):
            for c in range(self.x):
                cellType = "normal"
                if c is self.startCell[0] and r is self.startCell[1]:
                    cellType = "start"
                
                if self.isCoordinateInEndArea(c, r):
                    self.visited[r][c] = True
                    cellType = "end"

                self.maze[r][c] = Cell(c,r, cellType)
        
        self.deleteWallsBetween(self.endCell1, self.endCell2)
        self.deleteRandomEndAreaBorderWall()
    
    @staticmethod
    def getMiddleCoordinate(x):
        ''' Returns a object with the min and max coordinate of the middle of a size.

            Returns:  
                dict: An dictionary containing the min and max coordinate the middle of a size.
                    
                Note:
                    When the size is odd the middle is one cell wide. (Exp.: 7 => {min: 3, max: 3})
                    When the size is even the middle is two cell wide. (Exp.: 8 => {min: 3, max: 4})
        '''
        ErrorRaiser.raiseNoNegativeInt(x)

        x = x / 2 # Even: 8/2 = 4   Odd: 7/2 = 3.5

        minX = x - 0.1 # Even: 4 - 0.1 = 3.9   Odd: 3.5 - 0.1 = 3.4
        maxX = x + 0.1 # Even: 4 + 0.1 = 4.1   Odd: 3.5 + 0.1 = 3.6

        minX = floor(minX) # Even: floor(3.9) = 3  Odd: floor(3.4) = 3
        maxX = floor(maxX) # Even: floor(4.1) = 4  Odd: floor(3.6) = 3

        return {"min": minX, "max": maxX}

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

    def raiseNotInMazeIfApplicable(self, x: int, y: int):
        """Checks if coordinate is in the Maze. Otherwise it throws an error
        
        Args:
            x (int): x coordinate to check
            y (int): y coordinate to check
        """
        # TODO check that coordinates are int
        if not self.isCoordinateInMaze(x, y):
            raise IndexError(f'Cell isn\'t within the maze. X has to be between 0 and {self.x - 1}(included) and Y has to be between 0 and {self.y - 1}(included). Got X:{x}, Y:{y}')

    @staticmethod
    def raiseNotMaze(maze, name=""):
        name = ErrorRaiser.getNameText(name)

        if not issubclass(type(maze), Maze):
            raise TypeError(f'Only Maze subclasses are allowed. Received{name}: {type(maze)} of {maze}')

        return maze

    # General maze methods
    def isCoordinateInMaze(self, x: int, y: int) -> bool:
        """Checks if coordinate is in Maze.

        Returns:
            bool: True if the coordinate is in the maze, and False if it is not.
        """
        if type(x) is not int or type(y) is not int:
            raise TypeError(f'Only ints are allowed for x and y. Received for x: {type(x)} of {x} and for y: {type(y)} of {y}')
        return (x >= 0 and x < self.x and y >= 0 and y < self.y)

    def isCoordinateInEndArea(self, x: int, y:int) -> bool:
        """Checks if coordinate is part of the finish area of the maze.

        Returns:
            bool: True if the coordinate is part of the finish area of the maze, and False if it is not.
        """
        ErrorRaiser.raiseErrorOnlyInt(x, "x")
        ErrorRaiser.raiseErrorOnlyInt(y, "y")

        return (
            (self.endCell1[0] <= x <= self.endCell2[0] or self.endCell2[0] <= x <= self.endCell1[0]) and 
            (self.endCell1[1] <= y <= self.endCell2[1] or self.endCell2[1] <= y <= self.endCell1[1]))

    def getRandomEndAreaBorderCell(self):
        '''Returns a random border cell coordinate of the end area.
    
        Returns:
            tuple: coordinate of a random border cell of the end area.
        '''

        choices = Maze.getBorderCellsOfArea(self.endCell1, self.endCell2)

        return random.choice(choices)

    def deleteRandomEndAreaBorderWall(self):
        '''Deletes a random wall of the border of the end area.'''

        cell = self.getRandomEndAreaBorderCell()
        cell = self.maze[cell[1]][cell[0]]
        cell2 = self.choseRandomNeighbor(cell)
        cell2 = self.maze[cell2[1]][cell2[0]]

        self.deleteWallsBetween(cell, cell2)

    def getStartPosition(self):
        '''Returns the coordinates of the start position of the maze.
        
        Returns:
            tuple: of the coordinates of the start position.
        '''
        return self.startCell

    def isEndPosition(self, position):
        '''Returns a boolean describing if the passed position is an end position.

        Args:
            position (tuple | Cell): Position from you want to know if it is an end position.  

        Return:
            bool: describing if the passed position is an end position.      
        '''

        position = Cell.raiseIsNotCellIfApplicable(position)
        position = self.maze[position[1]][position[0]]

        return position.isOfType("end")

    def getNextSteps(self, position):
        '''Returns all the possible next steps for a position.
        
        Args:
            position (tuple | Cell): Position from which the possible next position are requested.

        Returns:
            list: of string keys of the possible next step for the position passed.
        '''

        position = Cell.raiseIsNotCellIfApplicable(position)
        
        position = self.maze[position[1]][position[0]]

        return position.getAllWalls(False)

    @staticmethod
    def getBorderCellsOfArea(cornerCell1, cornerCell2) -> tuple:
        '''Returns a list of tuples with the coordinates of the cells at the border of an area.
        
        Args:
            cornerCell1: Cell at one of the corners of the area. The two corners have to be opposite to each other so to contain the area between them.
            cornerCell2: Cell at one of the corners of the area. The two corners have to be opposite to each other so to contain the area between them. 

        Returns:
            list: of the coordinates of the cells at the border of an area.
        '''
        cornerCell1 = Cell.raiseIsNotCellIfApplicable(cornerCell1)
        cornerCell2 = Cell.raiseIsNotCellIfApplicable(cornerCell2)

        minMaxEndArea = Maze.getMinMaxCoordinatesOfCells([cornerCell1, cornerCell2])

        borderCells= []

        for x in range(minMaxEndArea["minX"], minMaxEndArea["maxX"] + 1):
            borderCells.append((x, minMaxEndArea["minY"]))
            borderCells.append((x, minMaxEndArea["maxY"]))

        for y in range(minMaxEndArea["minY"]+1, minMaxEndArea["maxY"]):
            borderCells.append((minMaxEndArea["minX"], y))
            borderCells.append((minMaxEndArea["maxX"], y))
        
        return borderCells

    @staticmethod
    def getMinMaxCoordinatesOfCells(cells: list):
        '''Returns an dictionary containing the min max coordinates from Cells.Cells.

        Note: Example
            getMinMaxCoordinatesOfCells([(1,2), (2,1)]) -> {minX:1, maxX:2, minY:1, maxY:2}

        Args:
            cells (list(Cell)): List containing Cells or tuples from which the min and max coordinate should be derived.
        
        Returns:
            dict: containing the minX, maxX, minY, maxY values of the inputted cells
        '''

        result = {}

        ErrorRaiser.raiseIsNotList(cells)
        for c in cells:
            cell = Cell.raiseIsNotCellIfApplicable(c)

            # minX
            if "minX" in result:
                if cell[0] < result["minX"]:
                    result["minX"] = cell[0]
            else:
                result["minX"] = cell[0]

            # minY
            if "minY" in result:
                if cell[1] < result["minY"]:
                    result["minY"] = cell[1]
            else:
                result["minY"] = cell[1]
            
            # maxX
            if "maxX" in result:
                if cell[0] > result["maxX"]:
                    result["maxX"] = cell[0]
            else:
                result["maxX"] = cell[0]

            # maxY
            if "maxY" in result:
                if cell[1] > result["maxY"]:
                    result["maxY"] = cell[1]
            else:
                result["maxY"] = cell[1]

        return result

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
        """Deletes all walls between cells.

        Args:
            cellStart (Cell | tuple): First cell in one corner to remove wall from
            cellEnd (Cell | tuple): Second cell in other corner to remove wall from
        """

        cellStart = Cell.raiseIsNotCellIfApplicable(cellStart)
        cellEnd = Cell.raiseIsNotCellIfApplicable(cellEnd)

        minX = 0
        maxX = 0
        minY = 0
        maxY = 0

        if cellStart[0] < cellEnd[0]:
            minX = cellStart[0]
            maxX = cellEnd[0]
        else:
            minX = cellEnd[0]
            maxX= cellStart[0]
        
        if cellStart[1] < cellEnd[1]:
            minY = cellStart[1]
            maxY = cellEnd[1]
        else:
            minY = cellEnd[1]
            maxY = cellStart[1]
        
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                cell = self.maze[y][x]

                if x != minX:
                    cell.deleteWall("left")
                if x != maxX:
                    cell.deleteWall("right")
                if y != minY:
                    cell.deleteWall("bottom")
                if y != maxY:
                    cell.deleteWall("top")
                 
    # Manage Neighbors
    def getNeighborByKey(self, cell, key):
        ''' Returns the coordinates of the neighbor referenced by an key.

        Args:
            cell (Cell | tuple): with coordinates from Cells.Cell from which the neighbor is searched.
            key (str): that describes what neighbor is searched. Possible keys are ["top", "right", "bottom", "left"]

        Returns:
            tuple: returns a tuple with the coordinates of the neighbor.
        
        '''
        key = Cell.raiseNotWallType(key)
        cell = Cell.raiseIsNotCellIfApplicable(cell)

        if key == "top":
            cell = (cell[0], cell[1] + 1)

        if key == "right":
            cell = (cell[0] + 1, cell[1])

        if key == "bottom":
            cell = (cell[0], cell[1] - 1)

        if key == "left":
            cell = (cell[0] - 1, cell[1])

        self.raiseNotInMazeIfApplicable(cell[0], cell[1])

        return cell

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
        """Gets a random not visited neighbor from a cell.

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

    @abc.abstractclassmethod
    def generate(self, startCell= (0,0)):
        pass

# c1 = Cell(5,5)
# c2 = Cell(7,7)

# print(Maze.raiseCellsAreNotNeighborIfApplicable(c1, c2))

# m = Maze(8,8)
# print(m.maze[4][4].type)
# print(m.maze)

# m.deleteWallsBetween((5,5), (5,6))
# m.deleteWallsBetween((5,5), (5,4))

# print(m.maze[5][5].walls)

# viz = Visualizer()
# viz.genericShapes(m.getVizShape())
