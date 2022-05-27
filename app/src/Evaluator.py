import abc
from ErrorRaiser import ErrorRaiser
from Mouse import Mouse
from Maze import Maze

class Evaluator(metaclass=abc.ABCMeta):
    def __init__(self, mouse: Mouse, maze: Maze) -> None:
        '''An object to evaluate the performance of an mouse in a maze. 
        
        Args:
            mouse (Mouse): is the mouse to be evaluated
            maze (Maze): is the maze on which the mouse should be evaluated on.
        '''

        ErrorRaiser.raiseIsNotType(Mouse, mouse, "mouse")
        ErrorRaiser.raiseIsNotType(Maze, maze, "maze")

        self.mouse = mouse
        self.maze = maze

    def evaluate(self, mouse: Mouse = None, maze: Maze = None):
        '''Evaluates the mouse performance. 
        
        Args:
            mouse (Mouse): is the mouse to be evaluated
            maze (Maze): is the maze on which the mouse should be evaluated on.

        Returns:
            float: Score of the performance of the mouse.
        '''

        if mouse is not None:
            ErrorRaiser.raiseIsNotType(Mouse, mouse, "mouse")
            self.mouse = mouse

        if maze is not None:
            ErrorRaiser.raiseIsNotType(Maze, maze, "maze")
            self.maze = maze

        self.mouse.solve(self.maze)
        return self.score()

    @abc.abstractclassmethod
    def score(self):
        '''Scores the mouse performance in the maze.
        
        Returns:
            float: Score of the performance of the mouse.
        '''
