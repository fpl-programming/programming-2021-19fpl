"""
Programming for linguists

Implementation of the class Diamond
"""
from shapes.rectangle import Rectangle


class Diamond(Rectangle):
    """
    A class for squares
    """
    def __init__(self, uid: int, diagonal_one: int, diagonal_two: int):
        super().__init__(uid, diagonal_one, diagonal_two)

    def get_area(self):
        """
        Returns the area of a square
        :return int: the area of a square
        """
        return super().get_area() / 2

    def get_perimeter(self):
        """
        Returns the perimeter of a square
        :return int: the perimeter of a square
        """
        return 4 * ((((self.length / 2) ** 2) + ((self.width / 2) ** 2)) ** 0.5)

    def get_side(self):
        """
        Returns the diagonal length of a square
        :return int: the diagonal length of a square
        """
        return self.get_perimeter() / 4
