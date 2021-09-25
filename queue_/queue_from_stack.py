"""
Programming for linguists

Implementation of the data structure "Queue" from stack
"""

from queue_.queue_ import FullQueue, InfiniteQueue
from stack.stack import Stack


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure from stack
    """

    def __init__(self, data: Stack = Stack(), max_size: int = 0):
        if max_size and len(data.data) > max_size:
            data.data = data.data[:max_size]
        self.in_stack = data
        self.out_stack = Stack()
        self.max_size = max_size

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if not self.max_size or not self.full():
            self.in_stack.push(element)
        else:
            raise FullQueue

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.in_stack.empty():
            raise IndexError

        while self.in_stack.size() != 1:
            self.out_stack.push(self.in_stack.top())
            self.in_stack.pop()

        top_element = self.in_stack.top()
        self.in_stack.pop()

        while not self.out_stack.empty():
            self.in_stack.push(self.out_stack.top())
            self.out_stack.pop()

        return top_element

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return self.in_stack.empty()

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return self.in_stack.size()

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        if self.in_stack.empty():
            raise IndexError

        while self.in_stack.size() != 1:
            self.out_stack.push(self.in_stack.top())
            self.in_stack.pop()

        top_element = self.in_stack.top()

        while not self.out_stack.empty():
            self.in_stack.push(self.out_stack.top())
            self.out_stack.pop()

        return top_element

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if the queue_ is not full
        """
        if not self.max_size:
            raise InfiniteQueue

        elif self.max_size and self.size() == self.max_size:
            return True

        return False
