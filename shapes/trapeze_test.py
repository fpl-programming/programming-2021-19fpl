"""
Programming for linguists

Tests for Trapeze class.
"""

import unittest

from shapes.trapeze import Trapeze


class SquareTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Trapeze
    """
    def test_trapeze_get_uid(self):
        """
        Creates a trapeze.
        Tests that the correct uid is returned.
        """
        trapeze = Trapeze(4, (10, 9), (10, 20))
        self.assertEqual(trapeze.get_uid(), 4)

    def test_trapeze_get_area(self):
        """
        Creates a trapeze.
        Tests that the area is calculated correctly.
        """
        trapeze = Trapeze(4, (10, 9), (10, 20))
        self.assertEqual(trapeze.get_area(), 120.55885492156933)

    def test_trapeze_get_perimeter(self):
        """
        Creates a trapeze.
        Tests that the perimeter is calculated correctly.
        """
        trapeze = Trapeze(4, (10, 9), (10, 20))
        self.assertEqual(trapeze.get_perimeter(), 49)

    def test_trapeze_mean_line(self):
        """
        Creates a trapeze.
        Tests that the mean line is calculated correctly.
        """
        trapeze = Trapeze(4, (10, 9), (10, 20))
        self.assertEqual(trapeze.get_mean_line(), 15.0)

    def test_trapeze_mean_line(self):
        """
        Creates a trapeze.
        Tests that the angles of the base is calculated correctly.
        """
        trapeze = Trapeze(4, (10, 9), (10, 20))
        self.assertEqual(trapeze.get_angles_of_base(), (53.48736790080603, 63.256316049597004))
