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
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_diagonal(self):
        """
        Returns the diagonal of a rectangle
        """
        return math.sqrt(self.width ** 2 + self.length ** 2)
