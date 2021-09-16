"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        if data is not None:
            self.data = data
        else:
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
            raise ValueError
        else:
            return self.data.pop(-1)

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.empty():
            raise ValueError
        else:
            return self.data[-1]

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        if self.data:
            return len(self.data)
        else:
            return 0

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        if not self.data:
            return True
        else:
            return False
