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

    def __init__(self, data: Iterable = ()):
        if isinstance(data, list):
            self.data = data
        elif isinstance(data, range) or isinstance(data, tuple):
            self.data = list(data)
        else:
            self.data = []

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
        if len(self.data) == 0:
            raise IndexError
        return self.data.pop(0)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        if self.data:
            return False
        return True

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
        if len(self.data) == 0:
            raise ValueError
        return self.data[0]

