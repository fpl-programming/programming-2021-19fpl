"""
Programming for linguists

Implementation of the data structure "Queue on stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        self.data = list(data) if data is not None else []

    def __str__(self):
        """
        return string representation of the object
        """
        str_repr = ''
        while self.data:
            str_repr += self.top()
            self.pop()
        return str_repr

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        self.data.append(element)

    def pop(self):
        """
        Delete the element on the top of stack
        """
        if not self.data:
            raise ValueError
        self.data.pop()

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.data:
            return self.data[-1]
        raise ValueError

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not bool(self.data)

    def print(self):
        """
        Print elements one by one in a column
        """
        for item in str(self):
            print(item)

    def clean_stack(self):
        """
        delete all elements
        """
        self.data = []


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = ()):
        self.data = Stack(data) if data is not None else Stack()

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        self.data.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.data.empty():
            raise IndexError

        temp_data = Stack()
        while self.data.size() > 1:
            temp_data.push(self.data.top())
            self.data.pop()
        elem = self.data.top()
        self.data.pop()

        while temp_data.size():
            self.data.push(temp_data.top())
            temp_data.pop()
        return elem

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
        if self.data.empty():
            raise IndexError

        temp_data = Stack()
        while self.data.size():
            temp_data.push(self.data.top())
            self.data.pop()
        elem = temp_data.top()

        while temp_data.size():
            self.data.push(temp_data.top())
            temp_data.pop()
        return elem
