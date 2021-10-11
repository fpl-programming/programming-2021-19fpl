"""
Binary Tree starter
"""

from binary_search_tree.bst import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes = [89, 23, 98, 95, 10, 29, 77]

    for element in nodes:
        tree.add(element)

    print(tree.get_height())
    tree.remove(98)
    print(tree.get_height())

    RESULT = tree.find(29)

    assert RESULT is True, 'Results are different'
