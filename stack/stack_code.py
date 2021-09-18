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
            self.stack = data
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
        if self.stack:
            self.stack = self.stack[:-1]
        else:
            raise ValueError

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.stack:
            return self.stack[-1]
        else:
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
        if not self.stack:
            return True
        else:
            return False
