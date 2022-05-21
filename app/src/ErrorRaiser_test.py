import unittest

from ErrorRaiser import ErrorRaiser
from Cell import Cell

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


class TestErrorRaiserRaiseIsNotListOfStr(unittest.TestCase):
    def test_invalid_input_types(self):
        """Test if the ErrorRaiser.raiseIsNotListOfStr method raises TypeError when called with the wrong parameter type."""

        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotListOfStr, "ABC")
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotListOfStr, ("A", "B"))
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotListOfStr, [1,2])
        self.assertRaises(TypeError, ErrorRaiser.raiseIsNotListOfStr, ["a", "b", 2])

    def test_valid_input(self):
        """Test if the ErrorRaiser.raiseIsNotListOfStr method passes the list through correctly."""
        self.assertEqual(ErrorRaiser.raiseIsNotListOfStr(["a"]), ["a"])
        self.assertEqual(ErrorRaiser.raiseIsNotListOfStr(["a", "B"]), ["a", "B"])

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


