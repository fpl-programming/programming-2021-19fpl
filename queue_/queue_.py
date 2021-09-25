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

    def __init__(self, data: Iterable = (), capacity: int = 20):
        self._capacity = capacity

        try:
            self.queue = list(data)

        except TypeError:
            self.queue = []

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise IndexError
        self.queue.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError
        return self.queue.pop(0)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.queue

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.queue)

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        if self.empty():
            raise ValueError
        return self.queue[0]

    def capacity(self):
        """
        Return the capacity of queue_
        :return: the maximum length in queue_
        """
        return self._capacity

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if size of queue_ equals the capacity of queue_.
                 False if the queue_ contains less elements.
        """
        return self.size() == self._capacity
