"""
Programming for linguists

Implementation of the abstract class Shape
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    An abstract class of a shape
    """
    def __init__(self, uid: int):
        self.uid = uid

    def get_uid(self):
        """
        Returns the uid of a shape
        """
        return self.uid

    @abstractmethod
    def get_area(self):
        """
        Returns the area of a shape
        """
        return self.get_area()

    @abstractmethod
    def get_perimeter(self):
        """
        Returns the perimeter of a shape
        """
        return self.get_perimeter()

