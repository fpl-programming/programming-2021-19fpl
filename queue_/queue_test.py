"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_ import Queue_
# from queue_ import Queue_


# @unittest.skip
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

    def test_max_size(self):
        """
        Create a Queue_ with a definite max_size
        Test that it returns max size correctly
        """
        queue = Queue_([1, 2, 3, 4], 10)
        self.assertEqual(queue.get_max_size(), 10)

    def test_new_queue_is_full(self):
        """
        Create various instances of Queue.
        Test whether it is possible to know is they are full
        """
        queue = Queue_([1, 2, 3], 3)
        self.assertEqual(queue.full(), True)

        queue = Queue_([1, 2, 3])
        self.assertEqual(queue.full(), False)

        queue = Queue_([1, 2, 3], 5)
        self.assertEqual(queue.full(), False)

    def test_incorrect_input_not_iterable_raised_error(self):
        """
        Create instances of Queue with non-iterable data
        Test that initialisation raises Type error
        """
        for data in (True, 1, float('inf'), 4.0):
            self.assertRaises(ValueError, Queue_, data)

    def test_incorrect_input_too_long_raised_error(self):
        """
        Create instances of Queue with mismatching data length and max size
        Test that initialisation raises Value error
        """
        self.assertRaises(ValueError, Queue_, [1, 2, 3, 4, 5], 1)

    def test_put_too_many_elements_raised_error(self):
        """
        Create instances of Queue
        Put in so many elements it exceeds max size
        Test that call of put function raises Value error
        """
        for max_size in [1, 4, 6, 600]:
            queue = Queue_([True] * max_size, max_size)
            self.assertRaises(ValueError, queue.put, True)
