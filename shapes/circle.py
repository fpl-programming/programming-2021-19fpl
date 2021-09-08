"""
Programming for linguists

Implementation of the class Circle
"""

from shapes.shape import Shape

class Circle(Shape):
    """
    A class for circles
    """
    def __init__(self, uid: int, radius: int):
        super().__init__(uid)

    def get_area(self):
        """
        Returns the area of a circle
        :return int: the area of a circle
        """
        pass

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        :return int: the perimeter of a circle
        """
        pass

    def get_diameter(self):
        """
        Returns the diameter of a circle
        :return int: the diameter of a circle
        """
        pass
