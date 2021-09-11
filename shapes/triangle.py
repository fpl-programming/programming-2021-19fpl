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
    def __init__(self, uid: int, side1: int, side2: int, side3: int):
        super().__init__(uid)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        s_perimeter = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(s_perimeter*(s_perimeter-self.side1)*(s_perimeter-self.side2)*(s_perimeter-self.side3))

    def get_semi_perimeter(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        return (self.side1 + self.side2 + self.side3) / 2
