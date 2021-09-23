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

    def __init__(self, data: Iterable = (), capacity: int = 50):
        self.data = list(data)
        self.capacity = capacity

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise IndexError
        self.data.append(element)

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
        return self.data[0]

    def capacity(self):
        """
        Return the capacity of queue_
        :return: the maximum length (capacity) of queue_
        """
        return self.capacity

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if size of queue_ equals the capacity of queue_.
                 False if the queue_ contains less elements.
        """
        if self.size() == self.capacity:
            return True
        return False
