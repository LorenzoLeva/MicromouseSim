from Simulations.Simulation import Simulation

from Mazes.DFS_R import DFS_R
from Evaluators.Evaluator import Evaluator
from Mazes.Maze import Maze
from Mice.Mouse import Mouse

class SingleRunSimulation(Simulation):
    def __init__(self, mouse: Mouse, MazeType: Maze, EvaluatorType: Evaluator) -> None:
        super().__init__(mouse, EvaluatorType)
        self.MazeType = MazeType
        self.EvaluatorType = EvaluatorType

        self.results = None

    def run(self):
        self.maze = self.MazeType()
        self.maze.generate()

        self.evaluator = self.EvaluatorType(self.mouse, self.maze)
        
        self.results = self.evaluator.evaluate()

