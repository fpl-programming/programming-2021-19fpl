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

    def __init__(self, data: Iterable = (), max_size: int = float("inf")):
        try:
            self.data = list(data)
            if len(self.data) > max_size:
                raise ValueError
            self.max_size = max_size
        except TypeError as exception:
            raise ValueError from exception

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if len(self.data) + 1 > self.max_size:
            raise ValueError
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

    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if number of elements in queue_ reached max
                 False if there is room in queue_
        """
        return len(self.data) == self.max_size

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.data)

    def get_max_size(self) -> int:
        """
        Return the max possible number of elements in queue_
        :return: Max number of elements in queue_
        """
        return self.max_size

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        return self.data[0]
