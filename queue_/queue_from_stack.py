# pylint: disable=duplicate-code
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


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Stack = Stack(), capacity_n_q: int = 0):
        if not isinstance(data, Stack):
            raise TypeError('Data is not Stack')
        if not isinstance(capacity_n_q, int):
            raise TypeError('Capacity is not int')
        self.data = data
        self.capacity_n_q = capacity_n_q
        if self.capacity_n_q and (self.size() > self.capacity_n_q):
            raise CapacityError('Number of elements in stack exceeds capacity')

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise CapacityError('Queue from stack is already full')
        self.data.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError('Queue is empty')
        tmp_stack = Stack()
        while not self.data.empty():
            tmp_stack.push(self.data.top())
            self.data.pop()
        last_el = tmp_stack.top()
        tmp_stack.pop()
        while not tmp_stack.empty():
            self.data.push(tmp_stack.top())
            tmp_stack.pop()
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
        tmp_stack = Stack()
        while not self.data.empty():
            tmp_stack.push(self.data.top())
            self.data.pop()
        last_el = tmp_stack.top()
        while not tmp_stack.empty():
            self.data.push(tmp_stack.top())
            tmp_stack.pop()
        return last_el

    def capacity(self) -> int:
        """
        Return the max number of elements in queue
        :return: Max number of elements in queue
        """
        return self.capacity_n_q

    def full(self) -> bool:
        """
        Return whether queue is full or not
        :return: True if queue is full.
                False if queue is not full
        """
        if self.size() == self.capacity() and self.capacity_n_q:
            return True
        return False
