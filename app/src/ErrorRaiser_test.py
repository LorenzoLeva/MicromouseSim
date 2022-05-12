import unittest

from app.src.ErrorRaiser import ErrorRaiser
from app.src.Cell import Cell

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



