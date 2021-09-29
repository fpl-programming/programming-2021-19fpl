"""
Programming for linguists

Tests for SQueue class.
"""

import unittest

from queue_.queue_ import EmptyQueueError, QueueOverflowError
from queue_.squeue import SQueue
from stack.stack import Stack


class SQueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the stack-based implementation of Queue
    """

    def test_new_queue_stack_is_empty(self):
        """
        Create an empty SQueue.
        Test that its size is 0.
        """
        queue = SQueue()

        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_new_queue_from_stack(self):
        """
        Create a SQueue from stack.
        Test that no excessive casts are made and SQueue is still based on Stack
        """
        stack = Stack(range(10))
        queue = SQueue(stack)

        self.assertTrue(queue.in_stack, Stack)

    def test_get_queue_stack_element(self):
        """
        Get an element from a SQueue.
        Test that it is 1.
        """
        data = Stack([1, 2, 3, 4])
        queue = SQueue(data)

        self.assertEqual(queue.get(), 1)

    def test_put_queue_stack_element(self):
        """
        Put an element in SQueue.
        Test that its size is 1.
        """
        queue = SQueue()
        queue.put(1)

        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.top(), 1)

    def test_call_get_of_empty_queue_stack_raised_error(self):
        """
        Create an empty SQueue.
        Test that call of get function raises Assertion error
        """
        queue = SQueue()

        self.assertRaises(EmptyQueueError, queue.get)

    def test_queue_stack_capacity(self):
        """
        Create an empty SQueue and SQueue with another capacity.
        Test that function capacity returns correct data.
        """
        queue = SQueue()
        self.assertEqual(50, queue.capacity())

        queue_new = SQueue(capacity=25)
        self.assertEqual(25, queue_new.capacity())

    def test_queue_data_wrong_type(self):
        """
        Create an empty SQueue with the given bad inputs.
        Test that raises TypeError when gets inappropriate input data type.
        """
        bad_inputs = [4, '100', {}, float("inf")]

        for item in bad_inputs:
            self.assertRaises(TypeError, SQueue.__init__, data=item)

    def test_queue_capacity_wrong_type(self):
        """
        Create an empty SQueue with the given bad inputs.
        Test that raises TypeError when gets inappropriate input data type.
        """
        bad_inputs = [4, '100', {}, float("inf")]

        for item in bad_inputs:
            self.assertRaises(TypeError, SQueue.__init__, capacity=item)

    def test_queue_stack_full_ideal(self):
        """
        Create SQueue and fill the capacity.
        Test that at first the full function returns False, then True.
        """
        queue = SQueue(capacity=10)
        self.assertFalse(queue.full())

        for element in range(10, 1, -1):
            queue.put(element)

        self.assertTrue(queue.full())

    def test_put_overcapacity(self):
        """
        Create a full SQueue and put one more element.
        Test that call of put function raises Assertion error
        """
        stack = Stack([2, 3, 4, 5, 6, 7])
        queue = SQueue(stack, 6)

        self.assertRaises(QueueOverflowError, queue.put, 1)
