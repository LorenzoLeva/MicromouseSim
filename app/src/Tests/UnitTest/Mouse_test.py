from operator import imod
import unittest
from unittest.mock import patch

from Mice.Mouse import Mouse
from Mazes.Maze import Maze

class TestMouseInitialization(unittest.TestCase):
   @patch("Mice.Mouse.Mouse.__abstractmethods__", set())
   def test_initialization(self):
        """Test if the Mouse class initializes correctly an object with all its properties correctly."""
        
        mouse = Mouse()

        self.assertTrue(hasattr(mouse, "maze"))
        self.assertTrue(hasattr(mouse, "visited"))
        self.assertTrue(hasattr(mouse, "currentPosition"))
        
class TestSetMaze(unittest.TestCase):
   @patch("Mice.Mouse.Mouse.__abstractmethods__", set())
   def test_invalid_input_types(self):
      """Test if the Mouse.setMaze method raises TypeError when called with the wrong parameter type."""

      mouse = Mouse()

      self.assertRaises(TypeError,  mouse.setMaze, "ABC")
      self.assertRaises(TypeError,  mouse.setMaze, 2)
      self.assertRaises(TypeError,  mouse.setMaze, True)

   @patch("Mice.Mouse.Mouse.__abstractmethods__", set())
   @patch("Mazes.Maze.Maze.__abstractmethods__", set())
   def test_valid_input(self):
      """Test if the Mouse.setMaze method stores the values correctly."""

      mouse = Mouse()
      maze = Maze(16, 16)

      mouse.setMaze(maze)

      self.assertEqual(mouse.maze, maze)
      self.assertEqual(len(mouse.visited), len(maze.maze))
      self.assertEqual(len(mouse.visited[0]), len(maze.maze[0]))




        
