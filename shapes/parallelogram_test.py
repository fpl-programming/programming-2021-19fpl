"""
Programming for linguists

Tests for Parallelogram class.
"""

import unittest
from shapes.parallelogram import Parallelogram


class ParallelogramTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Parallelogram
    """
    def test_parallelogram_get_uid(self):
        """
        Creates a parallelogram.
        Tests that the correct uid is returned.
        """
        parallelogram = Parallelogram(0, 2, 8, 4)
        self.assertEqual(parallelogram.get_uid(), 0)

    def test_parallelogram_get_area(self):
        """
        Creates a parallelogram.
        Tests that the area is calculated correctly.
        """
        parallelogram = Parallelogram(0, 2, 8, 4)
        self.assertEqual(parallelogram.get_area(), 32)

    def test_parallelogram_get_perimeter(self):
        """
        Creates a parallelogram.
        Tests that the perimeter is calculated correctly.
        """
        parallelogram = Parallelogram(0, 2, 8, 4)
        self.assertEqual(parallelogram.get_perimeter(), 20)
