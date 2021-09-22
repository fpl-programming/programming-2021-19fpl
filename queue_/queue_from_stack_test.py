"""
Programming for linguists

Tests for Queue from stack class.
"""

import unittest

from queue import Full

from queue_from_stack import Queue_
from stack import Stack


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue from stack
    """

    def test_queue_data_is_stack(self):
        """
        Create an empty Queue from stack.
        Test that its data field type is Stack.
        """
        stack = Stack([1, 2, 3, 4, 5])
        queue = Queue_(stack)
        self.assertTrue(isinstance(queue.data, Stack))

    def test_new_queue_is_empty(self):
        """
        Create an empty Queue.
        Test that its size is 0.
        """
        queue = Queue_()
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue created from stack.
        Test that it is 1.
        """
        stack = Stack([1, 2, 3, 4])
        queue = Queue_(stack)
        self.assertEqual(queue.get(), 1)

    def test_put_element(self):
        """
        Put an element in queue.
        Test that its size is 1.
        """
        queue = Queue_()
        queue.put(1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.top(), 1)

    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of get function raises Assertion error
        """
        queue = Queue_()
        self.assertRaises(IndexError, queue.get)

    def test_new_queue_with_max_size(self):
        """
        Create a Queue_ with max_size.
        Test that its field max_size is filled correctly
        """
        queue = Queue_(max_size=5)
        self.assertEqual(queue.max_size, 5)

    def test_put_element_into_full_queue(self):
        """
        Put element into a queue (created from stack) that is already full.
        Test that call of put function raises Full exception
        """
        stack = Stack([1, 2, 3, 4, 5])
        queue = Queue_(stack, 5)
        self.assertRaises(Full, queue.put, 6)
        queue.get()
        queue.put(6)
        self.assertEqual([2, 3, 4, 5, 6], queue.data.data)

    def test_limited_queue_is_full(self):
        """
        Create a full limited Queue_ from stack.
        Test that call of full function returns True
        """
        stack = Stack([1, 2, 3, 4, 5])
        queue = Queue_(stack, 5)
        self.assertTrue(queue.full())
        queue.get()
        self.assertFalse(queue.full())

    def test_infinite_queue_is_not_full(self):
        """
        Create a nonempty infinite Queue_ from stack.
        Test that call of full function returns False
        """
        stack = Stack([1, 2, 3, 4, 5])
        queue = Queue_(stack)
        self.assertFalse(queue.full())
