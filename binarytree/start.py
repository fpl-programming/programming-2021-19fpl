"""
Binary Tree implementation starter
"""

import random
from binarytree.binarytree import BinaryTree


if __name__ == '__main__':
    root = 5
    print('\t...creating a binary tree...')
    binary_tree = BinaryTree(root)
    print('The binary tree with root value', root, 'is created.\n')

    node_values = [2, 7, 6, 3, 4, 1, 10, 8, 9]
    print('\t...filling the binary tree with nodes...')
    for val in node_values:
        binary_tree.add(val)
    print('All the values are successfully added to the binary tree.\n')

    find_random_values = []
    find_random_values.append(random.randint(0, 15))
    find_random_values.append(random.randint(0, 15))
    find_random_values.append(random.randint(0, 15))
    for random_val in find_random_values:
        print('\t...trying to find if there is a node with value', random_val, '...')
        find_res = binary_tree.find(random_val)
        if find_res:
            print('Success! The binary tree contains a node with value', random_val, '.\n')
        else:
            print('Uh oh! Seems like no nodes with value', random_val, ' in the binary tree :( \n')

    print('\t...calculating how high the binary tree is...')
    height = binary_tree.get_height()
    print('The binary tree is', height, 'levels high!\n')

    print('\t...traversing the binary tree in depth...')
    binary_tree.get_dfs()
    print('- the result of DFS traversal of the binary tree\n')

    remove_random_values = []
    remove_random_values.append(random.randint(0, 15))
    remove_random_values.append(random.randint(0, 15))
    remove_random_values.append(random.randint(0, 15))
    for random_val in remove_random_values:
        print('\t...trying to remove a node with the value', random_val, '...')
        remove_res = binary_tree.remove(random_val)
        if remove_res:
            print('The node with value', random_val, 'is removed from the binary tree.\n')
        else:
            print('Uh oh! Cannot remove a node with value', random_val, 'because it is not in the binary tree now.\n')

    if binary_tree.get_height is not None:
        binary_tree.remove(binary_tree.root.value)
    binary_tree.add(0)
    RESULT = binary_tree.root.value
    assert RESULT == 0, 'Binary Tree not working'
