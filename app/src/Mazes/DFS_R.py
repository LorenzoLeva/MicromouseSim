from Mazes.Maze import Maze
from Cells.Cell import Cell


class DFS_R(Maze):
    """TODO add Doc
    https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_implementation
    """
    def __init__(self, columns: int=16, rows: int=16, seed=None) -> None:
        super().__init__(columns, rows, seed)
        self.current = (0,0)
        self.backlog = []

    def generate(self, startCell= (0,0)):
        #TODO is already generated block
        #TODO add reset method
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
    
# maze = DFS_R(16, 16)
# maze.generate((0,0))
# maze.visualize()

# print(maze.seed)
# maze2 = DFS_R(16, 16, maze.seed)
# print(maze2.seed)
# maze2.generate((8,8))

# print(maze.maze[0][0].walls)
# print(maze2.maze[0][0].walls)
# if maze.maze is maze2.maze:
#     print("Hello")

# maze3 = DFS_R(16, 16)
# maze3.generate((8,8))
# print(maze.getNotVisitedNeighbors((0,0)))
# print(maze.getNotVisitedNeighbors((8,0)))
# print(maze.getNotVisitedNeighbors((8,12)))
# print(maze.getNotVisitedNeighbors((0,12)))
# print(maze.getNotVisitedNeighbors((5,6)))
