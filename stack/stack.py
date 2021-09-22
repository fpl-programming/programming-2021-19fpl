"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class NumberOutOfRangeError(Exception):
    """
    Custom error
    """
    def __str__(self):
        return 'Stack is smaller than number'


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        try:
            self.data = list(data)
        except TypeError:
            self.data = []

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

    def pop_number_of_elements(self, number: int):
        """
        Delete the element on the top of stack and raises errors if incorrect arguments
        """
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError
        if number > self.size():
            raise NumberOutOfRangeError
        while number:
            self.pop()
            number -= 1
