"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable
from stack.stack import Stack


# pylint: disable=invalid-name
class StackQueue:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), max_size_queue: int = float("inf")):
        self.first = Stack()
        self.second = Stack()
        self.max_size_queue = max_size_queue
        for element in list(data):
            self.put(element)

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.size() >= self.max_size_queue:
            raise IndexError
        return self.first.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError
        if self.second.empty():
            self._shift()
        element = self.second.top()
        self.second.pop()
        return element

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return self.size() == 0

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return self.first.size() + self.second.size()

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        if self.empty():
            raise IndexError
        if self.second.empty():
            self._shift()
        return self.second.top()

    def _shift(self):
        """
        shifts elements to second stack
        """
        while not self.first.empty():
            element = self.first.top()
            self.second.push(element)
            self.first.pop()
