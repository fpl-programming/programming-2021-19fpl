"""
Programming for linguists

Start script for Binary search tree
"""

from binary_tree.binary_tree import BinarySearchTree

if __name__ == '__main__':
    print('''We should get this tree
            6
          /   \
         1     8
       /  \   / \
      0   2  7  15''')

    tree = BinarySearchTree()
    for element in (6, 1, 0, 8, 2, 7, 15):
        print('Add', tree.add(element))
    print('Add 8 again', tree.add(8))

    print('Tree:', end=' ')
    tree.depth_in_order()
    print(f'Height: {tree.get_height()}')

    print('Find 1', tree.find(7))
    print('Remove 1', tree.remove(7))
    print('Find 1', tree.find(7))

    print('Tree:', end=' ')
    tree.depth_in_order()

    for element in (6, 1, 0, 8, 2, 7, 15):
        print(f'Remove {element}', tree.remove(element))
    print('Tree:', end=' ')
    tree.depth_in_order()
