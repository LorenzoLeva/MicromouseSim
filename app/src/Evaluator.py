import abc
from datetime import datetime

from ErrorRaiser import ErrorRaiser
from Mouse import Mouse
from Maze import Maze

class Evaluator(metaclass=abc.ABCMeta):
    '''An object to evaluate the performance of an mouse in a maze. 
        
    Args:
        mouse (Mouse): is the mouse to be evaluated
        maze (Maze): is the maze on which the mouse should be evaluated on.

    Attributes:
        mouse (Mouse): is the mouse to be evaluated
        maze (Maze): is the maze on which the mouse should be evaluated on.
        startTime (datetime): is the time when the mouse starts to solve the maze.
        endTime (datetime): is the time when the mouse finished to solve the maze.
    '''
    def __init__(self, mouse: Mouse, maze: Maze) -> None:

        ErrorRaiser.raiseNotSubclass(Mouse, mouse, "Evaluator.mouse")
        ErrorRaiser.raiseNotSubclass(Maze, maze, "Evaluator.maze")

        self.mouse = mouse
        self.maze = maze

        self.startTime = None
        self.endTime = None

    def evaluate(self):
        '''Evaluates the mouse performance. 

        Returns:
            float: Score of the performance of the mouse.
        '''

        self.startTime = datetime.now()
        self.mouse.solve(self.maze)
        self.endTime = datetime.now()

        return self.score()

    @abc.abstractclassmethod
    def score(self):
        '''Scores the mouse performance in the maze.
        
        Returns:
            float: Score of the performance of the mouse.
        '''
