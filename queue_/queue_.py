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

    def __init__(self, data: Iterable = (), limit: int = 10):
        self.data = list(data)

        if not isinstance(limit, int):
            raise TypeError('Only numbers are allowed')
        self._limit = limit

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise IndexError('Queue is full')
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
        return self.data[0]

    def limit(self):
        """
        Return the limit of queue_
        :return: the maximum size (limitation) of queue_
        """
        return self._limit

    def full(self):
        """
        Return bool value is our queque_ full or not
        :return: True: queue limit reached
                 False: there is still free space in the queue
        """
        if self.size() == self._limit:
            return True
        return False
