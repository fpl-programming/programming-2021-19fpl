"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_from_stack import Queue_
from queue_.queue_ import QueueIsTooLongError
from stack.stack import Stack


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue from stack
    """

    def test_new_queue_is_empty(self):
        """
        Create an empty Queue.
        Test that its size is 0.
        """
        queue = Queue_(Stack())
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue.
        Test that it is 1.
        """
        data = Stack((1, 2, 3, 4, 5))
        queue = Queue_(data)
        self.assertEqual(queue.get(), 1)

    def test_put_element(self):
        """
        Put an element in queue.
        Test that its size is 3.
        """
        queue = Queue_(Stack((3, 2)))
        queue.put(1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.top(), 3)

    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of get function raises Assertion error
        """
        queue = Queue_(Stack())
        self.assertRaises(IndexError, queue.get)

    def test_create_too_long_queue_raised_error(self):
        """
        Test that call of instantitation of class Queue_
        with too many elements raises custom QueueIsTooLongError
        """
        self.assertRaises(QueueIsTooLongError, Queue_().__init__, Stack([1, 2, 3, 4, 5, 6]), 5)

    def test_call_put_of_too_long_queue_added_elements(self):
        """
        Create a Queue with maximum number of elements.
        Test that call of put function deletes the first element
        in order to put a new element without raising an error
        """
        queue = Queue_(Stack([1, 2, 3, 4, 5]), 5)
        queue.put(6)
        self.assertEqual(queue.size(), 5)
        self.assertEqual(queue.top(), 2)
        self.assertEqual(queue.data.data, [2, 3, 4, 5, 6])
