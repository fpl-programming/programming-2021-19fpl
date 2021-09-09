from math import sqrt

from shape import Shape


class Triangle(Shape):
    def __init__(self, uid: int, first_side_l: int, second_side_l: int, third_side_l: int):
        super().__init__(uid)
        self.first_side_l = first_side_l
        self.second_side_l = second_side_l
        self.third_side_l = third_side_l

    def get_perimeter(self):
        return self.first_side_l + self.second_side_l + self.third_side_l

    def get_area(self):
        half_p = self.get_perimeter() / 2
        return (sqrt(half_p * (half_p - self.first_side_l) * (half_p - self.second_side_l) *
                (half_p - self.third_side_l)))

    def get_incircle_radius(self):
        return self.get_area() / (self.get_perimeter() / 2)
