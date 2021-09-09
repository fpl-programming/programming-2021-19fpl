"""
Programming for linguists
Implementation of the class RightTriangle
"""
import math
from shapes.shape import Shape


class RightTrapeze(Shape):
    """
    A class for right-angled triangle
    """

    def __init__(self, uid: int, a_s: int, b_s: int, c_s: int):
        super().__init__(uid)
        self.a_s = a_s
        self.b_s = b_s
        self.c_s = c_s

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        return ((self.a_s + self.b_s) / 2) * math.sqrt(self.c_s ** 2 -
                                                       ((self.a_s - self.b_s) ** 2) / 4)

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.a_s + self.b_s + (2 * self.c_s)

    def get_diagonal(self):
        """
        Returns the diagonal length of a triangle
        :return int: the diagonal length of a triangle
        """
        return int(math.sqrt(self.a_s ** 2 + self.b_s * self.c_s))
