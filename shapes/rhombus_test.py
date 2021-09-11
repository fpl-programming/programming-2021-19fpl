"""
Programming for linguists

Tests for Rhombus class.
"""

import unittest

from shapes.rhombus import Rhombus


class SquareTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Rhombus
    """
    def test_rhombus_get_uid(self):
        """
        Creates a rhombus.
        Tests that the correct uid is returned.
        """
        rhombus = Rhombus(0, 8, 4, 90)
        self.assertEqual(rhombus.get_uid(), 0)

    def test_rhombus_get_area(self):
        """
        Creates a rhombus.
        Tests that the area is calculated correctly.
        """
        rhombus = Rhombus(0, 8, 4, 90)
        self.assertEqual(rhombus.get_area(), 32)

    def test_rhombus_get_perimeter(self):
        """
        Creates a rhombus.
        Tests that the perimeter is calculated correctly.
        """
        rhombus = Rhombus(0, 8, 4, 90)
        self.assertEqual(rhombus.get_perimeter(), 32)

    def test_rhombus_get_diagonal(self):
        """
        Creates a rhombus.
        Tests that the diagonal is calculated correctly.
        """
        rhombus = Rhombus(0, 8, 4, 90)
        self.assertEqual(rhombus.get_diagonal(), (13.614456392545895, 8.405151821083676))
