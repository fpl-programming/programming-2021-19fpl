"""
Programming for linguists

Implementation of the class Trapeze
"""
from math import sqrt, asin, pi
from shapes.shape import Shape


class Trapeze(Shape):
    """
    A class for trapezes
    """

    def __init__(self, uid: int, left: int, right: int, upper: int, lower: int):
        super().__init__(uid)
        self.left = left
        self.right = right
        self.upper = upper
        self.lower = lower

    @property
    def _get_height(self):
        """
        Returns the height of a trapeze
        :return float: the area of a circle
        """
        numerator = (self.lower - self.upper) ** 2 + self.right ** 2 - self.left ** 2
        denominator = 2 * (abs(self.lower - self.upper))
        return sqrt(self.right ** 2 - (numerator / denominator) ** 2)

    def get_area(self):
        """
        Returns the area of a trapeze
        :return float: the area of a trapeze
        """
        return 0.5 * self._get_height * (self.lower + self.upper)

    def get_perimeter(self):
        """
        Returns the perimeter of a trapeze
        :return int: the perimeter of a trapeze
        """
        return self.right + self.left + self.lower + self.upper

    def get_mean_line(self):
        """
        Returns the mean line of a trapeze
        :return float: the mean line of a trapeze
        """
        return (self.upper + self.lower) / 2

    def get_angles_of_base(self):
        """
        Returns the mean line of a trapeze
        :return tuple: left angle, right angle
        """
        h = self._get_height
        left = asin(h / self.left) * 180 / pi
        right = asin(h / self.right) * 180 / pi

        return left, right
