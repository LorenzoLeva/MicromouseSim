from Maze import Maze


class Mouse:
    def __init__(self, maze: Maze) -> None:

        self.maze = Maze.raiseNotMaze(maze)
        self.visited = [[False for x in range(self.maze.x)] for y in range(self.maze.y)]

        




