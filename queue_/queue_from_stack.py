"""
Programming for linguists

Implementation of the data structure "Queue" from stack
"""

from queue_.queue_ import FullQueue
from stack.stack import Stack


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure from stack
    """

    def __init__(self, data: Stack = Stack(), max_size: int = 0):
        if max_size and len(data.data) > max_size:
            data.data = data.data[:max_size]
        self.data = data
        self.max_size = max_size

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise FullQueue

        self.data.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        return self.data.data.pop(0)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return self.data.empty()

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return self.data.size()

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        return self.data.data[0]

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if the queue_ is not full
        """
        if not self.max_size:
            print('the queue size is infinite')

        elif self.max_size and self.size() == self.max_size:
            return True

        return False
