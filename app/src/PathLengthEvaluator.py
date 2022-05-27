from Evaluator import Evaluator
from Maze import Maze
from Mouse import Mouse

class PathLengthEvaluator(Evaluator):
    def __init__(self, mouse: Mouse, maze: Maze) -> None:
        super().__init__(mouse, maze)
    
    def score(self):
        self.scoreResults = len(self.mouse.solution["solutionPath"])
        self.timeToSolve = self.mouse.endTime - self.mouse.startTime
        return self.scoreResults
        