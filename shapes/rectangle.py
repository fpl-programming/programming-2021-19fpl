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
        self.uid = uid
        self.width = width
        self.length = length

    def get_area(self):
        area = self.width * self.length
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.length)
        return perimeter

    def get_diagonal(self):
        diagonal = math.sqrt(self.width ** 2 + self.length ** 2)
        return diagonal
