"""
Programming for linguists

Implementation of the class Circle
"""
from math import pi
from shapes.shape import Shape


class Circle(Shape):
    """
    A class for circles
    """
    def __init__(self, uid: int, radius: int):
        super().__init__(uid)
        self.radius = radius

    def get_area(self):
        """
        Returns the area of a circle
        :return int: the area of a circle
        """
        area = pi * (self.radius ** 2)
        return area

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        :return int: the perimeter of a circle
        """
        perimeter = 2 * pi * self.radius
        return perimeter

    def get_diameter(self):
        """
        Returns the diameter of a circle
        :return int: the diameter of a circle
        """
        diameter = 2 * self.radius
        return diameter
