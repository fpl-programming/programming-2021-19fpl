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
        return self.length * self.height

    def get_perimeter(self):
        return self.length * 4

    def get_diagonal(self):
        return self.length * math.sin(self.alpha / 2)
