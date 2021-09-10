"""
Programming for linguists
Tests for RightTrapeze class.
"""

import unittest
from shapes.trapeze import RightTrapeze


class RightTrapezeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of RightTrapeze
    """
    def test_trapeze_get_uid(self):
        """
        Creates a trapeze.
        Tests that the correct uid is returned.
        """
        trapeze = RightTrapeze(0, 1, 4, 3)
        self.assertEqual(trapeze.get_uid(), 0)

    def test_trapeze_get_area(self):
        """
        Creates a trapeze.
        Tests that the area is calculated correctly.
        """
        trapeze = RightTrapeze(0, 1, 4, 3)
        self.assertEqual(trapeze.get_area(), 6.49519052838329)

    def test_trapeze_get_perimeter(self):
        """
        Creates a trapeze.
        Tests that the perimeter is calculated correctly.
        """
        trapeze = RightTrapeze(0, 1, 4, 3)
        self.assertEqual(trapeze.get_perimeter(), 11)
