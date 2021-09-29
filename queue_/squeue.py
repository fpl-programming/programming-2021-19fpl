"""
Programming for linguists
Implementation of the data structure "Queue" based on Stack
"""

from stack.stack import Stack
from queue_.queue_ import EmptyQueueError, QueueOverflowError, CapacityError


class SQueue:
    """
    Queue Data Structure Based On Stack
    """
    def __init__(self, data: Stack = Stack(), capacity: int = 50):
        if not isinstance(capacity, int):
            raise TypeError

        if data.size() > capacity:
            raise CapacityError

        self.in_stack = data
        self.out_stack = Stack()

        self._capacity = capacity

    def get(self):
        """
        Remove and return an item from SQueue
        """
        if self.in_stack.empty():
            raise EmptyQueueError

        self._traverse(self.in_stack, self.out_stack)

        top_item = self.out_stack.top()
        self.out_stack.pop()

        self._traverse(self.out_stack, self.in_stack)

        return top_item

    def top(self):
        """
        Return the element on the top of SQueue
        :return: the element that is on the top of SQueue
        """
        if self.in_stack.empty():
            raise EmptyQueueError

        self._traverse(self.in_stack, self.out_stack)

        top_item = self.out_stack.top()

        self._traverse(self.out_stack, self.in_stack)

        return top_item

    def put(self, element):
        """
        Add the element ‘element’ at the end of SQueue
        :param element: element to add to SQueue
        """
        if self.full():
            raise QueueOverflowError

        self.in_stack.push(element)

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if size of SQueue equals the capacity of SQueue.
                 False if the SQueue contains less elements.
        """
        return self.in_stack.size() == self._capacity

    def empty(self) -> bool:
        """
        Return whether SQueue is empty or not
        :return: True if SQueue does not contain any elements.
                 False if the SQueue contains elements
        """
        return self.in_stack.empty()

    def size(self) -> int:
        """
        Return the number of elements in SQueue
        :return: Number of elements in SQueue
        """
        return self.in_stack.size()

    def capacity(self):
        """
        Return the capacity of SQueue
        :return: the capacity (maximum size) of SQueue
        """
        return self._capacity

    @staticmethod
    def _traverse(in_stack: Stack, out_stack: Stack):
        """
        Traverses elements between in- and out-stack
        :param in_stack: stack to be popped
        :param out_stack: stack to be pushed
        """
        while not in_stack.empty():
            out_stack.push(in_stack.top())
            in_stack.pop()
