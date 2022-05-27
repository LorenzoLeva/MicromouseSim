from Evaluators.Evaluator import Evaluator
from Mazes.Maze import Maze
from Mice.Mouse import Mouse

class PathLengthEvaluator(Evaluator):
    def __init__(self, mouse: Mouse, maze: Maze) -> None:
        super().__init__(mouse, maze)
    
    def score(self):
        self.scoreResults = len(self.mouse.solution["solutionPath"])
        self.timeToSolve = self.mouse.endTime - self.mouse.startTime
        return self.scoreResults
        