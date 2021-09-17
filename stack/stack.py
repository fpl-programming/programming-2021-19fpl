"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        if data:
            self.stack = [i for i in data]
        else:
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
        if not self.stack:
            raise ValueError
        self.stack = self.stack[:-1]

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if not self.stack:
            raise ValueError
        return self.stack[-1]

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.stack) if self.stack else 0

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return False if bool(self.stack) else True
