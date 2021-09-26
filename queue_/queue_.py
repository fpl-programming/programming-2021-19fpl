"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), queue_max_size: int = float('inf')):
        self.queue_ = []
        if data:
            self.queue_ = list(data)
        self.queue_max_size = queue_max_size
        if len(self.queue_) > self.queue_max_size:
            raise IndexError

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if len(self.queue_) == self.queue_max_size:
            raise IndexError
        self.queue_.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if not self.queue_:
            raise IndexError
        return self.queue_.pop(0)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.queue_

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.queue_)

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        if not self.queue_:
            raise IndexError
        return self.queue_[0]

    def max_size(self):
        """
        Return the maximum size of queue_
        :return: number of maximum size of queue_
        """
        return self.queue_max_size

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if the queue_ is not full
        """
        return len(self.queue_) == self.queue_max_size
