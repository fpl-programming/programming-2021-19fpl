"""
Programming for linguists

Tests for Diamond class.
"""

import unittest
from shapes.diamond import Diamond


class RectangleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Rectangle
    """
    def test_diamond_get_uid(self):
        """
        Creates a rectangle.
        Tests that the correct uid is returned.
        """
        diamond = Diamond(0, 16, 12)
        self.assertEqual(diamond.get_uid(), 0)

    def test_diamond_get_area(self):
        """
        Creates a rectangle.
        Tests that the area is calculated correctly.
        """
        diamond = Diamond(0, 16, 12)
        self.assertEqual(diamond.get_area(), 96)

    def test_diamond_get_perimeter(self):
        """
        Creates a rectangle.
        Tests that the perimeter is calculated correctly.
        """
        diamond = Diamond(0, 16, 12)
        self.assertEqual(diamond.get_perimeter(), 40)

    def test_diamond_get_side(self):
        """
        Creates a rectangle.
        Tests that the diagonal is calculated correctly.
        """
        diamond = Diamond(0, 16, 12)
        self.assertEqual(diamond.get_side(), 10)
