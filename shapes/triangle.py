from shapes.shape import Shape
import math

class RightTriangle(Shape):
    """
    A class for right-angled triangle
    """
    def __init__(self, uid: int, a: int, b: int, c: int):
        super().__init__(uid)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        return (self.a * self.b) // 2

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_diagonal(self):
        return int(math.sqrt(self.a**2 + self.b**2))

t = RightTriangle(4, 3, 4, 5)
print(t.get_area())
print(t.get_perimeter())
print(t.get_diagonal())