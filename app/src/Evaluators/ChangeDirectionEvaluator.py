from Evaluators.Evaluator import Evaluator
from Mazes.Maze import Maze
from Mice.Mouse import Mouse

class ChangeDirectionEvaluator(Evaluator):
    '''Calculates how often the mouse changed the direction in the maze.'''
    def __init__(self, mouse: Mouse, maze: Maze) -> None:
        super().__init__(mouse, maze)
    
    def score(self):
        directionChanges = 0

        lastCell = self.mouse.solution["solutionPath"][1]
        currentDir = (lastCell[0]- self.mouse.solution["solutionPath"][0][0], lastCell[1] - self.mouse.solution["solutionPath"][0][1])

        for c in self.mouse.solution["solutionPath"][2:]:
            direction = (c[0]-lastCell[0], c[1]-lastCell[1])
            if currentDir != direction:
                directionChanges += 1

            lastCell = c

        self.scoreResults = directionChanges
        self.timeToSolve = self.mouse.endTime - self.mouse.startTime
        return self.scoreResults
        
