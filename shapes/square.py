"""
Programming for linguists

Implementation of the class Square
"""
from math import sqrt
from shapes.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for squares
    """
    def __init__(self, uid: int, length: int):
        super().__init__(uid, length, length)
