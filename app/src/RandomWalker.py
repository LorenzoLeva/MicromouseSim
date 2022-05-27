import random

from hypothesis import seed
from Mouse import Mouse
from DFS_R import DFS_R

class RandomWalker(Mouse):
    def __init__(self, seed:int = None) -> None:
        super().__init__(seed)
    
    def solveMaze(self):
        self.solution["solutionPath"] = []

        while not self.maze.isEndPosition(self.currentPosition):
            self.solution["solutionPath"].append(self.currentPosition)
            possibleNextSteps = self.maze.getNextSteps(self.currentPosition)
            nextCell = random.choice(possibleNextSteps)

            self.currentPosition = self.maze.getNeighborByKey(self.currentPosition, nextCell)


# maze = DFS_R(seed=123)
# maze.generate()

# mouse = RandomWalker(seed= 321)
# mouse2 = RandomWalker(seed= 123)
# mouse.solve(maze)
# mouse2.solve(maze)