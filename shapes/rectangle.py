"""
Programming for linguists

Implementation of the class Rectangle
"""

from math import sqrt
from square import Square


class Rectangle(Square):
    """
    A class for rectangles
    """
    def __init__(self, uid: int, width: int, length: int):
        self.width = width
        super().__init__(uid, length)

    def get_area(self):
        """
        Returns the area of a rectangle
        :return int: the area of a rectangle
        """
        return self.length * self.width

    def get_perimeter(self):
        """
        Returns the perimeter of a rectangle
        :return int: the perimeter of a rectangle
        """
        return self.length * 2 + self.width * 2

    def get_diagonal(self):
        """
        Returns the diagonal length  of a rectangle
        :return int: the diagonal length of a rectangle
        """
        return sqrt(self.length ** 2 + self.width ** 2)
