"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_ import Queue_, EmptyQueueError, QueueOverflowError


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
        self.assertRaises(EmptyQueueError, queue.get)

    def test_put_overcapacity(self):
        """
        Create a full Queue and put one more element.
        Test that call of put function raises Assertion error
        """
        queue = Queue_([2, 3, 4, 5, 6], 5)
        self.assertRaises(QueueOverflowError, queue.put, 1)

    def test_queue_capacity(self):
        """
        Create an empty Queue, then Queue with another capacity.
        Test that function capacity returns correct data.
        """
        queue = Queue_()
        self.assertEqual(50, queue.capacity())
        queue_new = Queue_(capacity=25)
        self.assertEqual(25, queue_new.capacity())

    def test_auto_size(self):
        """
        Create a Queue with automatically determined size.
        Test that the size of Queue equals the size of data.
        """
        queue = Queue_([10, 100, 1000, 10000])
        self.assertEqual(queue.size(), 4)
