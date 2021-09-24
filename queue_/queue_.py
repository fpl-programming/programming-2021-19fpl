"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


class QueueIsTooLongError(Exception):
    """
    Error is raised when queue contains more elements than possible
    """

    def __str__(self):
        return 'The queue is too long'


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), max_elem_num: int = 15):
        self.max_elem_num = max_elem_num
        try:
            self.data = list(data)
        except TypeError:
            self.data = []
        else:
            if len(self.data) >= self.max_elem_num:
                raise QueueIsTooLongError

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        while len(self.data) >= self.max_elem_num:
            self.data.pop(0)
        return self.data.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if not self.data:
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
        if not self.data:
            raise IndexError
        return self.data[0]
