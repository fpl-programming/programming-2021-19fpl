"""
Programming for linguists

Implementation of the class Parallelogram
"""
from math import sin
from shapes.shape import Shape


class Parallelogram (Shape):
    """
    A class for parallelograms
    """
    def __init__(self, uid: int, width: int, length: int, acute_angle: int):
        super().__init__(uid)
        self.width = width
        self.length = length
        self.acute_angle = acute_angle

    def get_area(self):
        """
        Returns the area of a parallelogram
        :return int: the area of a parallelogram
        """
        return self.length * self.width * sin(self.acute_angle)

    def get_perimeter(self):
        """
        Returns the perimeter of a parallelogram
        :return int: the perimeter of a parallelogram
        """
        return (2 * self.width) + (2 * self.length)

    def get_larger_height(self):
        """
        Returns the larger height of a parallelogram
        :return int: the larger height of a parallelogram
        """
        return self.get_area() // self.width

    def get_lower_height(self):
        """
        Returns the lower height of a parallelogram
        :return int: the lower height of a parallelogram
        """
        return self.get_area() // self.length
