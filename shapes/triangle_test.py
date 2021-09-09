import unittest
from triangle import Triangle


class CircleTestCase(unittest.TestCase):
    def test_triangle_get_uid(self):
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_uid(), 0)

    def test_triangle_get_area(self):
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_area(), 6)

    def test_triangle_get_perimeter(self):
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_perimeter(), 12)

    def test_triangle_get_incircle_radius(self):
        triangle = Triangle(0, 3, 4, 5)
        self.assertEqual(triangle.get_incircle_radius(), 1)
