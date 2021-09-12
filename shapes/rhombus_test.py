import unittest
from shapes.rhombus import Rhombus


class RhombusTestCase(unittest.TestCase):

    def test_id(self):
        r = Rhombus(228, 10, 10)
        self.assertEqual(r.get_uid(), 228)

    def test_square_area(self):
        r = Rhombus(0, 5, 5)
        self.assertEqual(r.get_area(), 12.5)

    def test_area(self):
        r = Rhombus(0, 5, 3)
        self.assertEqual(r.get_area(), 7.5)

    def test_perimeter(self):
        r = Rhombus(0, 6, 8)
        self.assertEqual(r.get_perimeter(), 20)

    def test_square_perimeter(self):
        r = Rhombus(0, 10, 10)
        self.assertLess(abs(r.get_perimeter() - 28.28), 0.1)

    def test_uid_bad_input(self):
        with self.assertRaises(TypeError):
          r =Rhombus('j', 8, 8)

    def test_diagonal1_bad_input(self):
        with self.assertRaises(TypeError):
            r = Rhombus(1, 'gg', 8)

    def test_diagonal2_bad_input(self):
        with self.assertRaises(TypeError):
            r = Rhombus(4, 8, 'gg')

    def test_all_bad_input(self):
        with self.assertRaises(TypeError):
            r = Rhombus('r', 'i', 'p')

    def test_uid_bad_value(self):
        with self.assertRaises(ValueError):
            r = Rhombus(-1, 8, 8)

    def test_diagonal1_bad_value(self):
        with self.assertRaises(ValueError):
            r = Rhombus(1, -1, 8)

    def test_diagonal2_bad_value(self):
        with self.assertRaises(ValueError):
            r = Rhombus(4, 8, -1)

    def test_all_bad_value(self):
        with self.assertRaises(ValueError):
            r = Rhombus(-1, -1, -1)

    def test_diagonals_bad_value_boolean(self):
        with self.assertRaises(TypeError):
            r = Rhombus(1, True, True)

    def test_uid_bad_value_boolean(self):
        with self.assertRaises(TypeError):
            r = Rhombus(True, 1, 1)