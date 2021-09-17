"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        if data is None:
            self.data = []
        elif self._are_data_iterated(data):
            self.data = list(data)
        else:
            raise ValueError

    @staticmethod
    def _are_data_iterated(data):
        """
        Check whether the data are iterable
        :param data: data to create stack
        :return: True if data is an iterable object
                 False if data is not an iterable object
        """
        return isinstance(data, Iterable)

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        self.data.append(element)

    def pop(self):
        """
        Delete the element on the top of stack
        """
        if not self.data:
            raise ValueError
        self.data.pop()

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if not self.data:
            raise ValueError
        return self.data[-1]

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not self.data
