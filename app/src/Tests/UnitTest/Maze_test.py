import unittest
from unittest.mock import patch

from Cells.Cell import Cell
from Mazes.Maze import Maze

class TestMazeInitialization(unittest.TestCase):
    # TODO add tests for startCell and endCells
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
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

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
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

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
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
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.raiseCellsAreNotNeighborIfApplicable method raises TypeError when called with the wrong parameter type."""
        
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, 1, 1)
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, True, True)
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, ("1", "2"), ("2", "2"))

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
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

class TestIsCoordinateInEndArea(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.isCoordinateInEndArea method raises TypeError when called with the wrong parameter type."""
        
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, "1", "1")
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, True, True)
        self.assertRaises(TypeError, Maze.raiseCellsAreNotNeighborIfApplicable, ("1", "2"), ("2", "2"))

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.raiseCellsAreNotNeighborIfApplicable method passes correctly the tuple."""
        
        maze = Maze(6,6, None, (0,0), (2,2), (3,3))

        # Is in finish area
        self.assertEqual(maze.isCoordinateInEndArea(2,2), True)
        self.assertEqual(maze.isCoordinateInEndArea(2,3), True)
        self.assertEqual(maze.isCoordinateInEndArea(3,3), True)
        self.assertEqual(maze.isCoordinateInEndArea(3,2), True)

        # Is not in finish area
        self.assertEqual(maze.isCoordinateInEndArea(0,0), False)
        self.assertEqual(maze.isCoordinateInEndArea(0,5), False)
        self.assertEqual(maze.isCoordinateInEndArea(5,5), False)
        self.assertEqual(maze.isCoordinateInEndArea(5,0), False)

class TestGetMiddleCoordinate(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.getMiddleCoordinate method raises TypeError when called with the wrong parameter type."""
        
        self.assertRaises(IndexError, Maze.getMiddleCoordinate, -1)
        self.assertRaises(TypeError, Maze.getMiddleCoordinate, "1")
        self.assertRaises(TypeError, Maze.getMiddleCoordinate, True)

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.getMiddleCoordinate method returns correct values."""

        # Even
        self.assertEqual(Maze.getMiddleCoordinate(8), {'min': 3, 'max': 4})
        self.assertEqual(Maze.getMiddleCoordinate(16), {'min': 7, 'max': 8})
        self.assertEqual(Maze.getMiddleCoordinate(32), {'min': 15, 'max': 16})

        # Odd
        self.assertEqual(Maze.getMiddleCoordinate(7), {'min': 3, 'max': 3})
        self.assertEqual(Maze.getMiddleCoordinate(15), {'min': 7, 'max': 7})
        self.assertEqual(Maze.getMiddleCoordinate(31), {'min': 15, 'max': 15})

class TestDeleteWallsBetween(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.deleteWallsBetween method raises TypeError when called with the wrong parameter type."""

        maze = Maze(10,10)

        self.assertRaises(TypeError, maze.deleteWallsBetween, "1", "1")
        self.assertRaises(TypeError, maze.deleteWallsBetween, True, True)
        self.assertRaises(TypeError, maze.deleteWallsBetween, ("1", "2"), ("2", "2"))

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.deleteWallsBetween method deletes the correct walls."""

        maze = Maze(10,10)

        c1 = (0,0)
        c2 = (2,0)
        c3 = (0,2)
        c4 = (2,2)

        maze.deleteWallsBetween(c1, c1)

        self.assertEqual(maze.maze[c1[1]][c1[0]].walls, {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : True 
        })

        self.assertEqual(maze.maze[1][1].walls, {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : True 
        })

        maze.deleteWallsBetween(c1, c2)

        self.assertEqual(maze.maze[c1[1]][c1[0]].walls, {
            "top" : True,
            "right" : False,
            "bottom" : True,
            "left" : True 
        })

        self.assertEqual(maze.maze[1][1].walls, {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : True 
        })

        maze.deleteWallsBetween(c1, c3)

        self.assertEqual(maze.maze[c1[1]][c1[0]].walls, {
            "top" : False,
            "right" : False,
            "bottom" : True,
            "left" : True 
        })

        self.assertEqual(maze.maze[1][1].walls, {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : True 
        })

        maze.deleteWallsBetween(c1, c4)

        self.assertEqual(maze.maze[c1[1]][c1[0]].walls, {
            "top" : False,
            "right" : False,
            "bottom" : True,
            "left" : True 
        })

        self.assertEqual(maze.maze[1][1].walls, {
            "top" : False,
            "right" : False,
            "bottom" : False,
            "left" : False 
        })

class TestGetMinMaxCoordinatesOfCells(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.getMinMaxCoordinatesOfCells method raises TypeError when called with the wrong parameter type."""
        
        self.assertRaises(TypeError, Maze.getMinMaxCoordinatesOfCells, -1)
        self.assertRaises(TypeError, Maze.getMinMaxCoordinatesOfCells, (1,2))
        self.assertRaises(TypeError, Maze.getMinMaxCoordinatesOfCells, [1,2,3])
        self.assertRaises(TypeError, Maze.getMinMaxCoordinatesOfCells, [("1",2), (2,"1")])

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.getMinMaxCoordinatesOfCells method returns correct values."""

        self.assertEqual(Maze.getMinMaxCoordinatesOfCells([(2,1),(1,2)]), {'minX': 1, 'maxX': 2, 'minY': 1, 'maxY': 2})
        self.assertEqual(Maze.getMinMaxCoordinatesOfCells([(5,1),(1,2), (0,7)]), {'minX': 0, 'maxX': 5, 'minY': 1, 'maxY': 7})

class TestGetBorderCellsOfArea(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.getBorderCellsOfArea method raises TypeError when called with the wrong parameter type."""
        
        self.assertRaises(TypeError, Maze.getBorderCellsOfArea, -1, 2)
        self.assertRaises(TypeError, Maze.getBorderCellsOfArea, "-1", "2")

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.getBorderCellsOfArea method returns correct values."""

        self.assertEqual(Maze.getBorderCellsOfArea((2,1),(1,2)).sort(), [(1,1), (1,2), (2,2), (2,1)].sort())
        self.assertEqual(Maze.getBorderCellsOfArea((3,1),(1,3)).sort(), [(1,1), (1,2), (1,3), (2,3), (3,3), (3,2), (3,1), (2,1)].sort())

class TestGetBorderCellsOfArea(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.getRandomEndAreaBorderCell method returns correct values."""

        maze = Maze(16,16)
        borderCells = Maze.getBorderCellsOfArea(maze.endCell1, maze.endCell2)
        self.assertIn(maze.getRandomEndAreaBorderCell(), borderCells)

