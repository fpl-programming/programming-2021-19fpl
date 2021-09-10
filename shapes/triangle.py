"""
Programming for linguists

Implementation of the class Triangle
"""
import math
from shapes.shape import Shape

class Triangle (Shape):
    """
    A class for triangles
    """
    def __init__(self, uid: int, first_s: int, second_s: int, third_s:int):
        self.first_s=first_s
        self.second_s=second_s
        self.third_s = third_s
        super().__init__(uid)

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.first_s+self.second_s+self.third_s
    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """

        half_p=self.get_perimeter()/2
        return math.sqrt(half_p*(half_p-self.first_s)
                         *(half_p-self.second_s)
                         *(half_p-self.third_s))


    def get_height(self):
        """
        Returns the three heights  of a triangle

        """

        return 2*self.get_area()/self.first_s,\
               2*self.get_area()/self.second_s,\
               2*self.get_area()/self.third_s
