"""
Programming for linguists
Start script for BinarySearchTree
"""

from binary_tree.binary_tree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes = [15, 5, 19, 6, 30, 20, 4]
    for element in nodes:
        tree.add(element)

    print(tree.get_height())
    tree.remove(20)
    print(tree.get_height())

    RESULT = tree.find(15)

    assert RESULT is True, 'Results differ'
