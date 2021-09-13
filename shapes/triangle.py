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
        :return int: the area of a regular triangle
        """
        area = (self.length ** 2 * math.sqrt(3)) / 4
        return area

    def get_perimeter(self):
        """
        Returns the perimeter of a regular triangle
        :return int: the perimeter of a regular triangle
        """
        perimeter = self.length * 3
        return perimeter

    def get_height(self):
        """
        Returns the height of a regular triangle
        :return int: the height of a regular triangle
        """
        height = (self.length * math.sqrt(3)) / 2
        return height

    def get_circumscribed_radius(self):
        """
        Returns the radius of a circumscribed circle around a regular triangle
        :return int: the radius of a circumscribed circle around a regular triangle
        """
        circum_radius = (self.length * math.sqrt(3)) / 3
        return circum_radius

    def get_inscribed_radius(self):
        """
        Returns the diameter of an inscribed circle into a regular triangle
        :return int: the radius of an inscribed circle into a regular triangle
        """
        in_radius = (self.length * math.sqrt(3)) / 6
        return in_radius
