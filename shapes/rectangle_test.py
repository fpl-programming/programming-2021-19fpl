"""
Programming for linguists

Tests for Rectangle class.
"""

import unittest
from shapes.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Rectangle
    """
    def test_rectangle_get_uid(self):
        """
        Creates a rectangle.
        Tests that the correct uid is returned.
        """
        rectangle = Rectangle(0, 5, 6)
        self.assertEqual(rectangle.get_uid(), 0)

    def test_rectangle_get_area(self):
        """
        Creates a rectangle.
        Tests that the area is calculated correctly.
        """
        rectangle = Rectangle(0, 5, 6)
        self.assertEqual(rectangle.get_area(), 30)

    def test_rectangle_get_perimeter(self):
        """
        Creates a rectangle.
        Tests that the perimeter is calculated correctly.
        """
        rectangle = Rectangle(0, 5, 6)
        self.assertEqual(rectangle.get_perimeter(), 22)

    def test_rectangle_get_diagonal(self):
        """
        Creates a rectangle.
        Tests that the diagonal is calculated correctly.
        """
        rectangle = Rectangle(0, 3, 4)
        self.assertEqual(rectangle.get_diagonal(), 5)
