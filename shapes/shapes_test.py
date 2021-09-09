"""
Programming for linguists

Tests for all classes of shapes.
"""

import unittest

from shapes.shape import Shape
from shapes.square import Square
from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.triangle import Triangle


class ShapesTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of different shapes
    """
    def test_shapes_get_area(self):
        """
        Creates different shapes.
        Tests that the area is calculated correctly.
        """
        shapes = [Square(0, 5), Circle(0, 3), Rectangle(0, 5, 6), Triangle(0, 3, 4, 5)]
        areas = [25, 28.274333882308138, 30, 6]
        for index, shape in enumerate(shapes):
            self.assertEqual(shape.get_area(), areas[index])

    def test_shapes_get_perimeter(self):
        """
        Creates different shapes.
        Tests that the perimeter is calculated correctly.
        """
        shapes = [Square(0, 5), Circle(0, 2), Rectangle(0, 5, 6), Triangle(0, 3, 4, 5)]
        areas = [20, 12.566370614359172, 22, 12]
        for index, shape in enumerate(shapes):
            self.assertEqual(shape.get_perimeter(), areas[index])

    def test_shapes_impossible_create_abstract_shape(self):
        """
        Tries to create an abstract shape.
        Tests that the error is raised.
        """
        self.assertRaises(TypeError, Shape, 0)
