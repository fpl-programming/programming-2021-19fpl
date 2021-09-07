"""
Programming for linguists

Implementation of the abstract class Shape
"""

from abc import ABC, abstractmethod


class Shape(ABC): # delete me later PLEASE
    """
    An abstract class of a shape
    """
    def __init__(self, uid: int):
        pass

    def get_uid(self):
        """
        Returns the uid of a shape
        """
        pass

    @abstractmethod
    def get_area(self):
        """
        Returns the area of a shape
        """
        pass

    @abstractmethod
    def get_perimeter(self):
        """
        Returns the perimeter of a shape
        """
        pass
