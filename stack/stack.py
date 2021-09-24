"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


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
        if self.empty():
            raise ValueError('Stack is empty')
        self.data.pop()

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.empty():
            raise ValueError('Stack is empty')
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

    def clear(self):
        """
        Delete all elements from stack
        """
        if self.empty():
            raise ValueError('Stack is already empty')
        while self.size() > 0:
            self.pop()
