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

    def __init__(self, data: Iterable = (), queue_size: int = 'no_info'):
        if data and isinstance(data, list):
            self.queue = data
        elif isinstance(data, (int, float)):
            self.queue = [data]
        elif data:
            self.queue = list(data)
        elif not data:
            self.queue = []
        if isinstance(queue_size, int):
            self.queue_size = queue_size
        elif queue_size == 'no_info':
            self.queue_size = len(self.queue) if len(self.queue) > 0 else len(self.queue) + 1
        else:
            raise TypeError
        self.queue = self.queue[:self.queue_size]

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        self.queue.append(element)
        if len(self.queue) > self.queue_size:
            self.get()

    def get(self):
        """
        Remove and return an item from queue_stack
        """
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
        return self.queue[0]
