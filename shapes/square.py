"""
Programming for linguists

Implementation of the class Square
"""
import math
from shapes.shape import Shape

class Square(Shape):
    """
    A class for squares
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid, length, length)

    def get_area(self):
        """
        Returns the area of a square
        :return int: the area of a square
        """
        square_area = self.length ** 2
        return square_area

    def get_perimeter(self):
        """
        Returns the perimeter of a square
        :return int: the perimeter of a square
        """
        square_perimeter = self.length * 4
        return square_perimeter

    def get_diagonal(self):
        """
        Returns the diagonal length of a square
        :return int: the diagonal length of a square
        """
        square_diagonal = sqrt(2 * (self.length ** 2))
        return square_diagonal
