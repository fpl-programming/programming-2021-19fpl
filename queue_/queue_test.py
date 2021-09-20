"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue import Full

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

    def test_new_queue_with_max_size(self):
        """
        Create a Queue_ with max_size.
        Test that its field max_size is filled correctly
        """
        queue = Queue_(max_size=5)
        self.assertEqual(queue.max_size, 5)

    def test_put_element_into_full_queue(self):
        """
        Put element into a queue that is already full.
        Test that call of put function raises Full exception
        """
        queue = Queue_([1, 2, 3, 4, 5], 5)
        self.assertRaises(Full, queue.put, 6)

    def test_limited_queue_is_full(self):
        """
        Create a full limited Queue_.
        Test that call of full function returns True
        """
        queue = Queue_([1, 2, 3, 4, 5], 5)
        self.assertTrue(queue.full())
        queue.get()
        self.assertFalse(queue.full())

    def test_infinite_queue_is_not_full(self):
        """
        Create a nonempty infinite Queue_.
        Test that call of full function returns False
        """
        queue = Queue_([1, 2, 3, 4, 5])
        self.assertFalse(queue.full())
