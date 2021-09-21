"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        self.my_top = None
        self.my_size = 0
        if data is not None:
            for element in data:
                self.push(element)
    
    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        self.my_top = Node(element, self.my_top)
        self.my_size += 1

    def pop(self):
        """
        Delete the element on the top of stack
        """
        if self.empty():
            raise ValueError
        self.my_top = self.my_top.next_node
        self.my_size -= 1

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.empty():
            raise ValueError
        return self.my_top.val

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return self.my_size

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return self.my_size == 0
