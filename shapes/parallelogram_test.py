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
        parallelogram = Parallelogram(0, 4, 7, 60)
        self.assertEqual(parallelogram.get_uid(), 0)

    def test_parallelogram_get_area(self):
        """
        Creates a parallelogram.
        Tests that the area is calculated correctly.
        """
        parallelogram = Parallelogram(0, 4, 5, 60)
        self.assertEqual(parallelogram.get_area(), 17.32050807568877)

    def test_parallelogram_get_perimeter(self):
        """
        Creates a parallelogram.
        Tests that the perimeter is calculated correctly.
        """
        parallelogram = Parallelogram(0, 4, 5, 30)
        self.assertEqual(parallelogram.get_perimeter(), 18)

    def test_parallelogram_get_diagonal(self):
        """
        Creates a parallelogram.
        Tests that the diagonal is calculated correctly.
        """
        parallelogram = Parallelogram(0, 4, 5, 30)
        self.assertEqual(parallelogram.get_diagonal(), 8.697184380670421)