class TestGetNextSteps(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.getNextSteps method raises TypeError when called with the wrong parameter type."""
        
        maze = Maze(16,16)

        self.assertRaises(TypeError, maze.getNextSteps, ("a", "b"))
        self.assertRaises(TypeError, maze.getNextSteps, ("1", "2"))
        self.assertRaises(TypeError, maze.getNextSteps, "abc")

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.getNextSteps method returns correct values."""

        maze = Maze()

        maze.deleteWallsBetween((1,1), (2,1))
        self.assertEqual(maze.getNextSteps((1,1)).sort(), ["right"].sort())

        maze.deleteWallsBetween((1,1), (1,2))
        self.assertEqual(maze.getNextSteps((1,1)).sort(), ["right", "top"].sort())

        maze.deleteWallsBetween((1,1), (1,0))
        self.assertEqual(maze.getNextSteps((1,1)).sort(), ["right", "top", "bottom"].sort())

        maze.deleteWallsBetween((1,1), (0,1))
        self.assertEqual(maze.getNextSteps((1,1)).sort(), ["right", "top", "bottom", "left"].sort())

class TestGetStartPosition(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.getStartPosition method returns correct values."""

        startPosition = (0,0)
        maze = Maze(startCell=startPosition)

        self.assertEqual(maze.getStartPosition(), startPosition)

class TestIsEndPosition(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.isEndPosition method raises TypeError when called with the wrong parameter type."""
        
        maze = Maze()

        self.assertRaises(TypeError, maze.getNextSteps, ("a", "b"))
        self.assertRaises(TypeError, maze.getNextSteps, ("1", "2"))
        self.assertRaises(TypeError, maze.getNextSteps, "abc")

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.isEndPosition method returns correct values."""

        maze = Maze(endCell1=(1,1), endCell2=(2,2))

        self.assertEqual(maze.isEndPosition((1,1)), True)
        self.assertEqual(maze.isEndPosition((1,2)), True)
        self.assertEqual(maze.isEndPosition((2,2)), True)
        self.assertEqual(maze.isEndPosition((2,1)), True)

        self.assertEqual(maze.isEndPosition((0,0)), False)

class TestGetNeighborByKey(unittest.TestCase):
    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_invalid_input_types(self):
        """Test if the Maze.getNeighborByKey method raises TypeError when called with the wrong parameter type."""
        
        maze = Maze()


        self.assertRaises(TypeError, maze.getNeighborByKey, ("a", "b"), "top")

        self.assertRaises(KeyError, maze.getNeighborByKey, (1, 1), "Cat")

        self.assertRaises(IndexError, maze.getNeighborByKey, (0, 0), "bottom")

    @patch("Mazes.Maze.Maze.__abstractmethods__", set())
    def test_valid_input(self):
        """Test if the Maze.getNeighborByKey method returns correct values."""

        maze = Maze()

        self.assertEqual(maze.getNeighborByKey((1,1), "top"), (1, 2))
        self.assertEqual(maze.getNeighborByKey((1,1), "right"), (2, 1))
        self.assertEqual(maze.getNeighborByKey((1,1), "bottom"), (1, 0))
        self.assertEqual(maze.getNeighborByKey((1,1), "left"), (0, 1))




