"""
Programming for linguists

Tests for Square class.
"""

import unittest

from shapes.square import Square


class SquareTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Square
    """
    def test_square_get_uid(self):
        """
        Creates a square.
        Tests that the correct uid is returned.
        """
        square = Square(0, 5)
        self.assertEqual(square.get_uid(), 0)

    def test_square_get_area(self):
        """
        Creates a square.
        Tests that the area is calculated correctly.
        """
        square = Square(0, 5)
        self.assertEqual(square.get_area(), 25)

    def test_square_get_perimeter(self):
        """
        Creates a square.
        Tests that the perimeter is calculated correctly.
        """
        square = Square(0, 5)
        self.assertEqual(square.get_perimeter(), 20)

    def test_square_get_diagonal(self):
        """
        Creates a square.
        Tests that the diagonal is calculated correctly.
        """
        square = Square(0, 5)
        self.assertEqual(square.get_diagonal(), 7.0710678118654755)
