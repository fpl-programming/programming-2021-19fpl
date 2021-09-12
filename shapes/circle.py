"""
Programming for linguists

Implementation of the class Circle
"""

from math import pi


from shapes.shape import Shape
class Circle:
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
        circle_area = self.radius ** 2 * math.pi
        return circle_area

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        :return int: the perimeter of a circle
        """
        circle_perimeter = self.radius * 2 * math.pi
        return circle_perimeter

    def get_diameter(self):
        """
        Returns the diameter of a circle
        :return int: the diameter of a circle
        """
        circle_diameter = self.radius * 2
        return circle_diameter
