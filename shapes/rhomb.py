"""
Programming for linguists

Implementation of the abstract class Rhomb
"""
import math
from shapes.rectangle import Rectangle

class Rhomb(Rectangle):
    def __init__(self, uid : int, length: int, alpha: int):
        super.__init__(uid, length, length)
        self.alpha = alpha

    def get_area(self):
        """
        Returns the area of a rhomb
        :return int: the area of a rhomb
        """
        return self.side**2 * math.sin(self.alpha)

    def get_perimeter(self):
        """
        Returns the perimeter of a rhomb
        :return int: the perimeter of a rhomb
        """
        return 4 * self.side

    def get_big_diagonal(self):
        """
        Returns the big diagonal length of a rhomb
        :return int: the big diagonal length of a rhomb
        """
        return self.side * math.sqrt(2 + 2 * math.cos(self.alpha))

    def get_small_diagonal(self):
        """
        Returns the small diagonal length of a rhomb
        :return int: the diagonal length of a rhomb
        """
        return self.side * math.sqrt(2 + 2 * math.cos(180 - self.alpha))





