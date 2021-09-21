"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        if data and isinstance(data, list):
            self.stack = data
        elif isinstance(data, int) or isinstance(data, float):
            self.stack = [data]
        elif data:
            self.stack = list(data)
        elif not data:
            self.stack = []

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        self.stack.append(element)

    def pop(self):
        """
        Delete the element on the top of stack
        """
        if self.stack:
            self.stack.pop(-1)
        else:
            raise ValueError

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.stack:
            return self.stack[-1]
        raise ValueError

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.stack)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not self.stack







