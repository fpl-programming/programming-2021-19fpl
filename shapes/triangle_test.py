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
        triangle = Triangle(0, 9, 10, 11)
        self.assertEqual(triangle.get_uid(), 0)

    def test_triangle_get_area(self):
        """
        Creates a triangle.
        Tests that the area is calculated correctly.
        """
        triangle = Triangle(0, 9, 10, 11)
        self.assertEqual(triangle.get_area(), 42.42640687119285)

    def test_triangle_get_perimeter(self):
        """
        Creates a triangle.
        Tests that the perimeter is calculated correctly.
        """
        rectangle = Triangle(0, 9, 10, 11)
        self.assertEqual(rectangle.get_perimeter(), 30)

    def test_triangle_get_semiperimeter(self):
        """
        Creates a triangle.
        Tests that the semiperimeter is calculated correctly.
        """
        rectangle = Triangle(0, 9, 10, 11)
        self.assertEqual(rectangle.get_semiperimeter(), 15)

    def test_triangle_get_shortest_altitude(self):
        """
        Creates a triangle.
        Tests that the altitude to the longest side is calculated correctly.
        """
        rectangle = Triangle(0, 9, 10, 11)
        self.assertEqual(rectangle.get_shortest_altitude(), 7.713892158398701)

    def test_triangle_get_longest_altitude(self):
        """
        Creates a triangle.
        Tests that the altitude to the shortest side is calculated correctly.
        """
        rectangle = Triangle(0, 9, 10, 11)
        self.assertEqual(rectangle.get_longest_altitude(), 9.428090415820634)
