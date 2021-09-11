"""
Programming for linguists

Tests for Rhombus class.
"""

import unittest
from shapes.rhombus import Rhombus

class RhombusTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Rectangle
    """
    def test_rectangle_get_uid(self):
        """
        Creates a rhombus.
        Tests that the correct uid is returned.
        """
        rhombus = Rhombus(0, 5, 60)
        self.assertEqual(rhombus.get_uid(), 0)

    def test_rectangle_get_area(self):
        """
        Creates a rhombus.
        Tests that the area is calculated correctly.
        """
        rhombus = Rhombus(0, 5, 60)
        self.assertEqual(rhombus.get_area(), 41.8258151868904)

    def test_rectangle_get_perimeter(self):
        """
        Creates a rhombus.
        Tests that the perimeter is calculated correctly.
        """
        rhombus = Rhombus(0, 5, 60)
        self.assertEqual(rhombus.get_perimeter(), 20)

    def test_rectangle_get_diagonal(self):
        """
        Creates a rhombus.
        Tests that the diagonal is calculated correctly.
        """
        rectangle = Rhombus(0, 5,  60)
        self.assertEqual(rectangle.get_diagonal(), (9.659258262890683, 8.660254037844387))