"""
Programming for linguists

Tests for Hexagon class.
"""

import unittest
from shapes.hexagon import Hexagon


class HexagonTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Hexagon
    """
    def test_hexagon_get_uid(self):
        """
        Creates a hexagon.
        Tests that the correct uid is returned.
        """
        hexagon = Hexagon(0, 10)
        self.assertEqual(hexagon.get_uid(), 0)

    def test_hexagon_get_area(self):
        """
        Creates a hexagon.
        Tests that the area is calculated correctly.
        """
        hexagon = Hexagon(0, 10)
        self.assertEqual(hexagon.get_area(), 259.8076211353316)

    def test_hexagon_get_perimeter(self):
        """
        Creates a hexagon.
        Tests that the perimeter is calculated correctly.
        """
        hexagon = Hexagon(0, 10)
        self.assertEqual(hexagon.get_perimeter(), 60)

    def test_hexagon_get_main_diagonal(self):
        """
        Creates a hexagon.
        Tests that the main diagonal is calculated correctly.
        """
        hexagon = Hexagon(0, 10)
        self.assertEqual(hexagon.get_main_diagonal(), 20)

    def test_hexagon_get_small_diagonal(self):
        """
        Creates a hexagon.
        Tests that the small diagonal is calculated correctly.
        """
        hexagon = Hexagon(0, 10)
        self.assertEqual(hexagon.get_small_diagonal(), 17.32050807568877)
