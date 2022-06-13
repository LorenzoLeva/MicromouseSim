from Mazes.Maze import Maze
from Cells.Cell import Cell


class DFS_R(Maze):
    """The DFS_R generates a maze with the Depth first search (Recursive implementation) algorithm. For more information please refer to https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_implementation"""
    def __init__(self, columns: int=16, rows: int=16, seed=None) -> None:
        super().__init__(columns, rows, seed)
        self.current = (0,0)
        self.backlog = []

    def generate(self, startCell= (0,0)):
        self.current = Cell.raiseIsNotCellIfApplicable(startCell)
        # Mark the current cell as visited
        self.visited[self.current[1]][self.current[0]] = True
        nextCell = self.choseRandomNeighbor(self.current)
        if nextCell:
            # Adds cell to backlog
            self.backlog.append(self.current)
            # Remove the wall between the current cell and the chosen cell
            self.deleteWallsBetween(self.current, nextCell)
            # Invoke the routine recursively for a chosen cell
            self.generate(nextCell)
        else:
            # Backtrack to the last cell
            if len(self.backlog) > 0:
                self.generate(self.backlog.pop(-1))
