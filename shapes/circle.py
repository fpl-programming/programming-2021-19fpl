"""
Programming for linguists

Implementation of the class Circle
"""

from shape import Shape
import math


class Circle(Shape):
    """
    A class for circles
    """
    def __init__(self, uid: int, radius: int):
        super().__init__(uid)
        self.radius = radius

    def get_area(self):
        """
        Returns the area of a circle
        :return int: the area of a circle
        """
        area = math.pi * self.radius ** 2
        return area

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        :return int: the perimeter of a circle
        """
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def get_diameter(self):
        """
        Returns the diameter of a circle
        :return int: the diameter of a circle
        """
        diameter = self.radius * 2
        return diameter
