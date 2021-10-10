"""
Longest common subsequence implementation starter
"""
from binarytree.binarytree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes = [70, 31, 93, 94, 14, 23, 73]

    for element in nodes:
        tree.add(element)
    print(tree.get_height())
    tree.remove(93)
    print(tree.get_height())

    RESULT = tree.find(23)

    assert RESULT is True, 'Results differ'
