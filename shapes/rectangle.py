"""
Programming for linguists

Implementation of the class Rectangle
"""

import math
from shapes.shape import Shape


class Rectangle(Shape):
    """
    A class for rectangles
    """
    def __init__(self, uid: int, width: int, length: int):
        super().__init__(uid)
        self.width = width
        self.length = length

    def get_area(self):
        """
        Returns the area of a rectangle
        :return int: the area of a rectangle
        """
        area = self.width * self.length
        return area

    def get_perimeter(self):
        """
        Returns the perimeter of a rectangle
        :return int: the perimeter of a rectangle
        """
        perimeter = (self.width + self.length) * 2
        return perimeter

    def get_diagonal(self):
        """
        Returns the diagonal length  of a rectangle
        :return int: the diagonal length of a rectangle
        """
        diagonal = math.sqrt(self.width ** 2 + self.length ** 2)
        return diagonal
