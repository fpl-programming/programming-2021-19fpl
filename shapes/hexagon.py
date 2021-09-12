"""
Programming for linguists

Implementation of the class Hexagon
"""
from math import sqrt
from shapes.shape import Shape


class Hexagon(Shape):
    """
    A class for hexagon
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid)
        self.length = length

    def get_area(self):
        """
        Returns the area of a hexagon
        :return int: the area of a hexagon
        """
        return (3 * sqrt(3) * self.length ** 2) / 2

    def get_perimeter(self):
        """
        Returns the perimeter of a hexagon
        :return int: the perimeter of a hexagon
        """
        return self.length * 6

    def get_main_diagonal(self):
        """
        Returns the diagonal length  of a hexagon
        :return int: the diagonal length of a hexagon
        """
        return 2 * self.length

    def get_small_diagonal(self):
        """
        Returns the diagonal length  of a hexagon
        :return int: the diagonal length of a hexagon
        """
        return self.length * sqrt(3)
