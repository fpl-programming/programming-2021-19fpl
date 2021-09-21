"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node


#!
class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        self.top = None
        self.size = 0
        
    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        self.top = Node(element, self.top)

    def pop(self):
        """
        Delete the element on the top of stack
        """
        self.top = self.top.next_node

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        return self.top.val

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return self.size

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return self.top == None