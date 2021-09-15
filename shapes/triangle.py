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
    def __init__(self, uid: int, left_side: int, right_side: int, bottom_side: int):
        super().__init__(uid)
        self.left_side = left_side
        self.right_side = right_side
        self.bottom_side = bottom_side

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.left_side + self.right_side + self.bottom_side

    def get_semiperimeter(self):
        """
        Returns the semiperimeter of a triangle
        :return int: the semiperimeter of a triangle
        """
        return (self.left_side + self.right_side + self.bottom_side) / 2

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        semi_p = self.get_semiperimeter()
        return sqrt(semi_p
                    * (semi_p - self.left_side)
                    * (semi_p - self.right_side)
                    * (semi_p - self.bottom_side))

    def get_shortest_altitude(self):
        """
        Returns the shortest altitude of a triangle
        :return int: the shortest altitude of a triangle
        """
        return (2 * self.get_area()) / max(self.left_side, self.right_side, self.bottom_side)

    def get_longest_altitude(self):
        """
        Returns the longest altitude of a triangle
        :return int: the longest altitude of a triangle
        """
        return (2 * self.get_area()) / min(self.left_side, self.right_side, self.bottom_side)
