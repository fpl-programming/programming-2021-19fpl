"""
Programming for linguists

Implementation of the class Triangle
"""
from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    A class for triangles
    """
    def __init__(self, uid: int, first_side: int, second_side: int, third_side: int):
        super().__init__(uid)
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        return sqrt(self.get_half_the_perimeter() * (self.get_half_the_perimeter() - self.first_side)
                    * (self.get_half_the_perimeter() - self.second_side)
                    * (self.get_half_the_perimeter() - self.third_side))

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.first_side + self.second_side + self.third_side

    def get_half_the_perimeter(self):
        """
        Returns the half thr perimeter of a triangle
        :return int: the half of perimeter of a triangle
        """
        return self.get_perimeter() / 2
