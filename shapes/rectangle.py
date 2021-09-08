"""
Programming for linguists

Implementation of the class Rectangle
"""
import math
from shapes.shape import Shape
class Rectangle (Shape):
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
        rectangle_area = self.length * self.width
        return rectangle_area

    def get_perimeter(self):
        """
        Returns the perimeter of a rectangle
        :return int: the perimeter of a rectangle
        """
        rectangle_perimeter = (self.length + self.width)*2
        return rectangle_perimeter

    def get_diagonal(self):
        """
        Returns the diagonal length  of a rectangle
        :return int: the diagonal length of a rectangle
        """
        rectangle_diagonal = math.sqrt (self.length**2 + self.width**2)
        return rectangle_diagonal
