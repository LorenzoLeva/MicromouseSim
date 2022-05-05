import unittest
from .Cell import Cell


class TestCellInitialization(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the Cell class raises TypeError when initialized with the wrong parameter type."""
        self.assertRaises(TypeError, Cell, "x", "y")
        self.assertRaises(TypeError, Cell, 0, "y")
        self.assertRaises(TypeError, Cell, "x", 0)
        self.assertRaises(TypeError, Cell, True, True)
    
    def test_initialization(self):
        """Test if the Cell class initializes correctly an object with all its properties correctly."""
        x = 3
        y = 4

        cell = Cell(x, y)

        self.assertEqual(cell.x, x)
        self.assertEqual(cell.y, y)
        self.assertEqual(cell.walls, {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : True 
        })
