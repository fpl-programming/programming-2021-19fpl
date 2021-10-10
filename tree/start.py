"""
Longest common subsequence implementation starter
"""
from tree.binarytree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes = [20, 11, 33, 1, 31, 10, 9]
    for element in nodes:
        tree.add(element)

    print(tree.get_height())
    tree.remove(11)
    print(tree.get_height())

    RESULT = tree.find(33)

    assert RESULT is True, 'Results differ'
