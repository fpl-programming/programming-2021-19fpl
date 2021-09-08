"""
Programming for linguists

Implementation of the class Parallelogram
"""

from math import radians, sin, cos, sqrt
from shapes.shape import Shape


class Parallelogram(Shape):
    """
    A class for parallelogram
    """
    def __init__(self, uid: int, width: int, length: int, angle: float):
        super().__init__(uid)
        self.width = width
        self.length = length
        self.angle = angle

    def get_area(self):
        """
        Returns the area of a parallelogram
        :return int: the area of a parallelogram
        """
        return self.width * self.length * sin(radians(self.angle))

    def get_perimeter(self):
        """
        Returns the perimeter of a parallelogram
        :return int: the perimeter of a parallelogram
        """
        return 2 * (self.width + self.length)

    def get_diagonal(self):
        """
        Returns the largest diagonal length  of a parallelogram
        :return int: the largest diagonal length of a parallelogram
        """
        diagonal1 = (sqrt(pow(self.width, 2) + pow(self.length, 2) -
                          2 * self.width * self.length * cos(radians(self.angle))))
        diagonal2 = (sqrt(self.width ** 2 + self.length ** 2 -
                          2 * self.width * self.length * cos(radians(180 - self.angle))))
        return max(diagonal1, diagonal2)
