"""
Programming for linguists

Implementation of the class Square
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    A class for squares
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid, length, length)

    def get_area(self):
        """
        Returns the area of a square
        :return int: the area of a square
        """
        return super().get_area()

    def get_perimeter(self):
        """
        Returns the perimeter of a square
        :return int: the perimeter of a square
        """
        pass
        return super().get_perimeter()

    def get_diagonal(self):
        """
        Returns the diagonal length of a square
        :return int: the diagonal length of a square
        """
        pass
        return super().get_diagonal()

    def get_inradius(self):
        """
        Returns the radius of the inscribed circle
        :return int: the radius of the inscribed circle
        """
        return self.length / 2

    def get_circumradius(self):
        """
        Returns the radius of the circumscribed circle
        :return int: the radius of the circumscribed circle
        """
        return self.get_diagonal() / 2
