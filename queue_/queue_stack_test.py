"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_stack import QueueStack


class QueueStackTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_new_queue_is_empty(self):
        """
        Create an empty QueueStack.
        Test that its size is 0.
        """
        queue_stack = QueueStack()
        self.assertTrue(queue_stack.empty())
        self.assertEqual(queue_stack.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue_stack.
        Test that it is 1.
        """
        data = (1, 2, 3, 4)
        queue_stack = QueueStack(data)
        self.assertEqual(queue_stack.top(), data[0])

    def test_new_queue_from_tuple(self):
        """
        Create a QueueStack from an iterable object.
        Check that the size of queue_stack equals to the size of the given tuple.
        """
        data = (1, 2, 3, 4)
        queue_stack = QueueStack(data)
        self.assertFalse(queue_stack.empty())
        self.assertEqual(queue_stack.size(), len(data))
        for value in data:
            test_value = queue_stack.top()
            queue_stack.pop()
            self.assertEqual(test_value, value)
        self.assertTrue(queue_stack.empty())
        self.assertEqual(queue_stack.size(), 0)

    def test_new_queue_from_list(self):
        """
        Create a QueueStack from a list.
        Check that the size of queue_stack equals to the size of the queue.
        Check that the top element of queue equals to the latest element of the list.
        """
        data = [1, 3, 5, 7, 2, 4]
        queue_stack = QueueStack(data)
        self.assertFalse(queue_stack.empty())
        self.assertEqual(queue_stack.size(), len(data))
        self.assertEqual(queue_stack.top(), data[0])

    def test_new_queue_from_generator(self):
        """
        Create a QueueStack from a generator.
        Test that its size equals to the number provided in the generator.
        """
        queue_stack = QueueStack(range(10))
        self.assertFalse(queue_stack.empty())
        self.assertEqual(queue_stack.size(), 10)
        self.assertEqual(queue_stack.top(), 0)

    def test_put_element(self):
        """
        Put an element in queue_stack.
        Test that its size is 1.
        """
        queue = QueueStack()
        queue.push(1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.top(), 1)

    def test_merge_order(self):
        """
        Create two QueueStack.
        Test the top of changed Stack
        """
        stack_1 = QueueStack([1, 2, 3])
        stack_2 = QueueStack([4, 5, 6])
        stack_1.merge(stack_2)
        self.assertEqual(stack_1.top(), 1)




