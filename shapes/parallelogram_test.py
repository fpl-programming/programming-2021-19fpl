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
    def test_rectangle_get_uid(self):
        """
        Creates a parallelogram.
        Tests that the correct uid is returned.
        """
        parallelogram = Parallelogram(0, 3, 4, 60)
        self.assertEqual(parallelogram.get_uid(), 0)

    def test_rectangle_get_area(self):
        """
        Creates a parallelogram.
        Tests that the area is calculated correctly.
        """
        parallelogram = Parallelogram(0, 3, 4, 60)
        self.assertEqual(parallelogram.get_area(), 10.392304845413264)

    def test_rectangle_get_perimeter(self):
        """
        Creates a parallelogram.
        Tests that the perimeter is calculated correctly.
        """
        parallelogram = Parallelogram(0, 3, 4, 60)
        self.assertEqual(parallelogram.get_perimeter(), 14)

    def test_rectangle_get_diagonal_short(self):
        """
        Creates a parallelogram.
        Tests that the short diagonal is calculated correctly.
        """
        parallelogram = Parallelogram(0, 3, 4, 60)
        self.assertEqual(parallelogram.get_diagonal(short=True), 3.6055512754639887)

    def test_rectangle_get_diagonal_long(self):
        """
        Creates a parallelogram.
        Tests that the long diagonal is calculated correctly.
        """
        parallelogram = Parallelogram(0, 3, 4, 60)
        self.assertEqual(parallelogram.get_diagonal(short=False), 6.082762530298219)
