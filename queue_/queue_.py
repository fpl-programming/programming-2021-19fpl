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

    def __init__(self, data: Iterable = (), maxlen: int = None):
        self.maxlen = maxlen

        self.data = list(data)
        if self.maxlen and self.size() > self.maxlen:
            # pylint: disable=invalid-unary-operand-type
            self.data = self.data[-maxlen:]

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.maxlen and self.full():
            self.get()
            self.data.append(element)
        else:
            self.data.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError('Queue is empty.')
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
        if self.empty():
            raise IndexError('Queue is empty.')
        return self.data[0]

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if size of queue_ equals maxlen.
                 False if the queue_ isn't full
        """
        if self.size() < self.maxlen:
            return False
        return True
