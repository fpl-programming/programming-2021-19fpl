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

    def test_id(self):
        """
        Creates a Rhombus.
        Tests that the correct uid is returned.
        """
        rhombus = Rhombus(228, 10, 10)
        self.assertEqual(rhombus.get_uid(), 228)

    def test_square_area(self):
        """
        Creates a Rhombus with equal diagonals(Square).
        Tests that the area is calculated correctly.
        """
        rhombus = Rhombus(0, 5, 5)
        self.assertEqual(rhombus.get_area(), 12.5)

    def test_area(self):
        """
        Creates a Rhombus.
        Tests that the area is calculated correctly.
        """
        rhombus = Rhombus(0, 5, 3)
        self.assertEqual(rhombus.get_area(), 7.5)

    def test_perimeter(self):
        """
        Creates a Rhombus.
        Tests that the perimeter is calculated correctly.
        """
        rhombus = Rhombus(0, 6, 8)
        self.assertEqual(rhombus.get_perimeter(), 20)

    def test_height(self):
        """
        Creates a Rhombus.
        Tests that the height is calculated correctly.
        """
        rhombus = Rhombus(0, 6, 8)
        self.assertEqual(rhombus.get_height(), 4.8)

    def test_square_perimeter(self):
        """
        Creates a Rhombus with equal diagonals(Square).
        Tests that the perimeter is calculated correctly.
        """

        rhombus = Rhombus(0, 10, 10)
        self.assertLess(abs(rhombus.get_perimeter() - 28.28), 0.1)

    def test_uid_bad_input(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(TypeError):
            rhombus = Rhombus('j', 8, 8)
            print(rhombus.get_height())

    def test_diagonal1_bad_input(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(TypeError):
            rhombus = Rhombus(1, 'gg', 8)
            print(rhombus.get_height())

    def test_diagonal2_bad_input(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(TypeError):
            rhombus = Rhombus(4, 8, 'gg')
            print(rhombus.get_height())

    def test_all_bad_input(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(TypeError):
            rhombus = Rhombus('r', 'i', 'p')
            print(rhombus.get_height())

    def test_uid_bad_value(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(ValueError):
            rhombus = Rhombus(-1, 8, 8)
            print(rhombus.get_height())

    def test_diagonal1_bad_value(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(ValueError):
            rhombus = Rhombus(1, -1, 8)
            print(rhombus.get_height())

    def test_diagonal2_bad_value(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(ValueError):
            rhombus = Rhombus(4, 8, -1)
            print(rhombus.get_height())

    def test_all_bad_value(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(ValueError):
            rhombus = Rhombus(-1, -1, -1)
            print(rhombus.get_height())

    def test_diagonals_bad_value_boolean(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(TypeError):
            rhombus = Rhombus(1, True, True)
            print(rhombus.get_height())

    def test_uid_bad_value_boolean(self):
        """
        Creates a Rhombus.
        Tests that the rhombus can be created with only normal arguments.
        """
        with self.assertRaises(TypeError):
            rhombus = Rhombus(True, 1, 1)
            print(rhombus.get_height())
