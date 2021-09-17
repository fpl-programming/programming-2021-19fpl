"""
Programming for linguists

Implementation of the class Rectangle
"""

from math import radians, sin, cos

from shapes.shape import Shape


class Parallelogram(Shape):
    """
    A class for parallelograms
    """
    def __init__(self, uid: int, width: int, length: int, alpha: int):
        super().__init__(uid)
        self.width = width
        self.length = length
        self.alpha = radians(alpha)

    def get_area(self):
        """
        Returns the area of a parallelogram
        :return int: the area of a parallelogram
        """
        return self.length * self.width * sin(self.alpha)

    def get_perimeter(self):
        """
        Returns the perimeter of a parallelogram
        :return int: the perimeter of a parallelogram
        """
        return 2 * (self.length + self.width)

    def get_diagonal(self, short: bool = True):
        """
        Returns the diagonal length of a parallelogram
        :return int: the diagonal length of a parallelogram
        """
        sides_square_sum = self.length ** 2 + self.width ** 2
        double_sides_cos_product = 2 * self.length * self.width * cos(self.alpha)

        if short:
            return (sides_square_sum - double_sides_cos_product) ** 0.5
        return (sides_square_sum + double_sides_cos_product) ** 0.5
