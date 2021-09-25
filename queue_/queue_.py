"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable
from math import inf

# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), max_size=inf):
        if data is None:
            self.data = []
        else:
            self.data = list(data)
            self.data = self.data[:min(max_size, self.size())] # should use assert?
        self.max_size = max_size

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        assert self.max_size > self.size(), 'Too many elements in a queue.'
        self.data.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        return self.data.pop(0)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.data

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.data)

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        return self.data[0]
