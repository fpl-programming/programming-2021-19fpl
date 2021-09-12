"""
Programming for linguists

Implementation of the class Circle
"""

import math
from shapes.shape import Shape

class Circle:
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
        return pi * self.radius**2

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        :return int: the perimeter of a circle
        """


    def get_diameter(self):
        """
        Returns the diameter of a circle
        :return int: the diameter of a circle
        """
        pass
