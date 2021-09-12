"""
Programming for linguists

Tests for Triangle class.
"""


import unittest
from shapes.triangle import Triangle


class TriangleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Triangle
    """
    def test_triangle_get_uid(self):
        """
        Creates a triangle.
        Tests that the correct uid is returned.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_uid(), 0)

    def test_triangle_get_area(self):
        """
        Creates a triangle.
        Tests that the area is calculated correctly.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_area(), 6)

    def test_triangle_get_perimeter(self):
        """
        Creates a triangle.
        Tests that the perimeter is calculated correctly.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_perimeter(), 15)

    def test_triangle_int_circle_rad(self):
        """
        Creates a triangle.
        Tests that the radius of internal circle of a triangle is calculated correctly.
        """
        triangle = Triangle(0, 4, 5, 6)
        self.assertEqual(triangle.get_int_circle_rad(), 0.8)



