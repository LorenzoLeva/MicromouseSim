from datetime import datetime
import random
import sys
from Maze import Maze
from ErrorRaiser import ErrorRaiser

import abc

class Mouse(metaclass= abc.ABCMeta):
    def __init__(self, seed=None) -> None:
        self.maze = None
        self.visited = None
        self.currentPosition = None
        self.hasSolution = False

        if seed is None:
            self.seed = random.randrange(sys.maxsize)
        else:
            ErrorRaiser.raiseErrorOnlyInt(seed, "mouse.seed")
            self.seed = seed
       
    def solve(self, maze: Maze, seed: int = None) -> None:
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

        self.setMaze(maze, seed)
        self.startTime = datetime.now()
        self.solveMaze()
        self.endTime = datetime.now()

        self.hasSolution = True

        return self.solution

    @abc.abstractclassmethod
    def solveMaze(self):
        '''This function solves the maze and generates self.solution dictionary containing all the information about the solution.
        
        Note:
            The self.solution dictionary has to have the following structure:
                {
                    solutionPath: array of coordinates in tuple form describing the path the mouse found.
                }
        '''
        pass

    def setMaze(self, maze: Maze, seed: int = None) -> None:
        '''Sets up the mouse with all the Maze information it needs.'''
        self.hasSolution = False

        self.maze = Maze.raiseNotMaze(maze)
        self.visited = [[False for x in range(self.maze.x)] for y in range(self.maze.y)]

        self.currentPosition = self.maze.getStartPosition()
        self.solution = {}

        if seed is not None:
            self.seed = seed
        random.seed(self.seed)
