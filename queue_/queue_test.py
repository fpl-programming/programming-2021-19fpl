"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_ import Queue_


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

    def test_call_top_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of top function raises Index error
        """
        queue = Queue_()
        self.assertRaises(IndexError, queue.top)

    def test_new_queue_is_full(self):
        """
        Create a Queue from data.
        Set maximum size equal to the data size.
        Test that the Queue is full
        """
        data = [1, 3, 5, 7, 2, 4]
        queue = Queue_(data, len(data))
        self.assertFalse(queue.empty())
        self.assertTrue(queue.full())

    def test_max_size(self):
        """
        Create an empty Queue with defined maximum size.
        Test that call of max_size function returns the maximum size.
        """
        max_size = 1
        queue = Queue_([], max_size)
        self.assertEqual(queue.max_size(), max_size)

    def test_max_size_error(self):
        """
        Test that creating a Queue from data exceeding the defined max size raises Value error.
        """
        data = [1, 2, 3]
        max_size = 1
        self.assertRaises(ValueError, Queue_, data, max_size)

    def test_put_element_in_full_queue(self):
        """
        Create a Queue from a list with its maximum size equal to the data size.
        Test that call of put function raises Value error
        """
        data = [1, 3, 5, 7, 2, 4]
        queue = Queue_(data, len(data))
        self.assertRaises(ValueError, queue.put, 'element to put')
