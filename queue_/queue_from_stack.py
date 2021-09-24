"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from stack.stack import Stack


class CapacityError(Exception):
    """
    Custom Error
    Raises when number of elements exceeds capacity
    """
    pass


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Stack = Stack(), capacity_n: int = 40):
        if not isinstance(data, Stack):
            raise TypeError('Data is not Stack')
        if not isinstance(capacity_n, int):
            raise TypeError('Capacity is not int')
        self.data = data
        self.capacity_n = capacity_n
        self.storage = Stack()
        if self.size() > self.capacity_n:
            raise CapacityError('Number of elements exceeds capacity')

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise CapacityError('Queue is already full')
        self.data.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError('Queue is empty')
        while not self.data.empty():
            self.storage.push(self.data.top())
            self.data.pop()
        last_el = self.storage.top()
        self.storage.pop()
        while not self.storage.empty():
            self.data.push(self.storage.top())
            self.storage.pop()
        return last_el

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
        if self.empty():
            raise IndexError('Queue is empty')
        while not self.data.empty():
            self.storage.push(self.data.top())
            self.data.pop()
        last_el = self.storage.top()
        while not self.storage.empty():
            self.data.push(self.storage.top())
            self.storage.pop()
        return last_el

    def capacity(self) -> int:
        """
        Return the max number of elements in queue_
        :return: Max number of elements in queue_
        """
        return self.capacity_n

    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                False if queue_ is not full
        """
        if self.size() == self.capacity():
            return True
        return False
