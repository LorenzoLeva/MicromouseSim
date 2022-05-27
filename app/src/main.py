
from Simulations.SingleRunSimulation import SingleRunSimulation
from Mice.RandomWalker import RandomWalker
from Mazes.DFS_R import DFS_R
from Evaluators.PathLengthEvaluator import PathLengthEvaluator

mouse = RandomWalker()

sim = SingleRunSimulation(mouse, DFS_R, PathLengthEvaluator)
sim.run()

print(f'Simulation result: {sim.results["score"]} steps to solve the maze in {sim.results["time"]}')
