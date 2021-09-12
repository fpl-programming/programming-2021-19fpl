"""
Programming for linguists

Implementation of the class Rectangle
"""


import math
from shapes.shape import Shape


class Triangle(Shape):
    """
    A class for rectangles
    """
    def __init__(self, uid: int, first_side: int, second_side: int, third_side: int):
        super().__init__(uid)
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def get_area(self):
        """
        Returns the area of a rectangle
        :return int: the area of a rectangle
        """
        perimetr = self.get_perimeter() / 2
        return math.sqrt(perimetr * (perimetr - self.first_side) * (perimetr - self.second_side) *
                         (perimetr - self.third_side))

    def get_perimeter(self):
        """
        Returns the perimeter of a rectangle
        :return int: the perimeter of a rectangle
        """
        return self.first_side + self.second_side + self.third_side

    def get_height(self):
        """
        Returns the diagonal length  of a rectangle
        :return int: the diagonal length of a rectangle
        """
        return 2 * self.get_area() / self.first_side
