"""
Programming for linguists
Start script for BinarySearchTree
"""

from bintree.binarytree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes = [16, 11, 24, 6, 31, 19, 1]
    for element in nodes:
        tree.add(element)

    print(tree.get_height())
    tree.remove(19)
    print(tree.get_height())

    RESULT = tree.find(16)

    assert RESULT is True, 'Results differ'
