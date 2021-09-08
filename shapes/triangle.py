"""
Programming for linguists

Implementation of the class RightTriangle
"""
import math
from shapes.shape import Shape


class RightTriangle(Shape):
    """
    A class for right-angled triangle
    """

    def __init__(self, uid: int, a_side: int, b_side: int, c_side: int):
        super().__init__(uid)
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        return (self.a_side * self.b_side) // 2

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.a_side + self.b_side + self.c_side

    def get_diagonal(self):
        """
        Returns the diagonal length of a triangle
        :return int: the diagonal length of a triangle
        """
        return int(math.sqrt(self.a_side ** 2 + self.b_side ** 2))
