"""
Programming for linguists

Implementation of the class Square
"""
import math
from shapes.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for squares
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid, length, length)

    def get_diagonal(self):
        """
        Returns the diagonal of a square
        """
        return math.sqrt(2 * self.length ** 2)
