import unittest

from Tools.ErrorRaiser import ErrorRaiser
from Cells.Cell import Cell

class TestErrorRaiserRaiseIsNotTuple(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the ErrorRaiser.raiseIsNotTuple method raises TypeError when called with the wrong parameter type."""

        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotTuple, "ABC")
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotTuple, ("A", "B"))
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotTuple, ("1","2"))
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotTuple, Cell(0,0))

    def test_valid_input(self):
        """Test if the ErrorRaiser.raiseIsNotTuple method passes the tuple through correctly."""
        self.assertEqual(ErrorRaiser.raiseIsNotTuple((1,1)), (1,1))
        self.assertEqual(ErrorRaiser.raiseIsNotTuple((0,0)), (0,0))
        self.assertEqual(ErrorRaiser.raiseIsNotTuple((1,-1)), (1,-1))
        self.assertEqual(ErrorRaiser.raiseIsNotTuple((-1,-1)), (-1,-1))

class TestErrorRaiserRaiseIsNotType(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the ErrorRaiser.raiseIsNotType method raises TypeError when called with the wrong parameter type."""

        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotType, int, "ABC")
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotType, str, 1)
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotType, bool, "ABC")



    def test_valid_input(self):
        """Test if the ErrorRaiser.raiseIsNotType method passes the tuple through correctly."""
        self.assertEqual(ErrorRaiser.raiseIsNotType(tuple, (1,1)), (1,1))
        self.assertEqual(ErrorRaiser.raiseIsNotType(int, 2), 2)
        self.assertEqual(ErrorRaiser.raiseIsNotType(bool, False), False)
        cell = Cell(1,1)
        self.assertEqual(ErrorRaiser.raiseIsNotType(Cell, cell), cell)



class TestErrorRaiserRaiseNotValidKey(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the ErrorRaiser.raiseNotValidKey method raises TypeError when called with the wrong parameter type."""

        # Wrong key type
        self.assertRaises(TypeError, ErrorRaiser.raiseNotValidKey, 1, ["a", "b"])
        self.assertRaises(TypeError, ErrorRaiser.raiseNotValidKey, True, ["a", "b"])

        # Wrong possibleKeys type
        self.assertRaises(TypeError, ErrorRaiser.raiseNotValidKey, "a", ["a", 1])
        self.assertRaises(TypeError, ErrorRaiser.raiseNotValidKey, "a", ["a", True])
    
    def test_valid_input(self):
        """Test if the ErrorRaiser.raiseNotValidKey method passes the key through correctly if its in the list."""
        self.assertEqual(ErrorRaiser.raiseNotValidKey("a", ["a", "b"]), "a")
        self.assertEqual(ErrorRaiser.raiseNotValidKey("B", ["a", "B"]), "B")

class TestErrorRaiserRaiseIsNotListOfType(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the ErrorRaiser.raiseIsNotListOfType method raises TypeError when called with the wrong parameter type."""

        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotListOfType, str, "ABC")
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotListOfType, str, ("A", "B"))
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotListOfType, str, [1,2])
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotListOfType, str, ["a", "b", 2])

    def test_valid_input(self):
        """Test if the ErrorRaiser.raiseIsNotListOfType method passes the list through correctly."""
        self.assertEqual(ErrorRaiser.raiseIsNotListOfType(str, ["a"]), ["a"])
        self.assertEqual(ErrorRaiser.raiseIsNotListOfType(str, ["a", "B"]), ["a", "B"])
        self.assertEqual(ErrorRaiser.raiseIsNotListOfType(int, [1]), [1])
        self.assertEqual(ErrorRaiser.raiseIsNotListOfType(int, [2, 1]), [2, 1])
