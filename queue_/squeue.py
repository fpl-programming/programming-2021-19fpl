"""
Programming for linguists
Implementation of the data structure "Queue" based on Stack
"""

from typing import Iterable
from stack.stack import Stack
from queue_.queue_ import EmptyQueueError, QueueOverflowError


class SQueue(Stack):
    """
    Queue Data Structure Based On Stack
    """
    def __init__(self, data: Iterable = (), capacity: int = 50):
        super().__init__(data)

        if not isinstance(capacity, int):
            raise TypeError

        self._capacity = capacity

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise EmptyQueueError

        return self.data.pop()

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise QueueOverflowError

        self.data = [element] + self.data

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if size of queue_ equals the capacity of queue_.
                 False if the queue_ contains less elements.
        """
        if self.size() == self._capacity:
            return True

        return False

    def capacity(self):
        """
        Return the capacity of queue_
        :return: the capacity (maximum size) of queue_
        """
        return self._capacity
