"""
Tests for RegularTriangle class
"""

import unittest
from shapes.triangle import RegularTriangle


class RegularTriangleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of RegularTriangle
    """
    def test_triangle_get_uid(self):
        """
        Creates a triangle.
        Tests that the correct uid is returned.
        """
        triangle = RegularTriangle(0, 1)
        self.assertEqual(triangle.get_uid(), 0)

    def test_triangle_get_area(self):
        """
        Creates a regular triangle.
        Tests that the area is calculated correctly.
        """
        triangle = RegularTriangle(0, 2)
        self.assertEqual(triangle.get_area(), 1.7320508075688772)

    def test_triangle_get_perimeter(self):
        """
        Creates a regular triangle.
        Tests that the perimeter is calculated correctly.
        """
        triangle = RegularTriangle(0, 3)
        self.assertEqual(triangle.get_perimeter(), 9)

    def test_triangle_get_height(self):
        """
        Creates a regular triangle.
        Tests that the height is calculated correctly.
        """
        triangle = RegularTriangle(0, 4)
        self.assertEqual(triangle.get_height(), 3.4641016151377544)

    def test_triangle_get_circumscribed_radius(self):
        """
        Creates a regular triangle.
        Tests that the circumscribed radius is calculated correctly.
        """
        triangle = RegularTriangle(0, 5)
        self.assertEqual(triangle.get_circumscribed_radius(), 2.8867513459481287)

    def test_triangle_get_inscribed_radius(self):
        """
        Creates a regular triangle.
        Tests that the inscribed radius is calculated correctly.
        """
        triangle = RegularTriangle(0, 6)
        self.assertEqual(triangle.get_inscribed_radius(), 1.7320508075688774)
