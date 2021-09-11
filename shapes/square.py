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
        super().__init__(uid)
        self.length = length

    def get_area(self):
        area = self.length ** 2
        return area

    def get_perimeter(self):
        perimeter = 4 * self.length
        return perimeter

    def get_diagonal(self):
        """
        Returns the diagonal of a square
        """
        diagonal = math.sqrt(2 * self.length ** 2)
        return diagonal
