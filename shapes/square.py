"""
Programming for linguists

Implementation of the class Square
"""
from shapes.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for squares
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid, length, length)

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
