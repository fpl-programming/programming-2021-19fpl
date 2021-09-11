from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):

    def __init__(self, uid: int, a: int, b: int, c: int):
        super().__init__(uid)
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_semi_perimeter(self):
        return (self.a + self.b + self.c) / 2

    def get_area(self):
        semi_perimeter = (self.a + self.b + self.c) / 2
        return sqrt(semi_perimeter * (semi_perimeter-self.a)*(semi_perimeter-self.b)*(semi_perimeter-self.c))
