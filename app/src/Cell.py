import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ErrorRaiser import ErrorRaiser

class Cell:
    """Object that represents a cell of the maze.
        
        Args:
            x (int): x coordinate of the cell. Can't be negative.
            y (int): y coordinate of the cell. Can't be negative.
            type (str): is the type of the cell. It can be one of the following ["normal", "start", "end"]

        Attributes:
            x (int): x coordinate of the cell. Can't be negative.
            y (int): y coordinate of the cell. Can't be negative.
            walls (dict of bool): Dictionary with ["top", "right", "bottom", "left"] keys that describe if there is a wall through an bool.
            width (int): is the with of a cell. Used for visualization.
    """
    def __init__(self, x: int, y: int, type: str= "normal") -> None: 
        ErrorRaiser.raiseNoNegativeInt(x, "x")
        ErrorRaiser.raiseNoNegativeInt(y, "y")

        self.type = Cell.raiseNotCellType(type, "cell.type")
        
        self.x = x
        self.y = y
        self.width = 1
        self.walls = {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : True 
        }

    def deleteWall(self, wall: str):
        """Sets the specified wall to False.

        Args:
            wall (str): The key of the wall to delete. Possible keys are: ["top", "right", "bottom", "left"]
        """
        wall = Cell.raiseNotWallType(wall)
        
        self.walls[wall] = False
        
    def buildWall(self, wall: str):
        """Sets the specified wall to True.

        Args:
            wall (str): The key of the wall to delete. Possible keys are: ["top", "right", "bottom", "left"]
        """
        wall = Cell.raiseNotWallType(wall)
        
        self.walls[wall] = True  

    @staticmethod
    def raiseIsNotCellIfApplicable(cell):
        """Raises an error if the cell is not the right type. If everything is ok it passes the cell.

        Args:
            cell (tuple | Cell): the cell that has to be checked the type of.

        Returns:
            tuple: if the type is correct it passes the cell as a tuple.
        """
        if type(cell) is Cell:
            cell = (cell.x, cell.y)
        
        cell = ErrorRaiser.raiseIsNotTuple(cell)

        return cell 

    @staticmethod
    def raiseNotCellType(x: str, name=""):
        possibleCellTypes = ["normal", "start", "end"]
        ErrorRaiser.raiseErrorOnlyStr(x)
        
        x = x.lower()
        return ErrorRaiser.raiseNotValidKey(x, possibleCellTypes, name)

    @staticmethod
    def raiseNotWallType(x: str, name=""):
        possibleWallTypes = ["top", "right", "bottom", "left"]
        ErrorRaiser.raiseErrorOnlyStr(x)

        x = x.lower()
        return ErrorRaiser.raiseNotValidKey(x, possibleWallTypes)

    def minus(self, cell):
        """Subtracts one cell from the other. 

        Args:
            cell (tuple | Cell): the cell to subtract from the self cell.

        Returns:
            tuple: difference from the cells that is also the vector from cell to self
        """
        cell = Cell.raiseIsNotCellIfApplicable(cell)
        return (self.x - cell[0], self.y - cell[1])

    def getVizShape(self) -> list:
        """This function generates the list with 0-4 dict describing the walls so that they can be drawn in plotly.
        
        Returns:
            list: Returns a list of dir describing the walls so that they can be drawn in plotly. 
        """
        shape = []

        # Bottom
        if self.walls["bottom"]:
            shape.append(
                dict(type="line", xref="x", yref="y", line_width=3, line_color="green",
                    x0=self.x, 
                    y0=self.y, 
                    x1=self.x + self.width, 
                    y1=self.y
                )
            )

        # Right
        if self.walls["right"]:
            shape.append(
                dict(type="line", xref="x", yref="y", line_width=3, line_color="red",
                    x0=self.x + self.width, 
                    y0=self.y, 
                    x1=self.x + self.width, 
                    y1=self.y + self.width
                )
            )

        # Top
        if self.walls["top"]:
            shape.append(
                dict(type="line", xref="x", yref="y", line_width=3, line_color="blue",
                    x0=self.x + self.width, 
                    y0=self.y + self.width, 
                    x1=self.x, 
                    y1=self.y + self.width
                )
            )

        # Left
        if self.walls["left"]:
            shape.append(
                dict(type="line", xref="x", yref="y", line_width=3, line_color="orange",
                    x0=self.x, 
                    y0=self.y + self.width, 
                    x1=self.x, 
                    y1=self.y
                )
            )

        return shape
