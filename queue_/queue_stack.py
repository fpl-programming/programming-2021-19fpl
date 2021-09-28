"""
Programming for linguists

Implementation of the data structure "QueueStack"
"""

from typing import Iterable


class QueueStack:
    """
    Queue Data Structure from Stack
    """

    def __init__(self, data: Iterable = None, queue_size: int = 'no_info'):
        if data and isinstance(data, list):
            self.stack = data
        elif isinstance(data, (int, float)):
            self.stack = [data]
        elif data:
            self.stack = list(data)
        elif not data:
            self.stack = []
        else:
            raise TypeError
        if isinstance(queue_size, int):
            self.queue_size = queue_size
        elif queue_size == 'no_info':
            self.queue_size = len(self.stack) if len(self.stack) > 0 else len(self.stack) + 1
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

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        self.stack.append(element)

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.stack:
            return self.stack[-1]
        raise ValueError

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.stack)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not self.stack
