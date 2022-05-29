import abc

from Evaluators.Evaluator import Evaluator
from Mazes.Maze import Maze
from Mice.Mouse import Mouse
from Simulations.Simulation import Simulation
from Tools.ErrorRaiser import ErrorRaiser


class DataBase(metaclass= abc.ABCMeta):
    @abc.abstractclassmethod
    def insertMouse(self, mouse: Mouse, simID: int) -> int:
        '''Inserts the mouse in the DataBase and returns its id.

        Args:
            mouse (Mouse): Mouse to be inserted into the DB.
            simID (int): ID of the parent simulator

        Returns:
            int: ID of the inserted mouse.
        '''
    
    @abc.abstractclassmethod
    def insertMaze(self, maze: Maze, simID: int) -> int:
        '''Inserts the maze in the DataBase and returns its id.

        Args:
            maze (Maze): Maze to be inserted into the DB.
            simID (int): ID of the parent simulator

        Returns:
            int: ID of the inserted maze.
        '''
    
    @abc.abstractclassmethod
    def insertSimulation(self, sim: Simulation) -> int:
        '''Inserts the simulation in the DataBase and returns its id.
        
        Returns:
            int: ID of the inserted simulation.
        '''

    @abc.abstractclassmethod
    def insertEvaluator(self, evaluator: Evaluator, simID: int) -> int:
        '''Inserts the evaluator in the DataBase and returns its id.

        Args:
            evaluator (Evaluator): Evaluator to be inserted into the DB.
            simID (int): ID of the parent simulator

        Returns:
            int: ID of the inserted evaluator.
        '''

