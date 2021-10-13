"""
Binary Tree implementation starter
"""

import random
from binarytree.node import Node
from binarytree.binarytree import BinaryTree


if __name__ == '__main__':
    ROOT = 5
    print('\t...creating a binary tree...')
    binary_tree = BinaryTree(ROOT)
    print('The binary tree with root value', ROOT, 'is created.\n')

    nodes = [2, 7, 6, 3, 4, 1, 10, 8, 9]
    print('\t...filling the binary tree with nodes...')
    for val in nodes:
        binary_tree.add(Node(val))
    print('All the nodes are successfully added to the binary tree.\n')

    find_random_nodes = [Node(random.randint(0, 15))]
    find_random_nodes.append(Node(random.randint(0, 15)))
    find_random_nodes.append(Node(random.randint(0, 15)))
    for random_node in find_random_nodes:
        print('\t...trying to find if there is a node with value', random_node.value, '...')
        find_res = binary_tree.find(random_node)
        if find_res:
            print('Yes, the tree contains a node with value', random_node.value, '.\n')
        else:
            print('No nodes with value', random_node.value, ' in the binary tree :( \n')

    print('\t...calculating how high the binary tree is...')
    height = binary_tree.get_height()
    print('The binary tree is', height, 'levels high!\n')

    print('\t...traversing the binary tree in depth...')
    binary_tree.get_dfs()
    print('- the result of DFS traversal of the binary tree\n')

    remove_random_nodes = [Node(random.randint(0, 15))]
    remove_random_nodes.append(Node(random.randint(0, 15)))
    remove_random_nodes.append(Node(random.randint(0, 15)))
    for random_node in remove_random_nodes:
        print('\t...trying to remove a node with the value', random_node.value, '...')
        remove_res = binary_tree.remove(random_node)
        if remove_res:
            print('The node with value', random_node.value, 'is removed from the binary tree.\n')
        else:
            print('Cannot remove a node', random_node.value, 'because it is not in the tree.\n')

    if binary_tree.get_height is not None:
        binary_tree.remove(binary_tree.root)
    binary_tree.add(Node(0))
    RESULT = binary_tree.root.value
    assert RESULT == 0, 'Binary Tree not working'
