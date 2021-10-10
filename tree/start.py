"""
Programming for linguists

Start script for BinarySearchTree
"""

from tree.tree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes = [15, 10, 20, 7, 18, 9, 19]
    for element in nodes:
        tree.add(element)

    print(tree.get_height())
    tree.remove(10)
    print(tree.get_height())

    RESULT = tree.find(20)

    assert RESULT is True, 'Results differ'
