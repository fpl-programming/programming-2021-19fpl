"""
Programming for linguists

Implementation of the class Triangle
"""

from shapes.shape import Shape

class Triangle(Shape):
    """
    A class for triangles
    """

    def __init__(self, uid: int, first_side: int, second_side: int, third_side: int):
        super().__init__(uid)
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def get_perimeter(self):
        """
        Returns the perimeter of a triangle
        :return int: the perimeter of a triangle
        """
        return self.first_side + self.second_side + self.third_side

    def get_area(self):
        """
        Returns the area of a triangle
        :return int: the area of a triangle
        """
        half_perimeter = self.get_perimeter() / 2
        return (half_perimeter * (half_perimeter - self.first_side) * 
               (half_perimeter - self.second_side) * (half_perimeter - self.third_side)) ** 0.5
