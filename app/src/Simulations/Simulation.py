import abc

from Mice.Mouse import Mouse
from Evaluators.Evaluator import Evaluator


class Simulation(metaclass= abc.ABCMeta):
    def __init__(self, mouse: Mouse, EvaluatorType: Evaluator) -> None:
        self.EvaluatorType = EvaluatorType

        self.mouse = mouse

    @abc.abstractclassmethod
    def run(self):
        '''This function runs the simulation and returns the results of the Simulation.
        
        '''
        pass
