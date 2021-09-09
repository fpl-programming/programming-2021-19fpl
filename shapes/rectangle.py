"""
Programming for linguists

Implementation of the class Rectangle
"""
from shapes.parallelogram import Parallelogram
from math import sqrt


class Rectangle(Parallelogram):
    """
    A class for rectangles
    """
    def __init__(self, uid: int, width: int, length: int):
        self.uid = uid  # унаследование от родителя?
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
        perimeter = (2 * self.width) + (2 * self.length)
        return perimeter

    def get_diagonal(self):
        """
        Returns the diagonal length  of a rectangle
        :return int: the diagonal length of a rectangle
        """
        diagonal = sqrt((self.length ** 2) + (self.width ** 2))
        return diagonal
