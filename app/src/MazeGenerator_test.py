import unittest

from app.src.Cell import Cell
from app.src.MazeGenerator import MazeGenerator

class TestMazeGeneratorInitialization(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the MazeGenerator class raises TypeError when initialized with the wrong parameter type."""
        # No seed
        self.assertRaises(TypeError, MazeGenerator, "x", "y")
        self.assertRaises(TypeError, MazeGenerator, "3", "3")
        self.assertRaises(TypeError, MazeGenerator, 3, "y")
        self.assertRaises(TypeError, MazeGenerator, "x", 3)

        self.assertRaises(TypeError, MazeGenerator, True, True)
        self.assertRaises(TypeError, MazeGenerator, 3, True)
        self.assertRaises(TypeError, MazeGenerator, True, 3)

        # With seed
        # Strings
        self.assertRaises(TypeError, MazeGenerator, "x", "y", "seed")
        self.assertRaises(TypeError, MazeGenerator, "3", "3", "123")
        self.assertRaises(TypeError, MazeGenerator, 3, "y", 123)
        self.assertRaises(TypeError, MazeGenerator, "x", 3, 123)
        self.assertRaises(TypeError, MazeGenerator, 3, 3, "123")


        self.assertRaises(TypeError, MazeGenerator, True, True, False)
        self.assertRaises(TypeError, MazeGenerator, 3, True, True)
        self.assertRaises(TypeError, MazeGenerator, True, 3, True)


    def test_invalid_input_range(self):
        """Test if the MazeGenerator class raises IndexError when initialized with negative or zero size parameter type."""
        # Negative
        self.assertRaises(IndexError, MazeGenerator, 2, -2)
        self.assertRaises(IndexError, MazeGenerator, -2, 2)
        self.assertRaises(IndexError, MazeGenerator, -2, -2)

        # Zero
        self.assertRaises(IndexError, MazeGenerator, 2, 0)
        self.assertRaises(IndexError, MazeGenerator, 0, 2)
        self.assertRaises(IndexError, MazeGenerator, 0, 0)

    def test_initialization(self):
        """Test if the MazeGenerator class initializes correctly an object with all its properties correctly."""
        columns = 3
        rows = 4
        seed = 123

        maze = MazeGenerator(columns, rows, seed)

        self.assertEqual(maze.x, columns)
        self.assertEqual(maze.y, rows)
        self.assertEqual(maze.seed, seed)

        self.assertEqual(len(maze.visited), rows)
        self.assertEqual(len(maze.visited[0]), columns)
        self.assertEqual(type(maze.visited[0][0]), bool)

        self.assertEqual(len(maze.maze), rows)
        self.assertEqual(len(maze.maze[0]), columns)
        self.assertEqual(type(maze.maze[0][0]), Cell)

class TestMazeGeneratorRaiseCellsAreNotNeighborIfApplicable(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the MazeGenerator.raiseCellsAreNotNeighborIfApplicable method raises TypeError when called with the wrong parameter type."""
        
        self.assertRaises(TypeError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, 1, 1)
        self.assertRaises(TypeError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, True, True)
        self.assertRaises(TypeError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, ("1", "2"), ("2", "2"))

    def test_valid_input(self):
        """Test if the MazeGenerator.raiseCellsAreNotNeighborIfApplicable method passes correctly the tuple."""
        # With Cells Neighbor
        self.assertEqual(MazeGenerator.raiseCellsAreNotNeighborIfApplicable(Cell(1,1), Cell(1,2)), (0,1))
        self.assertEqual(MazeGenerator.raiseCellsAreNotNeighborIfApplicable(Cell(1,1), Cell(1,0)), (0,-1))
        self.assertEqual(MazeGenerator.raiseCellsAreNotNeighborIfApplicable(Cell(1,1), Cell(2,1)), (1,0))
        self.assertEqual(MazeGenerator.raiseCellsAreNotNeighborIfApplicable(Cell(1,1), Cell(0,1)), (-1,0))

        # With Cells not Neighbor
        self.assertRaises(IndexError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, Cell(2,2), Cell(0,2))
        self.assertRaises(IndexError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, Cell(2,2), Cell(4,2))
        self.assertRaises(IndexError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, Cell(2,2), Cell(2,0))
        self.assertRaises(IndexError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, Cell(2,2), Cell(2,4))

        # With tuples Neighbor
        self.assertEqual(MazeGenerator.raiseCellsAreNotNeighborIfApplicable((1,1), (1,2)), (0,1))
        self.assertEqual(MazeGenerator.raiseCellsAreNotNeighborIfApplicable((1,1), (1,0)), (0,-1))
        self.assertEqual(MazeGenerator.raiseCellsAreNotNeighborIfApplicable((1,1), (2,1)), (1,0))
        self.assertEqual(MazeGenerator.raiseCellsAreNotNeighborIfApplicable((1,1), (0,1)), (-1,0))

        # With tuples not Neighbor
        self.assertRaises(IndexError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, (2,2), (0,2))
        self.assertRaises(IndexError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, (2,2), (4,2))
        self.assertRaises(IndexError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, (2,2), (2,0))
        self.assertRaises(IndexError, MazeGenerator.raiseCellsAreNotNeighborIfApplicable, (2,2), (2,4))



