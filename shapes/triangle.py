"""
Implementation of the class RegularTriangle
"""

import math
from shapes.shape import Shape


class RegularTriangle(Shape):
    """
    A class for regular triangels
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid)
        self.length = length

    def get_area(self):
        """
        Returns the area of a regular triangle
        :return float: the area of a regular triangle
        """
        return (self.length ** 2 * math.sqrt(3)) / 4

    def get_perimeter(self):
        """
        Returns the perimeter of a regular triangle
        :return int: the perimeter of a regular triangle
        """
        return self.length * 3

    def get_height(self):
        """
        Returns the height of a regular triangle
        :return float: the height of a regular triangle
        """
        return (self.length * math.sqrt(3)) / 2

    def get_circumscribed_radius(self):
        """
        Returns the radius of a circumscribed circle around a regular triangle
        :return float: the radius of a circumscribed circle around a regular triangle
        """
        return (self.length * math.sqrt(3)) / 3

    def get_inscribed_radius(self):
        """
        Returns the diameter of an inscribed circle into a regular triangle
        :return float: the radius of an inscribed circle into a regular triangle
        """
        return (self.length * math.sqrt(3)) / 6
