"""
Programming for linguists

Implementation of the class Square
"""
from math import sqrt
from shapes.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for squares
    """
    def __init__(self, uid: int, length: int):
        self.uid = uid  # наследование от родителя?
        self.length = length

    def get_area(self):
        """
        Returns the area of a square
        :return int: the area of a square
        """
        area = self.length ** 2
        return area

    def get_perimeter(self):
        """
        Returns the perimeter of a square
        :return int: the perimeter of a square
        """
        perimeter = self.length * 4
        return perimeter

    def get_diagonal(self):
        """
        Returns the diagonal length of a square
        :return int: the diagonal length of a square
        """
        diagonal = sqrt(2 * (self.length ** 2))
        return diagonal
