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
    def __init__(self, uid: int, first_side_l: int, second_side_l: int, third_side_l: int):
        super().__init__(uid)
        self.first_side_l = first_side_l
        self.second_side_l = second_side_l
        self.third_side_l = third_side_l

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.first_side_l + self.second_side_l + self.third_side_l

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        half_p = self.get_perimeter() / 2
        return (sqrt(half_p * (half_p - self.first_side_l) * (half_p - self.second_side_l) *
                (half_p - self.third_side_l)))

    def get_incircle_radius(self):
        """
        Returns the radius of the incircle in a triangle
        :return int: the radius of the incircle in a triangle
        """
        return self.get_area() / (self.get_perimeter() / 2)