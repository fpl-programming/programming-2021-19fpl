"""

Implementation of the data structure "Queue" based on the data structure "Stack"
"""

from typing import Iterable
from stack.stack import Stack


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
        self.is_queue = True

    def queue_to_stack(self):
        """
        Turns queue_ back to stack
        """
        if not self.is_queue:
            raise TypeError
        while self.queue_:
            self.stack.push(self.queue_.pop(0))
        self.is_queue = False

    def empty(self) -> bool:
        """
        Return whether queue_ or stack is empty or not
        :return: True if queue_/stack does not contain any elements.
                 False if queue_/stack contains elements
        """
        if not self.is_queue:
            self.stack.empty()
        return not self.queue_

    def get(self):
        """
        Remove and return an item from queue_ or stack
        """
        if not self.is_queue:
            if not self.stack:
                raise IndexError
            self.stack.pop()
        if not self.queue_:
            raise IndexError
        return self.queue_.pop(0)

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_ or at the top of stack
        :param element: element to add to queue_ or to stack
        """
        if self.is_queue:
            self.queue_.append(element)
        self.stack.push(element)

    def top(self):
        """
        Return the available element depending on current data structure.
        :return: the element that is on the top of queue_ or stack
        """
        if not self.is_queue:
            if not self.stack:
                raise IndexError
            self.stack.top()
        if not self.queue_:
            raise IndexError
        return self.queue_[0]
