"""
Programming for linguists

Implementation of the data structure "Queue" based on data structure "Stack"
"""

from typing import Iterable
# from stack.stack import Stack
from stack.stack import Stack


# pylint: disable=invalid-name
class Queue_(Stack):
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), max_size: int = float("inf")):
        super().__init__(data)
        if len(data) > max_size:
            raise ValueError
        self.max_size = max_size

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if len(self.stack) + 1 > self.max_size:
            raise ValueError
        self.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        return self.stack.pop(0)

    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if number of elements in queue_ reached max
                 False if there is room in queue_
        """
        return len(self.stack) == self.max_size

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
        return self.stack[0]
