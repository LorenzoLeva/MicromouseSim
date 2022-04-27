from MazeGenerator import MazeGenerator
from Visualizer import Visualizer


class DFS_R(MazeGenerator):
    """TODO add Doc
    https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_implementation
    """
    def generate(self):
        pass
    
    def visualize(self):
        viz = Visualizer()
        viz.genericShapes(self.getVizShape())
    
maze = DFS_R(9,16)
maze.visualize()