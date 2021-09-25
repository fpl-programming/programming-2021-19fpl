"""
Programming for linguists

Implementation of the data structure "Queue" based on Stack
"""

from typing import Iterable
from stack.stack import Stack


# pylint: disable=invalid-name
class QueueStack_(Stack):
    """
    Queue Data Structure On Stack
    """
    def __init__(self, data: Iterable = (), capacity: int = 50):
        super().__init__(data)
        if not isinstance(capacity, int):
            raise TypeError
        self._capacity = capacity

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise IndexError
        self.data = [element] + self.data

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError
        return self.data.pop()

    def full(self):
        """
        Return whether queuestack_ is full or not
        :return: True if size of queuestack_ equals the capacity of queue_.
                 False if the queuestack_ contains less elements.
        """
        if self.size() == self._capacity:
            return True
        return False

    def capacity(self):
        """
        Return the capacity of queuestack_
        :return: the capacity (maximum size) of queuestack_
        """
        return self._capacity


