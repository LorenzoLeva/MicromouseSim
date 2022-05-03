import random
from MazeGenerator import MazeGenerator
from Visualizer import Visualizer
from Cell import Cell


class DFS_R(MazeGenerator):
    """TODO add Doc
    https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_implementation
    """
    def __init__(self, columns: int, rows: int) -> None:
        super().__init__(columns, rows)
        self.visited = [[False for x in range(self.x)] for y in range(self.y)]
        self.current = (0,0)

    def isCoordinateInMaze(self, x, y):
        return (x >= 0 and x < self.x and y >= 0 and y < self.y)

    def raiseNotInMazeIfApplicable(self, x, y):
        if not self.isCoordinateInMaze(x, y):
            raise IndexError(f'Cell isn\'t within the maze. X has to be between 0 and {self.x - 1}(included) and Y has to be between 0 and {self.y - 1}(included). Got X:{x}, Y:{y}')
    
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

        choices = self.getNotVisitedNeighbors()
        
        if len(choices) > 0:
            return random.choice(choices)
        else:
            return None

    def generate(self, startX = 0, startY = 0):
        self.current = (startX, startY)
        # Mark the current cell as visited
        self.visited[self.current[0]][self.current[1]] = True
        nextCell = self.choseRandomNeighbor(self.current)
        if nextCell:
            # Remove the wall between the current cell and the chosen cell
            # Invoke the routine recursively for a chosen cell
            pass
        else:
            # Backtrack to last cell with neighbors
            print("Im stuck.")
    
    def visualize(self):
        viz = Visualizer()
        viz.genericShapes(self.getVizShape())
    
maze = DFS_R(9, 13)
# maze.visualize()
maze.getShape()
print(maze.getNotVisitedNeighbors((0,0)))
print(maze.getNotVisitedNeighbors((8,0)))
print(maze.getNotVisitedNeighbors((8,12)))
print(maze.getNotVisitedNeighbors((0,12)))
print(maze.getNotVisitedNeighbors((5,6)))
