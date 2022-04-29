import plotly.graph_objects as go
from plotly.subplots import make_subplots


class Cell:
    """TODO add doc"""
    def __init__(self, x: int, y: int) -> None:
        if type (x) is not int:
            raise TypeError("Only integers are allowed. Received for x:", type (x), x)
        
        if type (y) is not int:
            raise TypeError("Only integers are allowed. Received for y:", type (y), y)
        
        self.x = x
        self.y = y
        self.width = 1
        self.walls = {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : True 
        }

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







# # TODO remove this test section
# # TODO create Unit test to test cell class
# c1 = Cell(0, 0)
# c2 = Cell(1, 1)

# shapes = []
# shapes += c1.getShape()
# shapes += c2.getShape()

# print(shapes)


# # Create Subplots
# fig = make_subplots(rows=1, cols=1)

# fig.add_trace(go.Scatter(x=[], y=[]), row=1, col=1)

# # Add shapes
# fig.update_layout(
#     shapes=shapes)
# fig.show()