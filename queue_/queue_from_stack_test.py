"""
Programming for linguists

Tests for Queue from stack class.
"""

import unittest

from stack.stack import Stack
from queue_.queue_from_stack import Queue_
from queue_.queue_ import TooManyElementsInQueueError, QueueIsFullError


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_data_is_stack(self):
        """
        Test that the data in the queue has Stack type
        """
        queue = Queue_(Stack([1, 2, 3]))
        self.assertTrue(isinstance(queue.data, Stack))

    def test_create_queue_not_from_stack(self):
        """
        Tests that call of instantiation of class Queue_ with not a Stack data
        raises TypeError
        """
        self.assertRaises(TypeError, Queue_().__init__, [1, 2, 3])

    def test_new_queue_is_empty(self):
        """
        Create an empty Queue from stack.
        Test that its size is 0.
        """
        queue = Queue_(Stack())
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue.
        Test that it is 0.
        """
        data = Stack((0, 1, 2, 3, 4))
        queue = Queue_(data)
        self.assertEqual(queue.get(), 0)

    def test_put_element(self):
        """
        Put an element in queue.
        Test that its size is 1.
        """
        queue = Queue_(Stack())
        queue.put(4)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.top(), 4)

    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of get function raises Assertion error
        """
        queue = Queue_(Stack())
        self.assertRaises(IndexError, queue.get)

    def test_capacity_of_full_queue(self):
        """
        Create a full Queue.
        Test that if the queue is full, its size is equal to its capacity
        """
        queue = Queue_(Stack([1, 2, 3]), 3)
        if queue.full():
            self.assertEqual(queue.size(), queue.capacity())

    #@unittest.skip
    def test_create_queue_with_too_many_elements(self):
        """
        Test that call of instantiation of class Queue_ with the number of elements
        larger than the capacity raises the TooManyElementsInQueue error
        """
        self.assertRaises(TooManyElementsInQueueError, Queue_().__init__, Stack([1, 2, 3, 4]), 3)

    #@unittest.skip
    def test_call_put_of_full_queue_raised_error(self):
        """
        Create an empty Queue with the capacity.
        Put elements in the queue to make it full.
        Test that call of put function raises QueueIsFull error when the queue is full
        """
        queue = Queue_(Stack(), 5)
        self.assertTrue(queue.empty())
        for element in range(5):
            queue.put(element)
        self.assertEqual(queue.size(), 5)
        self.assertRaises(QueueIsFullError, queue.put, 1)

    def test_infinite_queue_is_not_full(self):
        """
        Create an infinite queue.
        Test that the call of full function is False
        """
        queue = Queue_(Stack([1, 3, 4]))
        self.assertFalse(queue.full())
        queue.put(6)
        self.assertFalse(queue.full())
