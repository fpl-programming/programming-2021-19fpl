"""
Binary Search Tree implementation starter
"""

from binary_search_tree.binary_search_tree import BinarySearchTree


if __name__ == '__main__':
    elements = [10, 8, 12, 6, 7, 14, 9]

    tree = BinarySearchTree()

    print('1. Let us add the elements [10, 8, 12, 6, 7, 14, 9] to the tree.\n')
    for element in elements:
        tree.add(element)
    print('The Binary Search Tree after adding the elements:')
    print(tree)

    print('2. Let us find an element "8" in the tree and see its children.\n')
    node_element = tree.find(8)
    print(f'We are looking for {node_element.root}. '
          f'Its left child is {node_element.left.root}. '
          f'Its right child is {node_element.right.root}.\n')

    print('3. Let us remove an element "6" from the tree and see the structure of the tree after removing.\n')
    print('The Binary Search Tree before:')
    print(tree)

    tree.remove(6)

    print('The Binary Search Tree after:')
    print(tree)

    print('3. Let us find out how many levels in the tree.\n')
    print(f"The Binary Search Tree's height is {tree.get_height()}.")

    RESULT = tree.get_height()

    assert RESULT == 3, 'Binary Search Tree is not working'
