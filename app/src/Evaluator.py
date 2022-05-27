import abc
from datetime import datetime
from re import S

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
    '''
    def __init__(self, mouse: Mouse, maze: Maze) -> None:

        ErrorRaiser.raiseNotSubclass(Mouse, mouse, "Evaluator.mouse")
        ErrorRaiser.raiseNotSubclass(Maze, maze, "Evaluator.maze")

        self.mouse = mouse
        self.maze = maze

        self.scoreResults = None
        self.timeToSolve = None

    def evaluate(self, solved: bool = False):
        '''Evaluates the mouse performance. 

        Args:
            solved (bool):  describes if the mouse already solved the maze. 
                            - False:  the Evaluator makes the mouse solve the maze and then scores the mouse performance.
                            - True:   the Evaluator doesn't makes the mouse solve the maze but it impiety scores the mouse performance.

        Returns:
            float: Score of the performance of the mouse.
        '''
        ErrorRaiser.raiseIsNotType(bool, solved)

        if not solved:
            self.mouse.solve(self.maze)
        else:
            if not self.mouse.hasSolution:
                raise Exception("Mouse hasn't a solution. Set solved to False or make the mouse solve a maze prior of evaluating it.")

        self.score()

        return dict(score=self.scoreResults, time=self.timeToSolve)

    @abc.abstractclassmethod
    def score(self):
        '''Scores the mouse performance in the maze.
        
        Returns:
            float: Score of the performance of the mouse.
        '''
