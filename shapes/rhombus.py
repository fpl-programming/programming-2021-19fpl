"""
Programming for linguists

Implementation of the class Rectangle
"""
# from shapes.shape import Shape
import math
from shapes.square import Square

class Rhombus(Square):
    """
    A class for rectangles
    """
    def __init__(self, uid: int, length: int, angle:float):
        super().__init__(uid, length)
        self.angle = angle

    def get_area(self):
        """
        Returns the area of a rhombus
        :return int: the area of a rhombus
        """
        d_1, d_2 = self.get_diagonal()
        return d_1 * d_2 / 2

    def get_diagonal(self):
        """
        Returns the diagonals' lengths  of a rhombus
        :return ints: the diagonals' lengths of a rhombus
        """
        big_angle = (180 - (self.angle * 2)) / 2
        return 2*self.length*math.cos(math.radians(big_angle/2)), 2*self.length*math.cos(math.radians(self.angle/2))
