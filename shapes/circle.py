"""
Programming for linguists

Implementation of the class Circle
"""
import math

class Circle:
    uidCircle = 0
    """
    A class for circles
    """
    def __init__(self, uid: int, radius: int):
        self.uid = uid
        self.radius = radius
        Circle.uidCircle = 0

    def get_area(self):
        """
        Returns the area of a circle
        :return int: the area of a circle
        """
        circle_area = math.pi*(self.radius**2)
        return circle_area

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        :return int: the perimeter of a circle
        """
        circle_perimeter = 2*math.pi*self.radius
        return circle_perimeter

    def get_diameter(self):
        """
        Returns the diameter of a circle
        :return int: the diameter of a circle
        """
        circle_diameter = 2*self.radius
        return circle_diameter
