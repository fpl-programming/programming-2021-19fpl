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

    def __init__(self, data: Iterable = (), maxsize: int = 0):
        self.maxsize = maxsize
        if not isinstance(data, Iterable):
            self.data = []
        else:
            self.data = list(data)

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
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
        if not self.data:
            raise ValueError
        return self.data[0]

    def is_full(self):
        """
        Return whether queue_ has maxsize or not
        :return: True if the number of elements in the list is bigger than the maximum number.
                 False if the number of elements in the list is not bigger than the maximum number.
        """
        if self.size() > self.maxsize:
            return False
        return True
