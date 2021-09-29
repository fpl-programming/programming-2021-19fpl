"""
Programming for linguists

Implementation of the data structure "Queue" from Stack structure
"""

from stack.stack import Stack
from queue_.queue_ import QueueIsTooLongError


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Stack = Stack(), max_elem_num: int = 15):
        self.max_elem_num = max_elem_num

        try:
            self.data = data
        except TypeError:
            self.data = Stack([])
        else:
            if self.data.size() > self.max_elem_num:
                raise QueueIsTooLongError

    @staticmethod
    def get_reversed_stack(data: list):
        """
        Method returns the reversed stack
        """
        tmp_stack = Stack()
        new_data = Stack(data)

        while new_data.size() != 0:
            tmp_stack.push(new_data.pop())
        return tmp_stack

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        tmp_stack = Queue_.get_reversed_stack(self.data.data)

        while tmp_stack.size() >= self.max_elem_num:
            tmp_stack.pop()

        self.data = Queue_.get_reversed_stack(tmp_stack.data)
        return self.data.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.data.empty():
            raise IndexError

        tmp_stack = Queue_.get_reversed_stack(self.data.data)
        needed_value = tmp_stack.top()
        tmp_stack.pop()
        self.data = Queue_.get_reversed_stack(tmp_stack.data)
        return needed_value

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
        if not self.data:
            raise IndexError

        tmp_stack = Queue_.get_reversed_stack(self.data.data)
        return tmp_stack.top()
