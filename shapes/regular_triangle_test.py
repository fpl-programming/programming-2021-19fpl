"""
Programming for linguists

Tests for RegularTriangle class.
"""

import unittest

from shapes.regular_triangle import RegularTriangle


class RegularTriangleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of RegularTriangle
    """
    def test_regular_triangle_get_uid(self):
        """
        Creates a regular triangle.
        Tests that the correct uid is returned.
        """
        regular_triangle = RegularTriangle(0, 5)
        self.assertEqual(regular_triangle.get_uid(), 0)

    def test_regular_triangle_get_area(self):
        """
        Creates a regular triangle.
        Tests that the area is calculated correctly.
        """
        regular_triangle = RegularTriangle(0, 5)
        self.assertEqual(regular_triangle.get_area(), 10.825317547305483)

    def test_regular_triangle_get_perimeter(self):
        """
        Creates a regular triangle.
        Tests that the perimeter is calculated correctly.
        """
        regular_triangle = RegularTriangle(0, 5)
        self.assertEqual(regular_triangle.get_perimeter(), 15)

    def test_regular_triangle_get_diagonal(self):
        """
        Creates a regular triangle.
        Tests that the height is calculated correctly.
        """
        regular_triangle = RegularTriangle(0, 5)
        self.assertEqual(regular_triangle.get_height(), 4.330127018922193)
