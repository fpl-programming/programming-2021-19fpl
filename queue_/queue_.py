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
        pass

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """

    def get(self):
        """
        Remove and return an item from queue_
        """

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
