"""
Programming for linguists
Tests for RealeauxTriangle class.
"""

import unittest

from shapes.reuleaux_triangle import ReuleauxTriangle


class ReuleauxTriangleTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Ellipse
    """
    def test_reuleaux_triangle_get_uid(self):
        """
        Creates a Reuleaux triangle.
        Tests that the correct uid is returned.
        """
        reuleaux_triangle = ReuleauxTriangle(0, 5)
        self.assertEqual(reuleaux_triangle.get_uid(), 0)

    def test_reuleaux_triangle_get_area(self):
        """
        Creates a Reuleaux triangle.
        Tests that the area is calculated correctly.
        """
        reuleaux_triangle = ReuleauxTriangle(1, 5)
        self.assertEqual(reuleaux_triangle.get_area(), 17.61927307526145)

    def test_reuleaux_triangle_get_perimeter(self):
        """
        Creates a Reuleaux triangle.
        Tests that the perimeter is calculated correctly.
        """
        reuleaux_triangle = ReuleauxTriangle(2, 5)
        self.assertEqual(reuleaux_triangle.get_perimeter(), 15.707963267948966)

    def test_reuleaux_triangle_get_inscribed_circle_area(self):
        """
        Creates a Reuleaux triangle.
        Tests that the inscribed circle area is calculated correctly.
        """
        reuleaux_triangle = ReuleauxTriangle(3, 5)
        self.assertEqual(reuleaux_triangle.get_inscribed_circle_radius(), 2.113248654051871)

    def test_reuleaux_triangle_get_circumscribed_circle_area(self):
        """
        Creates a Reuleaux triangle.
        Tests that the inscribed circle area is calculated correctly.
        """
        reuleaux_triangle = ReuleauxTriangle(4, 5)
        self.assertEqual(reuleaux_triangle.get_circumscribed_circle_radius(), 2.886751345948129)
