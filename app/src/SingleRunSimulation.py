from Simulation import Simulation

from RandomWalker import RandomWalker
from DFS_R import DFS_R

class SingleRunSimulation(Simulation):
    def __init__(self, mouseType, MazeType) -> None:
        super().__init__(mouseType)
        self.maze = MazeType()
        self.solution = None

    def run(self):
        self.maze.generate()
        self.solution = self.mouse.solve(self.maze)
        
        #TODO evaluate solution


sim = SingleRunSimulation(RandomWalker, DFS_R)
sim.run() 