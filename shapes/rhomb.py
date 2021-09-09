"""
Programming for linguists

Implementation of the abstract class Rhomb
"""
import math
from shapes.rectangle import Rectangle

class Rhomb(Rectangle):
    """
    A class for rhomb
    """
    def __init__(self, uid: int, length: int, alpha: int):
        super().__init__(uid, length, length)
        self.alpha = alpha

    def get_area(self):
        """
        Returns the area of a rhomb
        :return int: the area of a rhomb
        """
        return self.length**2 * math.sin(self.alpha)

    def get_perimeter(self):
        """
        Returns the perimeter of a rhomb
        :return int: the perimeter of a rhomb
        """
        return 4 * self.length

    def get_diagonal(self):
        """
        Returns the diagonal length of a rhomb
        :return int: the diagonal length of a rhomb
        """
        big_diagonal = self.length * math.sqrt(2 + 2 * math.cos(self.alpha))
        small_diagonal = self.length * math.sqrt(2 + 2 * math.cos(180 - self.alpha))

        return big_diagonal, small_diagonal
