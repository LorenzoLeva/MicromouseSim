
from SingleRunSimulation import SingleRunSimulation
from RandomWalker import RandomWalker
from DFS_R import DFS_R
from PathLengthEvaluator import PathLengthEvaluator

mouse = RandomWalker()

sim = SingleRunSimulation(mouse, DFS_R, PathLengthEvaluator)
sim.run()

print(f'Simulation result: {sim.results["score"]} steps to solve the maze in {sim.results["time"]}')
