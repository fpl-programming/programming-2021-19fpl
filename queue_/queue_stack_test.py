"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_stack import QueueStack


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue on Stack.
    """

    def test_new_queue_is_empty(self):
        """
        Create an empty Queue.
        Test that its size is 0.
        """
        queue_stack = QueueStack()
        self.assertTrue(queue_stack.empty())
        self.assertEqual(queue_stack.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue.
        Test that it is 1.
        """
        data = (1, 2, 3, 4)
        queue_stack = QueueStack(data)
        self.assertEqual(queue_stack.get(), data[0])

    def test_new_queue_from_tuple(self):
        """
        Create a Queue from an iterable object.
        Check that the size of queue_ equals to the size of the given tuple.
        """
        data = (1, 2, 3, 4)
        queue_stack = QueueStack(data)
        self.assertFalse(queue_stack.empty())
        self.assertEqual(queue_stack.size(), len(data))
        for value in data:
            test_value = queue_stack.get()
            self.assertEqual(test_value, value)
        self.assertTrue(queue_stack.empty())
        self.assertEqual(queue_stack.size(), 0)

    def test_new_queue_from_list(self):
        """
        Create a Queue from a list.
        Check that the size of queue equals to the size of the queue.
        Check that the top element of queue equals to the latest element of the list.
        """
        data = [1, 3, 5, 7, 2, 4]
        queue_stack = QueueStack(data)
        self.assertFalse(queue_stack.empty())
        self.assertEqual(queue_stack.size(), len(data))
        self.assertEqual(queue_stack.top(), data[0])

    def test_new_queue_from_generator(self):
        """
        Create a Queue_ from a generator.
        Test that its size equals to the number provided in the generator.
        """
        queue_stack = QueueStack(range(10))
        self.assertFalse(queue_stack.empty())
        self.assertEqual(queue_stack.size(), 10)
        self.assertEqual(queue_stack.top(), 0)

    def test_put_element(self):
        """
        Put an element in queue.
        Test that its size is 1.
        """
        queue_stack = QueueStack()
        queue_stack.put(1)
        self.assertFalse(queue_stack.empty())
        self.assertEqual(queue_stack.size(), 1)
        self.assertEqual(queue_stack.top(), 1)

    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of get function raises Assertion error.
        """
        queue_stack = QueueStack()
        self.assertRaises(IndexError, queue_stack.get)
