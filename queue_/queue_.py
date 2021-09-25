# pylint: disable=duplicate-code
"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


class CapacityError(Exception):
    """
    Custom Error
    Raises when number of elements exceeds capacity
    """


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), capacity_n: int = 0):
        if not isinstance(capacity_n, int):
            raise TypeError('Capacity is not int')
        self.capacity_n = capacity_n
        try:
            self.data = list(data)
        except TypeError:
            self.data = []
        else:
            if self.capacity_n and (self.size() > self.capacity_n):
                raise CapacityError('Number of elements exceeds capacity')

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise CapacityError('Queue is already full')
        self.data.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError('Queue is empty')
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
        if self.empty():
            raise IndexError('Queue is empty')
        return self.data[0]

    def capacity(self) -> int:
        """
        Return the max number of elements in queue_
        :return: Max number of elements in queue_
        """
        return self.capacity_n

    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                False if queue_ is not full
        """
        if self.size() == self.capacity() and self.capacity_n:
            return True
        return False
