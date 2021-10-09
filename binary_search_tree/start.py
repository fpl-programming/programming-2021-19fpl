"""
Binary Search Tree implementation starter
"""

from binary_search_tree.binary_search_tree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree('BST')
    elements = [10, 4, 12, 6, 8, 1, 11, 14, 3, 5, 7]

    for element in elements:
        tree.add(element)

    print('The Binary Search Tree before transformation')
    print(tree)

    tree.add(2)
    print('After adding 2:')
    print(tree)

    found_element = tree.find(6)
    print('We are looking for 6...')
    print(f"""Node is found, where the root is {found_element.root}
                     the left child's root is {found_element.left_node.root}
                     the right child's root is {found_element.right_node.root}""")

    tree.remove(6)
    print('\nThe tree after removing 6')
    print(tree)

    print('\nLet\'s find the max height of the tree.')
    print(f'It is {tree.max_height}.')

    RESULT = tree.get_tree_traversal()
    print('\nAnd finally let\'s get lengthwise tree traversal.')
    print(f'Here it is: {", ".join(map(str, RESULT))}')

    assert RESULT == [10, 4, 1, 3, 2, 12, 11, 14], 'BST does not work'
