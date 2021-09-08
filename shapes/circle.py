"""
Programming for linguists

Implementation of the class Circle
"""

from math import pi
from shape import Shape


class Circle(Shape):
    """
    A class for circles
    """
    def __init__(self, uid: int, radius: int):
        self.radius = radius
        super().__init__(uid)

    def get_area(self):
        """
        Returns the area of a circle
        :return int: the area of a circle
        """
        return self.radius * self.radius * pi

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        :return int: the perimeter of a circle
        """
        return pi * 2 * self.radius

    def get_diameter(self):
        """
        Returns the diameter of a circle
        :return int: the diameter of a circle
        """
        return 2 * self.radius
