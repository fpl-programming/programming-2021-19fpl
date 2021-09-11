"""
Programming for linguists

Tests for Rhombus class.
"""

import unittest
from shapes.rhombus import Rhombus

class RhombusTestCase(unittest.TestCase):
    """
    Creates a
    This Case of tests checks the functionality of the implementation of Parallelogram
    """
    def test_rhombus_get_uid(self):
        """
        Creates a rhombus.
        Tests that the correct uid is returned.
        """
        rhombus = Rhombus(0, 6, 90)
        self.assertEqual(rhombus.get_uid(), 0)

    def test_rhombus_get_area(self):
        """
        Creates a rhombus.
        Tests that the area is calculated correctly.
        """
        rhombus = Rhombus(0, 6, 90)
        self.assertEqual(rhombus.get_area(), 32.18387988962008)

    def test_get_giagonal(self):
        """
        Returns the diagonal length  of a rectangle
        :return int: the diagonal length of a rectangle
        """
        rhombus = Rhombus(0, 6, 90)
        self.assertEqual(rhombus.get_diagonal(), (6.303863865812756, 6.303863865812756))
