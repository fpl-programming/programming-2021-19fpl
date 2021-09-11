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
        self.uid = uid
        self.length = length

    def get_area(self):
        area = 3 ** 0.5 / 4 * self.length ** 2
        return area

    def get_perimeter(self):
        perimeter = 3 * self.length
        return perimeter

    def get_height(self):
        height = 3 ** 0.5 / 2 * self.length
        return height
