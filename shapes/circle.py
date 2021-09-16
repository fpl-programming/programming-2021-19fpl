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
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_diameter(self):
        """
        Returns the diameter of a circle
        """
        return 2 * self.radius
