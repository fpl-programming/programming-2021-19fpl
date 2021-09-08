"""
Programming for linguists

Implementation of the class Square
"""

from shape import Shape


class Square(Shape):
    """
    A class for squares
    """
    def __init__(self, uid: int, length: int):
        self.length = length
        super().__init__(uid)

    def get_area(self):
        """
        Returns the area of a square
        :return int: the area of a square
        """
        return self.length ** 2

    def get_perimeter(self):
        """
        Returns the perimeter of a square
        :return int: the perimeter of a square
        """
        return self.length * 4

    def get_diagonal(self):
        """
        Returns the diagonal length of a square
        :return int: the diagonal length of a square
        """
        return self.length * sqrt(2)
