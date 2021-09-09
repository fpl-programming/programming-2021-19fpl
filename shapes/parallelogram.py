from shapes.shape import Shape
from math import sin


class Parallelogram (Shape):

    def __init__(self, uid: int, larger_side: int, lower_side: int, acute_angle: int):
        super().__init__(uid)
        self.larger_side = larger_side
        self.lower_side = lower_side
        self.acute_angle = acute_angle

    def get_area(self):
        area = self.larger_side * self.lower_side * sin(self.acute_angle)
        return area

    def get_perimeter(self):
        perimeter = (2 * self.lower_side) + (2 * self.larger_side)
        return perimeter

    def get_larger_height(self):
        larger_height = self.get_area() // self.lower_side
        return larger_height

    def get_lower_height(self):
        lower_height = self.get_area() // self.larger_side
        return lower_height
