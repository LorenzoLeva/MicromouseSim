from operator import imod
import unittest

from app.src.Mouse import Mouse
from app.src.Maze import Maze

class TestMouseInitialization(unittest.TestCase):
     def test_invalid_input_types(self):
        """Test if the Mouse class raises TypeError when initialized with the wrong parameter type."""

        self.assertRaises(TypeError, Mouse, "x")

     def test_initialization(self):
        """Test if the Mouse class initializes correctly an object with all its properties correctly."""

        columns = 3
        rows = 4
        seed = 123

        maze = Maze(columns, rows, seed)
        mouse = Mouse(maze)

        self.assertEqual(mouse.maze, maze)
        

        
