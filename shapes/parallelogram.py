"""
Programming for linguists

Implementation of the class Parallelogram
"""
import math
from shapes.shape import Shape

class Parallelogram(Shape):
    """
    A class for parallelogram
    """
    def __init__(self, uid: int, small_side: int, big_side: int, height: int, beta_angle: int):
        super().__init__(uid)
        self.small_side = small_side
        self.big_side = big_side
        self.height = height
        self.beta_angle = beta_angle

    def get_area(self):
        """
        Returns the area of a parallelogram
        :return int: the area of a parallelogram
        """
        parallelogram_area = self.height*self.big_side
        return parallelogram_area

    def get_perimeter(self):
        """
        Returns the perimeter of a parallelogram
        :return int: the perimeter of a parallelogram
        """
        parallelogram_perimeter = 2*(self.big_side+self.small_side)
        return parallelogram_perimeter

    def get_diagonal(self):
        """
        Returns the diagonal length  of a parallelogram
        :return int: the diagonal length of a parallelogram
        """

        parallelogram_diagonal = math.sqrt((math.pow(self.big_side, 2) +\
                                           math.pow(self.small_side, 2)) - 2 * self.big_side *\
                                           self.small_side * math.cos(self.beta_angle))
        return round(parallelogram_diagonal)
