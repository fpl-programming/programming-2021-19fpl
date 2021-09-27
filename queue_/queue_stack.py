"""
Programming for linguists

Implementation of the data structure "Queue on Stack"
"""
from stack.stack import Stack


class QueueStack(Stack):
    """
    Queue on Stack Data Structure
    """

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_stack
        :param element: element to add to queue_stack
        """
        self.push(element)

    def get(self):
        """
        Remove and return an item from queue_stack
        """
        if self.empty():
            raise IndexError('Queue is empty.')

        new_stack = Stack()
        while self.data:
            elem = Stack.top(self)
            new_stack.push(elem)
            self.pop()

        res = Stack.top(new_stack)
        new_stack.pop()

        while new_stack.data:
            elem = Stack.top(new_stack)
            self.push(elem)
            new_stack.pop()
        return res

    def top(self):
        """
        Return the element on the top of queue_stack
        :return: the element that is on the top of queue_stack
        """
        return self.data[0]
