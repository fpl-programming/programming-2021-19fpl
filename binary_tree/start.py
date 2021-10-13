"""
start
"""

from binary_tree.binary_tree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes = [22, 2, 20, 5, 12, 15, 67]
    for element in nodes:
        tree.add(element)
    print(tree.get_height())
    tree.remove(67)
    print(tree.get_height())

    RESULT = tree.find(15)

    assert RESULT is True, 'Results differ'
