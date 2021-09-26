"""

Implementation of the data structure "Queue" based on the data structure "Stack"
"""

from stack.stack import Stack
from typing import Iterable


class QueueFromStack(Stack):
    """
    Queue Data Structure based on Stack Data Structure
    """

    def __init__(self, data: Iterable = ()):
        super().__init__(data)
        self.stack = Stack(data)
        self.tmp_stack = Stack()
        self.queue_ = []
        while not self.stack.empty():
            self.tmp_stack.push(self.stack.pop())
        while not self.tmp_stack.empty():
            self.queue_.append(self.tmp_stack.pop())

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        self.queue_.append(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if not self.queue_:
            raise IndexError
        return self.queue_.pop(0)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.queue_

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.queue_)

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        if not self.queue_:
            raise IndexError
        return self.queue_[0]
