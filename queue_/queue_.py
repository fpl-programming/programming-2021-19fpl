"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


class ExceededMaxSizeError(Exception):
    """
    Custom error
    """


class IncorrectMaxSizeError(Exception):
    """
    Custom error
    """


class QueueIsFullError(Exception):
    """
    Custom error
    """


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """
    def __init__(self, data: Iterable = (), maxsize=0):
        try:
            self.data = list(data)
            if not isinstance(maxsize, int) or isinstance(maxsize, bool):
                raise IncorrectMaxSizeError
            self._maxsize = maxsize
            if self._maxsize and self.size() > self._maxsize:
                raise ExceededMaxSizeError
        except TypeError:
            self.data = []

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.capacity() and self.full():
            raise QueueIsFullError
        self.data.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if not self.data:
            raise IndexError
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
        if not self.data:
            raise IndexError
        return self.data[0]

    def capacity(self):
        return self._maxsize

    def full(self):
        return True if self.size() == self.capacity() else False
