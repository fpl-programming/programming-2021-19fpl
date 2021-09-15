"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        self.stack_list = []
        if data:
            for element in data:
                self.stack_list.append(element)

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        self.stack_list.append(element)

    def pop(self):
        """
        Delete the element on the top of stack
        """
        if self.stack_list:
            self.stack_list.pop()
        else:
            raise ValueError

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.stack_list:
            return self.stack_list[-1]
        raise ValueError

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.stack_list)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        stack_length = len(self.stack_list)
        if stack_length:
            return False
        return True
