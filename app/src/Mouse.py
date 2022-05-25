from Maze import Maze


class Mouse:
    def __init__(self) -> None:
        self.maze = None
        self.visited = None
        self.currentPosition = None
        self.solution = None
        
    def solve(self, maze: Maze) -> None:
        '''Makes the mouse solve the maze passed as params.
        
        Args:
            maze (Maze): the maze to be solved by the mouse.

        Returns:
            dict: dictionary containing the solution of the maze with some metadata

            The dict that is returned has the following structure:
                {
                    solutionPath: array of coordinates in tuple form describing the path the mouse found.
                }
        '''

        self.setMaze(maze)
        self.solveMaze(maze)
        return self.solution

        

    def solveMaze(self):
        '''This function solves the maze and generates self.solution dictionary containing all the information about the solution.
        
        Note:
            The self.solution dictionary has to have the following structure:
                {
                    solutionPath: array of coordinates in tuple form describing the path the mouse found.
                }
        '''
        raise NotImplementedError("The Maze class is an abstract class. Please implement the solveMaze method in a child class to be able to call Maze.solve.")

    def setMaze(self, maze: Maze) -> None:
        '''Sets up the mouse with all the Maze information it needs.'''
        self.maze = Maze.raiseNotMaze(maze)
        self.visited = [[False for x in range(self.maze.x)] for y in range(self.maze.y)]

        self.currentPosition = self.maze.getStartPosition()
        self.solution = {}
