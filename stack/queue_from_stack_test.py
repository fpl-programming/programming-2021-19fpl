# pylint: disable=duplicate-code
"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from stack.queue_from_stack import Queue_


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_new_queue_is_empty(self):
        """
        Create an empty Queue.
        Test that its size is 0.
        """
        que = Queue_()
        self.assertEqual(que.size(), 0)
        self.assertTrue(que.empty())

    def test_get_element(self):
        """
        Get an element from a queue.
        Test that it is 1.
        """
        data = (1, 2, 3)
        que = Queue_(data)
        self.assertEqual(que.get(), data[0])

    def test_new_queue_from_tuple(self):
        """
        Create a Queue from an iterable object.
        Check that the size of queue_ equals to the size of the given tuple.
        """
        data = (1, 2, 3, 4)
        que = Queue_(data)
        self.assertFalse(que.empty())
        self.assertEqual(que.size(), len(data))
        for value in data:
            test_value = que.get()
            self.assertEqual(test_value, value)
        self.assertTrue(que.empty())
        self.assertEqual(que.size(), 0)

    def test_new_queue_from_list(self):
        """
        Create a Queue from a list.
        Check that the size of queue equals to the size of the queue.
        Check that the top element of queue equals to the latest element of the list.
        """
        data = [1, 3, 5, 7, 2, 4]
        que = Queue_(data)
        self.assertFalse(que.empty())
        self.assertEqual(que.size(), len(data))
        self.assertEqual(que.top(), data[0])

    def test_new_queue_from_generator(self):
        """
        Create a Queue_ from a generator.
        Test that its size equals to the number provided in the generator.
        """
        que = Queue_(range(10))
        self.assertEqual(que.top(), 0)
        self.assertFalse(que.empty())
        self.assertEqual(que.size(), 10)
    def test_put_element(self):
        """
        Put an element in queue.
        Test that its size is 1.
        """
        que = Queue_()
        que.put(1)
        self.assertFalse(que.empty())
        self.assertEqual(que.top(), 1)
        self.assertEqual(que.size(), 1)


    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of get function raises Assertion error
        """
        que = Queue_()
        self.assertRaises(IndexError, que.get)

    def test_max_size(self):
        """
        Create a Queue_ with a definite max_size
        Test that it returns max size correctly
        """
        que = Queue_([1, 2, 3, 4], 10)
        self.assertEqual(que.get_max_size(), 10)

    def test_new_queue_is_full(self):
        """
        Create various instances of Queue.
        Test whether it is possible to know is they are full
        """
        for material, max_size, answer in zip(([1, 0, 3], [0, 2, 3], [1000000, 2, 3]),
                                              (3, 5), (True, False, False)):
            queue = Queue_(material, max_size)
            self.assertEqual(queue.full(), answer)

    def test_incorrect_input_not_iterable_raised_error(self):
        """
        Create instances of Queue with non-iterable data
        Test that initialisation raises Type error
        """
        for material in (True, 1, float('inf'), 4.0):
            self.assertRaises(ValueError, Queue_, material)

    def test_incorrect_input_too_long_raised_error(self):
        """
        Create instances of Queue with mismatching data length and max size
        Test that initialisation raises Value error
        """
        self.assertRaises(ValueError, Queue_, [1, 45, 3, 0, 0], 1)

    def test_put_too_many_elements_raised_error(self):
        """
        Create instances of Queue
        Put in so many elements it exceeds max size
        Test that call of put function raises Value error
        """
        for capacity in [1, 4, 6, 600]:
            queue = Queue_([True] * capacity, capacity)
            self.assertRaises(ValueError, queue.put, True)
