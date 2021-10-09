"""
Programming for linguists

Start script for Binary tree.
"""

from binary_tree import BinaryTree


if __name__ == '__main__':
    print(r'''Let's create this tree
            5
          /   \
         2     7
       /  \   / \
      0   4  6  10''')

    tree = BinaryTree()
    for elem in (5, 2, 7, 0, 4, 6, 10):
        print(f'Insert {elem}', tree.insert(elem))
    print('Insert 5 again', tree.insert(5))

    print('Tree:', end=' ')
    tree.depth_in_order_print()
    print(f'Height: {tree.get_height()}')

    print('Find 7', tree.find(7))
    print('Remove 7', tree.remove(7))
    print('Find 7', tree.find(7))

    print('Tree:', end=' ')
    tree.depth_in_order_print()

    for elem in (5, 2, 0, 4, 6, 10):
        print(f'Remove {elem}', tree.remove(elem))
    print('Tree:', end=' ')
    tree.depth_in_order_print()
