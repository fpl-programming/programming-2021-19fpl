"""
Programming for linguists

Tests for Rhombus class.
"""

import unittest
from shapes.rhombus import Rhombus


class RhombusTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Rhombus
    """
    def test_rhombus_get_uid(self):
        """
        Creates a rhombus.
        Tests that the correct uid is returned.
        """
        rhombus = Rhombus(0, 5, 0.5)
        self.assertEqual(rhombus.get_uid(), 0)

    def test_rectangle_get_area(self):
        """
        Creates a rhombus.
        Tests that the area is calculated correctly.
        """
        rhombus = Rhombus(0, 6, 0.5)
        self.assertEqual(rhombus.get_area(), 18)

    def test_rectangle_get_perimeter(self):
        """
        Creates a rhombus.
        Tests that the perimeter is calculated correctly.
        """
        rhombus = Rhombus(0, 6, 0.5)
        self.assertEqual(rhombus.get_perimeter(), 24)

    def test_rectangle_get_height(self):
        """
        Creates a rhombus.
        Tests that the height is calculated correctly.
        """
        rhombus = Rhombus(0, 6, 0.5)
        self.assertEqual(rhombus.get_height(), 3)
