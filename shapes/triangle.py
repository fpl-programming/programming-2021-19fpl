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
    def __init__(self, uid: int, side_a: int, side_b: int, side_c: int):
        super().__init__(uid)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        semi_perimeter = self.get_perimeter() / 2
        return sqrt(semi_perimeter *
                        (semi_perimeter - self.side_a) *
                            (semi_perimeter - self.side_b) *
                                (semi_perimeter - self.side_c))

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.side_a + self.side_b + self.side_c

    def get_int_circle_rad(self):
        """
        Returns the radius of internal circle of a triangle
        :return int: the radius of internal circle of a triangle
        """
        return (2 * self.get_area()) / self.get_perimeter()
