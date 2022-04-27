from MazeGenerator import MazeGenerator
from Visualizer import Visualizer


class DFS_R(MazeGenerator):
    def generate(self):
        pass
    
    def visualize(self):
        viz = Visualizer()
        viz.genericShapes(self.getVizShape())
    
maze = DFS_R(10,10)
maze.visualize()