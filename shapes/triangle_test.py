"""
Programming for linguists

Tests for Rectangle class.
"""

import unittest
from shapes.triangle import Triangle


class TriangleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Rectangle
    """
    def test_triangle_get_uid(self):
        """
        Creates a rectangle.
        Tests that the correct uid is returned.
        """
        triangle = Triangle(0, 5, 6, 5)
        self.assertEqual(triangle.get_uid(), 0)

    def test_triangle_get_area(self):
        """
        Creates a rectangle.
        Tests that the area is calculated correctly.
        """
        triangle = Triangle(0, 5, 6, 5)
        self.assertEqual(triangle.get_area(), 12)

    def test_triangle_get_perimeter(self):
        """
        Creates a rectangle.
        Tests that the perimeter is calculated correctly.
        """
        triangle = Triangle(0, 5, 6, 5)
        self.assertEqual(triangle.get_perimeter(), 16)

    def test_triangle_get_height(self):
        """
        Creates a rectangle.
        Tests that the diagonal is calculated correctly.
        """
        triangle = Triangle(0, 5, 6, 5)
        self.assertEqual(triangle.get_height(), 4.8)
