"""
Programming for linguists

Implementation of the class Rhombus
"""

from shapes.square import Square


class Rhombus(Square):
    """
    A class for rhombi
    """
    def __init__(self, uid: int, length: int, sin: float):
        self.sin = sin
        super().__init__(uid, length)

    def get_area(self):
        """
        Returns the area of a rhombus
        :return int: the area of a rhombus
        """
        return int(self.length ** 2 * self.sin)

    def get_height(self):
        """
        Returns the height of a rhombus
        :return int: the height of a rhombus
        """
        return int(self.length * self.sin)
