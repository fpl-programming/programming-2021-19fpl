"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Node:
    """
    Stack Node
    """
    def __init__(self, val, next_node):
        self.val = val
        self.next_node = next_node

    def get_val(self):
        """get value"""
        return self.val

    def get_next(self):
        """get next node"""
        return self.next_node


# pylint: disable=too-few-public-methods
class StackIterator:
    """
    Stack iterators class
    """
    def __init__(self, data):
        self.now_element = data

    def __next__(self):
        if self.now_element is None:
            raise StopIteration
        element = self.now_element.get_val()
        self.now_element = self.now_element.get_next()
        return element


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

    def __iter__(self):
        return StackIterator(self.my_top)

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
