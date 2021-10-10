"""
start.py file
"""
from binarytree.binarytree import BinaryTree

if __name__ == '__main__':
    tree = BinaryTree()
    elements = [1, 7, 9, 4, 6, 2]

    for element in elements:
        tree.add(None,element)
    print(tree)

    tree.add(None, 8)
    print(tree)

    find_element = tree.find(None, 6)
    print(find_element)

    tree.remove(None,6)
    print(tree)

    RESULT = tree.get_height()

    assert RESULT == 4, 'BST does not work'
