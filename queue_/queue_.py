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

    def __init__(self, data: Iterable = (), max_size=9):
        self.data = list(data)
        self.max_size = max_size

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if queue_ does is full.
        False if the queue_ can contain more elements
        """
        return True if len(self.data) == self.max_size else False

    def change_max_size(self, value: int):
        """
        Changes max_size of queue_
        :param value: value to be max_size of queue_
        """
        if not isinstance(value, int) and value > 0:
            raise ValueError
        else:
            self.max_size = value

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if not self.full():
            self.data.append(element)
        else:
            raise ValueError('the queue_ is full')

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
        return self.data[-1]
