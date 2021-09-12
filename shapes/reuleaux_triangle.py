"""
Programming for linguists
Implementation of the class ReuleauxTriangle
"""

import math

from shapes.shape import Shape


class ReuleauxTriangle(Shape):
    """
    A class for Reuleaux triangles
    """

    def __init__(self, uid: int, width: int):
        super().__init__(uid)
        self.width = width

    def get_area(self):
        """
        Returns the area of an Reuleaux triangle
        :return int: the area of an Reuleaux triangle
        """
        area = 0.5 * (math.pi - math.sqrt(3)) * (self.width ** 2)
        return area

    def get_perimeter(self):
        """
        Returns the perimeter of an Reuleaux triangle
        :return float: the perimeter of an Reuleaux triangle
        """
        perimeter = math.pi * self.width
        return perimeter

    def get_inscribed_circle_radius(self):
        """
        Returns the inscribed circle radius of an Reuleaux triangle
        :return float: the inscribed circle radius of an Reuleaux triangle
        """
        inscribed_circle_radius = (1 - 1 / math.sqrt(3)) * self.width
        return inscribed_circle_radius

    def get_circumscribed_circle_radius(self):
        """
        Returns the circumscribed circle radius of an Reuleaux triangle
        :return float: the circumscribed circle radius of an Reuleaux triangle
        """
        circumscribed_circle_radius = self.width / math.sqrt(3)
        return circumscribed_circle_radius
