"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        pass

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        pass

    def pop(self):
        """
        Delete the element on the top of stack
        """
        pass

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        pass

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        pass

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        pass
