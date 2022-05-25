import random

from hypothesis import seed
from Mouse import Mouse
from DFS_R import DFS_R

class RandomWalker(Mouse):
    def __init__(self, seed:int = None) -> None:
        super().__init__(seed)
    
    def solveMaze(self):
        self.solution["solutionPath"] = []
        i=0
        while not self.maze.isEndPosition(self.currentPosition):
            i+= 1
            if i % 10 == 0:
                print(".", end="")

            self.solution["solutionPath"].append(self.currentPosition)
            possibleNextSteps = self.maze.getNextSteps(self.currentPosition)
            nextCell = random.choice(possibleNextSteps)

            self.currentPosition = self.maze.getNeighborByKey(self.currentPosition, nextCell)


        print(f'\nArrived at:{self.currentPosition} in {len(self.solution["solutionPath"])} steps.')



# maze = DFS_R(seed=123)
# maze.generate()

# mouse = RandomWalker(seed= 321)
# mouse2 = RandomWalker(seed= 123)
# mouse.solve(maze)
# mouse2.solve(maze)