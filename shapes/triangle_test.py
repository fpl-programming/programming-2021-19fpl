"""
Programming for linguists

Tests for Triangle class.
"""

import unittest
from shapes.triangle import RightTriangle


class TriangleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of right triangle
    """

    def test_triangle_get_area(self):
        """
        Creates a triangle.
        Tests that the area is calculated correctly.
        """
        triangle = RightTriangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_area(), 6)

    def test_triangle_get_perimeter(self):
        """
        Creates a triangle.
        Tests that the perimeter is calculated correctly.
        """
        triangle = RightTriangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_perimeter(), 12)

    def test_triangle_get_diagonal(self):
        """
        Creates a triangle.
        Tests that the diagonal is calculated correctly.
        """
        triangle = RightTriangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_diagonal(), 5)
