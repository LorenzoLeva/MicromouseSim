import unittest
from .Cell import Cell


class TestCellInitialization(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the Cell class raises TypeError when initialized with the wrong parameter type."""
        self.assertRaises(TypeError, Cell, "x", "y")
        self.assertRaises(TypeError, Cell, "3", "3")
        self.assertRaises(TypeError, Cell, 0, "y")
        self.assertRaises(TypeError, Cell, "x", 0)
        self.assertRaises(TypeError, Cell, True, True)
    
    def test_invalid_input_range(self):
        """Test if the Cell class raises IndexError when initialized with negative coordinates parameter type."""
        self.assertRaises(IndexError, Cell, 0, -2)
        self.assertRaises(IndexError, Cell, -2, 0)
        self.assertRaises(IndexError, Cell, -2, -2)
    
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

class TestCellDeleteWallMethod(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the Cell.deleteWall method raises TypeError when called with the wrong parameter type."""
        cell = Cell(0,0)
        
        self.assertRaises(TypeError, cell.deleteWall, 1)
        self.assertRaises(TypeError, cell.deleteWall, (0,0))
        self.assertRaises(TypeError, cell.deleteWall, True)

    def test_invalid_input_keys(self):
        """Test if the Cell.deleteWall method raises KeyError when called with the wrong parameter key."""
        cell = Cell(0,0)
        
        self.assertRaises(KeyError, cell.deleteWall, "North")
        self.assertRaises(KeyError, cell.deleteWall, "2")
        self.assertRaises(KeyError, cell.deleteWall, "Hello")

    def test_valid_input(self):
        """Test if the Cell.deleteWall method deletes correctly the walls."""
        cell = Cell(0,0)
        
        cell.deleteWall("Top")
        self.assertEqual(cell.walls, {
            "top" : False,
            "right" : True,
            "bottom" : True,
            "left" : True 
        })

        cell.deleteWall("right")
        self.assertEqual(cell.walls, {
            "top" : False,
            "right" : False,
            "bottom" : True,
            "left" : True 
        })

        cell.deleteWall("bOTTom")
        self.assertEqual(cell.walls, {
            "top" : False,
            "right" : False,
            "bottom" : False,
            "left" : True 
        })

        cell.deleteWall("left")
        self.assertEqual(cell.walls, {
            "top" : False,
            "right" : False,
            "bottom" : False,
            "left" : False 
        })

class TestCellBuildWallMethod(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the Cell.buildWall method raises TypeError when called with the wrong parameter type."""
        cell = Cell(0,0)
        
        self.assertRaises(TypeError, cell.buildWall, 1)
        self.assertRaises(TypeError, cell.buildWall, (0,0))
        self.assertRaises(TypeError, cell.buildWall, True)

    def test_invalid_input_keys(self):
        """Test if the Cell.buildWall method raises KeyError when called with the wrong parameter key."""
        cell = Cell(0,0)
        
        self.assertRaises(KeyError, cell.buildWall, "North")
        self.assertRaises(KeyError, cell.buildWall, "2")
        self.assertRaises(KeyError, cell.buildWall, "Hello")

    def test_valid_input(self):
        """Test if the Cell.buildWall method builds correctly the walls."""
        cell = Cell(0,0)

        cell.walls = {
            "top" : False,
            "right" : False,
            "bottom" : False,
            "left" : False 
        }
        
        cell.buildWall("Top")
        self.assertEqual(cell.walls, {
            "top" : True,
            "right" : False,
            "bottom" : False,
            "left" : False 
        })

        cell.buildWall("right")
        self.assertEqual(cell.walls, {
            "top" : True,
            "right" : True,
            "bottom" : False,
            "left" : False 
        })

        cell.buildWall("bOTTom")
        self.assertEqual(cell.walls, {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : False 
        })

        cell.buildWall("left")
        self.assertEqual(cell.walls, {
            "top" : True,
            "right" : True,
            "bottom" : True,
            "left" : True 
        })

class TestCellRaiseIsNotCellIfApplicableMethod(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the Cell.raiseIsNotCellIfApplicable method raises TypeError when called with the wrong parameter type."""
        self.assertRaises(TypeError, Cell.raiseIsNotCellIfApplicable, 2)
        self.assertRaises(TypeError, Cell.raiseIsNotCellIfApplicable, "A")
        self.assertRaises(TypeError, Cell.raiseIsNotCellIfApplicable, True)
        self.assertRaises(TypeError, Cell.raiseIsNotCellIfApplicable, ("A","B"))
        self.assertRaises(TypeError, Cell.raiseIsNotCellIfApplicable, [1, 2])
        self.assertRaises(TypeError, Cell.raiseIsNotCellIfApplicable, (1, 2, 3))
        self.assertRaises(TypeError, Cell.raiseIsNotCellIfApplicable, ("A","B","C"))

    def test_valid_input(self):
        """Test if the Cell.raiseIsNotCellIfApplicable method passes the value if of right type."""
        cell = Cell(1,2)
        tup = (1,2)
        self.assertEqual(Cell.raiseIsNotCellIfApplicable(cell), tup)
        self.assertEqual(Cell.raiseIsNotCellIfApplicable(tup), tup)

class TestCellMinusMethod(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the Cell.minus method raises TypeError when called with the wrong parameter type."""
        c1 = Cell(1,2)

        self.assertRaises(TypeError, c1.minus, 2)
        self.assertRaises(TypeError, c1.minus, "A")
        self.assertRaises(TypeError, c1.minus, True)
        self.assertRaises(TypeError, c1.minus, ("A","B"))
        self.assertRaises(TypeError, c1.minus, [1, 2])
        self.assertRaises(TypeError, c1.minus, (1, 2, 3))
        self.assertRaises(TypeError, c1.minus, ("A","B","C"))
        
    def test_valid_input(self):
        """Test if the Cell.minus method returns the correct vector."""
        c1 = Cell(1,2)
        c2 = Cell(3,4)

        self.assertEqual(c1.minus(c2), (-2, -2))
        self.assertEqual(c2.minus(c1), (2, 2))
