"""
Programming for linguists

Tests for Ellipse class.
"""

import unittest
from shapes.ellipse import Ellipse


class EllipseTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Ellipse
    """
    def test_ellipse_get_uid(self):
        """
        Creates a ellipse.
        Tests that the correct uid is returned.
        """
        ellipse = Ellipse(0, 4, 6)
        self.assertEqual(ellipse.get_uid(), 0)

    def test_ellipse_get_area(self):
        """
        Creates a ellipse.
        Tests that the area is calculated correctly.
        """
        ellipse = Ellipse(1, 4, 6)
        self.assertEqual(ellipse.get_area(), 18.84955592153876)

    def test_ellipse_get_perimeter(self):
        """
        Creates a ellipse.
        Tests that the perimeter is calculated correctly.
        """
        ellipse = Ellipse(0, 4, 6)
        self.assertEqual(ellipse.get_perimeter(), 16.01904224441409)
