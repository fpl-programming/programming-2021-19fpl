"""
Programming for linguists

Implementation of the data structure "Queue on stack"
"""
from typing import Iterable
from math import inf
from stack.stack import Stack
from queue_.queue_ import LimitError


# pylint: disable=invalid-name
class QueueOnStack_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), limit: int = inf):
        self.data = Stack(data) if data is not None else Stack()
        self.limit = limit

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.data.size() >= self.limit:
            raise LimitError('limit has been reached')
        self.data.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.data.empty():
            raise IndexError

        temp_data = Stack()
        while self.data.size() > 1:
            temp_data.push(self.data.top())
            self.data.pop()
        elem = self.data.top()
        self.data.pop()

        while temp_data.size():
            self.data.push(temp_data.top())
            temp_data.pop()
        return elem

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return self.data.empty()

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return self.data.size()

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        if self.data.empty():
            raise IndexError

        temp_data = Stack()
        while self.data.size():
            temp_data.push(self.data.top())
            self.data.pop()
        elem = temp_data.top()

        while temp_data.size():
            self.data.push(temp_data.top())
            temp_data.pop()
        return elem
