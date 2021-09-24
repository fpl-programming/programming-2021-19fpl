"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


class TooManyElementsInQueueError(Exception):
    """
    Custom error
    Error is raised when a number of elements in queue_ is larger than its capacity
    """
    def __str__(self):
        return "There are too many elements in the queue_"


class QueueIsFullError(Exception):
    """
    Custom error
    Error is raised when a new element cannot be added
    due to the lack of the space in queue_
    """
    def __str__(self):
        return "The queue_ is full"


class TypeCapacityError(Exception):
    """
    Custom error
    Error is raised capacity is not int
    """

    def __str__(self):
        return "The capacity is not int"


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (),  capacity: int = 0):
        if not isinstance(capacity, int):
            raise TypeCapacityError
        self._capacity = capacity

        try:
            listed_data = list(data)
        except TypeError:
            self.data = []
        else:
            if (listed_data and self._capacity) and (len(listed_data) > self._capacity):
                raise TooManyElementsInQueueError
            self.data = listed_data

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise QueueIsFullError

        return self.data.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
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
        if self.empty():
            raise IndexError
        return self.data[0]

    def capacity(self):
        """
        Return the capacity of queue_
        :return: the number of elements which can be in queue_
        """
        return self._capacity

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if the queue_ is not full
        """
        if not self._capacity:
            return False  # if capacity == 0, the queue_ is infinite

        if self._capacity and self.size() == self._capacity:
            return True

        return False
