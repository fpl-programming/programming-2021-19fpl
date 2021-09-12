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

    def test_triangle_get_height(self):
        """
        Creates a triangle.
        Tests that the height is calculated correctly.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_height(), 4)

    def test_triangle_get_perimeter(self):
        """
        Creates a triangle.
        Tests that the perimeter is calculated correctly.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_perimeter(), 12)

    def test_triangle_get_semi_perimeter(self):
        """
        Creates a triangle.
        Tests that the semi perimeter is calculated correctly.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_semi_perimeter(), 6)

    def test_triangle_get_area(self):
        """
        Creates a triangle.
        Tests that the area is calculated correctly.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_area(), 6)

    def test_triangle_get_inscribed_circle_radius(self):
        """
        Creates a triangle.
        Tests that the inscribed circle radius is calculated correctly.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_inscribed_circle_radius(), 1)

    def test_triangle_get_circumscribed_circle_radius(self):
        """
        Creates a triangle.
        Tests that the circumscribed circle radius is calculated correctly.
        """
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_circumscribed_circle_radius(), 90)
