"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable
from math import inf


class LimitError(Exception):
    pass


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), limit: int = inf):
        self.data = list(data) if data is not None else []
        self.limit = limit

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.size() >= self.limit:
            raise LimitError('limit has been reached')
        self.data.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.data:
            return self.data.pop(0)
        raise IndexError

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not bool(self.data)

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
        if self.data:
            return self.data[0]
        raise ValueError
