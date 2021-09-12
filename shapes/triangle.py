"""
Programming for linguists

Implementation of the class Triangle
"""

from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    A class for triangles
    """
    def __init__(self, uid: int, side_1: int, side_2: int, side_3: int):
        super().__init__(uid)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.side_1 + self.side_2 + self.side_3

    def get_semi_perimeter(self):
        """
        Returns the semi perimeter of a triangle
        :return int: the semi perimeter of a triangle
        """
        perimeter = self.get_perimeter()
        return perimeter / 2

    def get_height(self):
        """
        Returns the height of a triangle
        :return int: the height of a triangle
        """
        semi_per = self.get_semi_perimeter()
        return (2 * sqrt(semi_per * (semi_per - self.side_1)
                         * (semi_per - self.side_2)
                         * (semi_per - self.side_3))) / self.side_1

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        height = self.get_height()
        return (self.side_1 * height) / 2

    def get_inscribed_circle_radius(self):
        """
        Returns the inscribed circle radius of a triangle
        :return int: the inscribed circle radius of a triangle
        """
        area = self.get_area()
        semi_per = self.get_semi_perimeter()
        return area / semi_per

    def get_circumscribed_circle_radius(self):
        """
        Returns the circumscribed circle radius of a triangle
        :return int: the circumscribed circle radius of a triangle
        """
        area = self.get_area()
        return self.side_1 * self.side_2 * self.side_3 / 4 * area
