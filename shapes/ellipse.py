"""
Programming for linguists

Implementation of the class Ellipse
"""
import math
from shape import Shape


class Ellipse(Shape):
    """
    A class for ellipses
    """
    def __init__(self, uid: int, major_axis: int, minor_axis: int):
        super().__init__(uid)
        self.semi_major_axis = major_axis / 2
        self.semi_minor_axis = minor_axis / 2

    def get_area(self):
        """
        Returns the area of an ellipse
        :return int: the area of an ellipse
        """
        area = math.pi * self.semi_minor_axis * self.semi_major_axis
        return area

    def get_perimeter(self):
        """
        Returns the perimeter of an ellipse
        :return int: the perimeter of an ellipse
        """
        perimeter = 2 * math.pi * math.sqrt(((self.semi_minor_axis**2) + (self.semi_major_axis**2)) / 2)
        return perimeter
