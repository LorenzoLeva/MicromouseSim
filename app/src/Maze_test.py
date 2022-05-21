import unittest

from app.src.Cell import Cell
from app.src.Maze import Maze

class TestMazeInitialization(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the Maze class raises TypeError when initialized with the wrong parameter type."""
        # No seed
        self.assertRaises(TypeError, Maze, "x", "y")
        self.assertRaises(TypeError, Maze, "3", "3")
        self.assertRaises(TypeError, Maze, 3, "y")
        self.assertRaises(TypeError, Maze, "x", 3)

        self.assertRaises(TypeError, Maze, True, True)
        self.assertRaises(TypeError, Maze, 3, True)
        self.assertRaises(TypeError, Maze, True, 3)

        # With seed
        # Strings
        self.assertRaises(TypeError, Maze, "x", "y", "seed")
        self.assertRaises(TypeError, Maze, "3", "3", "123")
        self.assertRaises(TypeError, Maze, 3, "y", 123)
        self.assertRaises(TypeError, Maze, "x", 3, 123)
        self.assertRaises(TypeError, Maze, 3, 3, "123")


        self.assertRaises(TypeError, Maze, True, True, False)
        self.assertRaises(TypeError, Maze, 3, True, True)
        self.assertRaises(TypeError, Maze, True, 3, True)


    def test_invalid_input_range(self):
        """Test if the Maze class raises IndexError when initialized with negative or zero size parameter type."""
        # Negative
        self.assertRaises(IndexError, Maze, 2, -2)
        self.assertRaises(IndexError, Maze, -2, 2)
        self.assertRaises(IndexError, Maze, -2, -2)

        # Zero
        self.assertRaises(IndexError, Maze, 2, 0)
        self.assertRaises(IndexError, Maze, 0, 2)
        self.assertRaises(IndexError, Maze, 0, 0)

    def test_initialization(self):
        """Test if the Maze class initializes correctly an object with all its properties correctly."""
        columns = 3
        rows = 4
        seed = 123

        maze = Maze(columns, rows, seed)

        self.assertEqual(maze.x, columns)
        self.assertEqual(maze.y, rows)
        self.assertEqual(maze.seed, seed)

        self.assertEqual(len(maze.visited), rows)
        self.assertEqual(len(maze.visited[0]), columns)
        self.assertEqual(type(maze.visited[0][0]), bool)

        self.assertEqual(len(maze.maze), rows)
        self.assertEqual(len(maze.maze[0]), columns)
        self.assertEqual(type(maze.maze[0][0]), Cell)

class TestMazeRaiseCellsAreNotNeighborIfApplicable(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the Maze.raiseCellsAreNotNeighborIfApplicable method raises TypeError when called with the wrong parameter type."""
        
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, 1, 1)
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, True, True)
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, ("1", "2"), ("2", "2"))

    def test_valid_input(self):
        """Test if the Maze.raiseCellsAreNotNeighborIfApplicable method passes correctly the tuple."""
        # With Cells Neighbor
        self.assertEqual(Maze.raiseCellsAreNotNeighborIfApplicable(Cell(1,1), Cell(1,2)), (0,1))
        self.assertEqual(Maze.raiseCellsAreNotNeighborIfApplicable(Cell(1,1), Cell(1,0)), (0,-1))
        self.assertEqual(Maze.raiseCellsAreNotNeighborIfApplicable(Cell(1,1), Cell(2,1)), (1,0))
        self.assertEqual(Maze.raiseCellsAreNotNeighborIfApplicable(Cell(1,1), Cell(0,1)), (-1,0))

        # With Cells not Neighbor
        self.assertRaises(IndexError, Maze.raiseCellsAreNotNeighborIfApplicable, Cell(2,2), Cell(0,2))
        self.assertRaises(IndexError, Maze.raiseCellsAreNotNeighborIfApplicable, Cell(2,2), Cell(4,2))
        self.assertRaises(IndexError, Maze.raiseCellsAreNotNeighborIfApplicable, Cell(2,2), Cell(2,0))
        self.assertRaises(IndexError, Maze.raiseCellsAreNotNeighborIfApplicable, Cell(2,2), Cell(2,4))

        # With tuples Neighbor
        self.assertEqual(Maze.raiseCellsAreNotNeighborIfApplicable((1,1), (1,2)), (0,1))
        self.assertEqual(Maze.raiseCellsAreNotNeighborIfApplicable((1,1), (1,0)), (0,-1))
        self.assertEqual(Maze.raiseCellsAreNotNeighborIfApplicable((1,1), (2,1)), (1,0))
        self.assertEqual(Maze.raiseCellsAreNotNeighborIfApplicable((1,1), (0,1)), (-1,0))

        # With tuples not Neighbor
        self.assertRaises(IndexError, Maze.raiseCellsAreNotNeighborIfApplicable, (2,2), (0,2))
        self.assertRaises(IndexError, Maze.raiseCellsAreNotNeighborIfApplicable, (2,2), (4,2))
        self.assertRaises(IndexError, Maze.raiseCellsAreNotNeighborIfApplicable, (2,2), (2,0))
        self.assertRaises(IndexError, Maze.raiseCellsAreNotNeighborIfApplicable, (2,2), (2,4))


