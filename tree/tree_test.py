from tree import Tree
import unittest


class TreeUnitTestCase(unittest.TestCase):
    def test_insert_increase_sequence(self):
        tree = Tree()
        for i in range(100):
            tree.insert(i)

        self.assertEqual(tree.height(), 100)

    def test_insert_decrease_sequence(self):
        tree = Tree()
        data = [x for x in range(100)]
        data.reverse()
        for i in data:
            tree.insert(i)

        self.assertEqual(tree.height(), 100)

    def test_insert_negative(self):
        tree = Tree()
        for i in range(100):
            tree.insert(i)
        self.assertRaises(IndexError, tree.erase, 1000)

    def test_erase(self):
        tree = Tree()
        tree.insert(100)
        tree.insert(150)
        tree.insert(50)
        tree.erase(50)
        self.assertEqual(tree.width(), 1)

    def test_erase_negative(self):
        tree = Tree()
        for i in range(100):
            tree.insert(i)
        tree.erase(10)
        self.assertRaises(IndexError, tree.erase, 10)

    def test_find(self):
        tree = Tree()
        data = [x for x in range(100)]
        for i in data:
            tree.insert(i)
        data.reverse()
        for i in data:
            tree.insert(i)
        self.assertTrue(tree.find(1))

    def test_width_greater_one(self):
        tree = Tree()
        tree.insert(100)
        tree.insert(150)
        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(125)
        tree.insert(175)
        self.assertEqual(tree.width(), 4)

    def test_width_eight(self):
        tree = Tree()
        for element in [100, 150, 50, 25, 75, 125, 175, 10, 30, 60, 80, 120, 130, 170, 180]:
            tree.insert(element)
        self.assertEqual(tree.width(), 8)

    def test_lot_insert_erase(self):
        tree = Tree()
        for i in range(100):
            tree.insert(i)
        for i in range(100):
            tree.erase(i)
        self.assertEqual(0, tree.get_size())
