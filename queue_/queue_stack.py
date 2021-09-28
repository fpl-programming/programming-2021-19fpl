"""
Programming for linguists

Implementation of the data structure "QueueStack"
"""

from typing import Iterable
from stack.stack import Stack


class QueueStack(Stack):
    """
    Queue Data Structure from Stack
    """

    def __init__(self, data: Iterable = None, queue_size: int = 'no_info'):
        super().__init__(data)
        if isinstance(queue_size, int):
            self.queue_size = queue_size
        elif queue_size == 'no_info':
            self.queue_size = len(self.stack) if len(self.stack) > 0 else len(self.stack) + 1
        else:
            raise TypeError
        self.stack = self.stack[::-1][:self.queue_size]

    def get(self):
        """
        Remove and return an item from queue_stack
        """
        return self.stack.pop()

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_stack
        :param element: element to add to queue_stack
        """
        if len(self.stack) == self.queue_size:
            raise ValueError
        self.stack.insert(0, element)
