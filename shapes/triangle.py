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
    def __init__(self, uid: int, side_1: int, side_2: int, side_3: int):
        super().__init__(uid)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.side_1 + self.side_2 + self.side_3

    def get_semiperimeter(self):
        """
        Returns the semiperimeter of a triangle
        :return int: the semiperimeter of a triangle
        """
        return self.get_perimeter() / 2

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        semi_p = self.get_semiperimeter()
        return sqrt(semi_p * (semi_p - self.side_1) * (semi_p - self.side_2) * (semi_p - self.side_3))

    def get_shortest_altitude(self):
        """
        Returns the shortest altitude of a triangle
        :return int: the shortest altitude of a triangle
        """
        return (2 * self.get_area()) / max(self.side_1, self.side_2, self.side_3)

    def get_longest_altitude(self):
        """
        Returns the longest altitude of a triangle
        :return int: the longest altitude of a triangle
        """
        return (2 * self.get_area()) / min(self.side_1, self.side_2, self.side_3)
