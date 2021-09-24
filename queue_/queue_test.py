"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_ import Queue_, IncorrectMaxSizeError, ExceededMaxSizeError, QueueIsFullError


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

    def test_queue_is_empty_with_non_iterable_data(self):
        """
        Create a Queue of noniterable data.
        Test that its size is 0.
        """
        non_iterable_data = [None, 5, 1.09, True, Queue_(), False, 0, 1]
        for data in non_iterable_data:
            queue = Queue_(data)
            self.assertTrue(queue.empty())
            self.assertEqual(queue.size(), 0)

    def test_incorrect_maxsize_raised_error(self):
        """
        Test that an incorrect type of a maxsize parameter raises a ExceededMaxSizeError.
        """
        data = [1, None, 3, 5, 7, 'a', 2, 4, False]
        incorrect_maxsize = [None, 7.56, True, Queue_(), False, ['string'], {'b': 2}]
        for maxsize in incorrect_maxsize:
            self.assertRaises(IncorrectMaxSizeError, Queue_, data, maxsize)

    def test_exceeded_maxsize_raised_error(self):
        """
        Create a Queue with a size that is bigger than capacity.
        Test that creation of a Queue raises a ExceededMaxSizeError.
        """
        data = [1, None, 3, 5, 7, 'a', 2, 4, False]
        self.assertRaises(ExceededMaxSizeError, Queue_, data, 3)

    def test_new_queue_is_full(self):
        """
        Create a Queue with a size equal to capacity.
        Test that Queue is full.
        """
        data = [1, None, 3, 5, 7, 'a']
        queue = Queue_(data, 6)
        self.assertEqual(queue.size(), queue.capacity())
        self.assertTrue(queue.full())

    def test_call_put_for_full_queue_raised_error(self):
        """
        Create a Queue with a size equal to capacity.
        Test that call of put function raises a QueueIsFullError.
        """
        data = [1, None, 3, 5, 7, 'a']
        queue = Queue_(data, 6)
        self.assertRaises(QueueIsFullError, queue.put, 'new_element')
