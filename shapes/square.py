"""
Programming for linguists

Implementation of the class Square
"""
import math
from shapes.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for squares
    """

    def __init__(self, uid: int, length: int):
        super().__init__(uid)
        self.length = length

    def get_area(self):
        """
        Returns the area of a square
        :return int: the area of a square
        """
        return self.length * 2

    def get_perimeter(self):
        """
        Returns the perimeter of a square
        :return int: the perimeter of a square
        """
        return self.length * 4

    def get_diagonal(self):
        """
        Returns the diagonal length of a square
        :return int: the diagonal length of a square
        """
        return math.sqrt(2 * self.length ** 2)
