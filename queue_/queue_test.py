# pylint: disable=duplicate-code
"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_ import Queue_
from queue_.queue_ import TooManyElementsInQueueError, TypeCapacityError, QueueIsFullError


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

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
        Get an element from a queue.
        Test that it is 1.
        """
        data = (1, 2, 3, 4)
        queue = Queue_(data)
        self.assertEqual(queue.get(), data[0])

    def test_new_queue_from_tuple(self):
        """
        Create a Queue from an iterable object.
        Check that the size of queue_ equals to the size of the given tuple.
        """
        data = (1, 2, 3, 4)
        queue = Queue_(data)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        for value in data:
            test_value = queue.get()
            self.assertEqual(test_value, value)
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_new_queue_from_list(self):
        """
        Create a Queue from a list.
        Check that the size of queue equals to the size of the queue.
        Check that the top element of queue equals to the latest element of the list.
        """
        data = [1, 3, 5, 7, 2, 4]
        queue = Queue_(data)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        self.assertEqual(queue.top(), data[0])

    def test_new_queue_from_generator(self):
        """
        Create a Queue_ from a generator.
        Test that its size equals to the number provided in the generator.
        """
        queue = Queue_(range(10))
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 10)
        self.assertEqual(queue.top(), 0)

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

    def test_incorrect_capacity_raised_error(self):
        """
        Test that call of instantiation of class Queue_ with the not integer
        capacity raises the TypeCapacity error
        """
        self.assertRaises(TypeCapacityError, Queue_().__init__, [1, 2, 3], '5')

    def test_capacity_of_full_queue(self):
        """
        Create a full Queue.
        Test that if the queue is full, its size is equal to its capacity
        """
        queue = Queue_([1, 2, 3, 4, 5], 5)
        if queue.full():
            self.assertEqual(queue.size(), queue.capacity())

    def test_create_queue_with_too_many_elements(self):
        """
        Test that call of instantiation of class Queue_ with the number of elements
        larger than the capacity raises the TooManyElementsInQueue error
        """
        self.assertRaises(TooManyElementsInQueueError, Queue_().__init__, [1, 2, 3], 2)

    def test_call_put_of_full_queue_raised_error(self):
        """
        Create an empty Queue with the capacity.
        Put elements in the queue to make it full.
        Test that call of put function raises QueueIsFull error when the queue is full
        """
        queue = Queue_([], 4)
        self.assertTrue(queue.empty())
        for element in range(4):
            queue.put(element)
        self.assertEqual(queue.size(), 4)
        self.assertRaises(QueueIsFullError, queue.put, 1)
