"""
Programming for linguists

Implementation of the class Rhombus
"""

import math
from shapes.shape import Shape


class Rhombus(Shape):
    """
    A class of Rhombus
    """
    def __init__(self, uid: int, length: int, height: int, alpha: int):
        super().__init__(uid)
        self.length = length
        self.height = height
        self.alpha = alpha

    def get_area(self):
        """
        Returns the area of a rhombus
        :return int: the area of a rhombus
        """
        return self.length * self.height

    def get_perimeter(self):
        """"
        Returns the perimeter of a rhombus
        :return int: the perimeter of a rhombus
        """
        return self.length * 4

    def get_diagonal(self):
        """
        Returns the diagonal length of a rhombus
        :return int: the diagonal length of a rhombus
        """
        short_diagonal = (self.length * 2) * math.sin(self.alpha / 2)
        long_diagonal = (self.length * 2) * math.cos(self.alpha / 2)
        return short_diagonal, long_diagonal
