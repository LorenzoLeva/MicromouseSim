from Simulation import Simulation

from RandomWalker import RandomWalker
from DFS_R import DFS_R
from Evaluator import Evaluator
from Maze import Maze
from Mouse import Mouse

class SingleRunSimulation(Simulation):
    def __init__(self, mouse: Mouse, MazeType: Maze, EvaluatorType: Evaluator) -> None:
        super().__init__(mouse, EvaluatorType)
        self.MazeType = MazeType
        self.EvaluatorType = EvaluatorType

        self.results = None

    def run(self):
        self.maze = self.MazeType()
        self.evaluator = self.EvaluatorType(self.mouse, self.maze)
        
        self.results = self.evaluator.evaluate()
        #TODO evaluate solution


sim = SingleRunSimulation(RandomWalker, DFS_R)
sim.run() 