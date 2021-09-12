import math
from numbers import Number

from shapes.shape import Shape


class Rhombus(Shape):
    def __init__(self, uid: int, diagonal_1: float, diagonal_2: float):
        super().__init__(uid)
        if not isinstance(uid, int) or str(type(uid)) == str(type(True)):
            raise TypeError
        if not isinstance(diagonal_1, Number) or str(type(diagonal_1)) == str(type(True)):
            raise TypeError
        if not isinstance(diagonal_2, Number) or str(type(diagonal_2)) == str(type(True)):
            raise TypeError
        if uid < 0 or diagonal_2 <= 0 or diagonal_1 <= 0:
            raise ValueError
        self.diagonal_1 = diagonal_1
        self.diagonal_2 = diagonal_2
        self.length = ((diagonal_1 / 2) ** 2 + (diagonal_2 / 2) ** 2) ** 0.5

    def get_area(self):
        return (self.diagonal_1 * self.diagonal_2) / 2

    def get_perimeter(self):
        return self.length * 4

    def get_height(self):
        return self.diagonal_1 * self.diagonal_2 / (2 * self.length)
