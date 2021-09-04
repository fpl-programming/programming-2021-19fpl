"""
Programming for linguists

Tests for Circle class.
"""

import unittest
from shapes.circle import Circle


class CircleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Circle
    """
    def test_circle_get_uid(self):
        """
        Creates a circle.
        Tests that the correct uid is returned.
        """
        circle = Circle(0, 5)
        self.assertEqual(circle.get_uid(), 0)

    def test_circle_get_area(self):
        """
        Creates a circle.
        Tests that the area is calculated correctly.
        """
        circle = Circle(0, 3)
        self.assertEqual(circle.get_area(), 28.274333882308138)

    def test_circle_get_perimeter(self):
        """
        Creates a circle.
        Tests that the perimeter is calculated correctly.
        """
        circle = Circle(0, 2)
        self.assertEqual(circle.get_perimeter(), 12.566370614359172)

    def test_circle_get_diameter(self):
        """
        Creates a circle.
        Tests that the diameter is calculated correctly.
        """
        circle = Circle(0, 2)
        self.assertEqual(circle.get_diameter(), 4)
