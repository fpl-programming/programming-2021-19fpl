"""
Programming for linguists

Implementation of the class Triangle
"""

from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    A class for triangles
    """
    def __init__(self, uid: int, first_edge: int, second_edge: int, third_edge: int):
        super().__init__(uid)
        self.first_edge = first_edge
        self.second_edge = second_edge
        self.third_edge = third_edge

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        semi_per = self.get_perimeter() / 2
        return sqrt(semi_per *
                    (semi_per - self.first_edge) *
                    (semi_per - self.second_edge) *
                    (semi_per - self.third_edge))

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.first_edge + self.second_edge + self.third_edge

    def get_altitude(self):
        """
        Returns the largest altitude of a triangle
        :return int: the largest altitude of a triangle
        """
        return 2 * self.get_area() / min(self.first_edge, self.second_edge, self.third_edge)
