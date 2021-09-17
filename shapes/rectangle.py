"""
Programming for linguists

Implementation of the class Rectangle
"""

from shapes.parallelogram import Parallelogram


class Rectangle(Parallelogram):
    """
    A class for rectangles
    """
    def __init__(self, uid: int, width: int, length: int):
        super().__init__(uid, width, length, alpha=90)
