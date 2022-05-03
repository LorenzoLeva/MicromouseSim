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

    def generate(self, startCell= (0,0)):
        self.current = Cell.raiseIsNotCellIfApplicable(startCell)
        # Mark the current cell as visited
        self.visited[self.current[1]][self.current[0]] = True
        nextCell = self.choseRandomNeighbor(self.current)
        if nextCell:
            # Remove the wall between the current cell and the chosen cell
            self.deleteWallsBetween(self.current, nextCell)
            # Invoke the routine recursively for a chosen cell
            self.generate(nextCell)
        else:
            # TODO Backtrack to last cell with neighbors
            print("Im stuck.")
    
maze = DFS_R(16, 16)
maze.generate((8,8))
maze.visualize()
# maze.getShape()
# print(maze.getNotVisitedNeighbors((0,0)))
# print(maze.getNotVisitedNeighbors((8,0)))
# print(maze.getNotVisitedNeighbors((8,12)))
# print(maze.getNotVisitedNeighbors((0,12)))
# print(maze.getNotVisitedNeighbors((5,6)))
