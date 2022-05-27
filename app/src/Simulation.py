import abc

from RandomWalker import RandomWalker


class Simulation(metaclass= abc.ABCMeta):
    def __init__(self, MouseType) -> None:
        self.mouse = MouseType()
    
    @abc.abstractclassmethod
    def run(self):
        '''This function runs the simulation and returns the results of the Simulation.
        
        '''
        pass
