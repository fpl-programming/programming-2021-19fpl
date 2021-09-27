"""
Programming for linguists

Tests for QueueFromStack class.
"""

import unittest

# from queue_.queue_from_stack import QueueFromStack
from queue_from_stack import QueueFromStack


class QueueFromStackTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of QueueFromStack class
    """

    def test_queue_to_stack(self):
        """
        Create a Queue.
        Turn it into a stack back.
        Test that call this function again raises Type error
        """
        queue = QueueFromStack([1, 2, 3])
        queue.queue_to_stack()
        self.assertFalse(queue.is_queue)
        self.assertRaises(TypeError, queue.queue_to_stack)

