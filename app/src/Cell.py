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

    def deleteAllWalls(self):
        '''Sets all walls to False.'''

        for w in self.walls:
            self.deleteWall(w)

    def deleteWall(self, wall: str):
        """Sets the specified wall to False.

        Args:
            wall (str): The key of the wall to delete. Possible keys are: ["top", "right", "bottom", "left"]
        """
        wall = Cell.raiseNotWallType(wall)
        
        self.walls[wall] = False

    def buildAllWalls(self):
        '''Sets all walls to True.'''

        for w in self.walls:
            self.buildWall(w)

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

        # Corners
        bottomLeft= {
            'x': self.x,
            'y': self.y
        }

        bottomRight = {
            'x': self.x + self.width,
            'y': self.y
        }

        topLeft = {
            'x': self.x,
            'y': self.y + self.width
        }

        topRight = {
            'x': self.x + self.width,
            'y': self.y + self.width
        }

        if self.type != "normal":
            color = "grey"

            if self.type == "start":
                color = "green"
            elif self.type == "end":
                color = "red"
            shape.append(
                dict(type="rect", xref="x", yref="y", line_width=0, fillcolor=color, opacity=0.2,
                    x0 = bottomLeft["x"], 
                    x1 = topRight["x"],
                    y0 = bottomLeft["y"],
                    y1 = topRight["y"]
                )

            )



        # Bottom Wall
        if self.walls["bottom"]:
            shape.append(
                dict(type="line", xref="x", yref="y", line_width=3, line_color="green",
                    x0=bottomLeft["x"], 
                    y0=bottomLeft["y"], 
                    x1=bottomRight["x"], 
                    y1=bottomRight["y"]
                )
            )

        # Right Wall
        if self.walls["right"]:
            shape.append(
                dict(type="line", xref="x", yref="y", line_width=3, line_color="red",
                    x0=bottomRight["x"], 
                    y0=bottomRight["y"], 
                    x1=topRight["x"], 
                    y1=topRight["y"]
                )
            )

        # Top Wall
        if self.walls["top"]:
            shape.append(
                dict(type="line", xref="x", yref="y", line_width=3, line_color="blue",
                    x0=topLeft["x"], 
                    y0=topLeft["y"], 
                    x1=topRight["x"], 
                    y1=topRight["y"]
                )
            )

        # Left Wall
        if self.walls["left"]:
            shape.append(
                dict(type="line", xref="x", yref="y", line_width=3, line_color="orange",
                    x0=bottomLeft["x"], 
                    y0=bottomLeft["y"], 
                    x1=topLeft["x"], 
                    y1=topLeft["y"]
                )
            )

        return shape
