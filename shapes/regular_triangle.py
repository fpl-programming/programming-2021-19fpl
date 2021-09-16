"""
Programming for linguists

Implementation of the class RegularTriangle
"""
from shapes.shape import Shape


class RegularTriangle(Shape):
    """
    A class for regular triangles
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid)
        self.length = length

    def get_area(self):
        return 3 ** 0.5 / 4 * self.length ** 2

    def get_perimeter(self):
        return 3 * self.length

    def get_height(self):
        """
        Returns the height of a regular triangle
        """
        return 3 ** 0.5 / 2 * self.length
