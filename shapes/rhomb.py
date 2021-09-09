"""
Programming for linguists

Implementation of the abstract class Rhomb
"""
import math
from shapes.rectangle import Rectangle

class Rhomb(Rectangle):
    def __init__(self, uid : int, side: int, alpha: int):
        super.__init__(uid, side, side)
        self.alpha = alpha

    def get_area(self):
        return self.side**2 * math.sin(self.alpha)

    def get_perimeter(self):
        return 4 * self.side

    def get_big_diagonal(self):
        return self.side * math.sqrt(2 + 2 * math.cos(self.alpha))

    def get_small_diagonal(self):
        return self.side * math.sqrt(2 + 2 * math.cos(180 - self.alpha))





