"""
Programming for linguists

Binary Tree

"""

from binary_tree.binary_tree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes_to_add = [8, 3, 10, 1, 6]
    for node in nodes_to_add:
        tree.add(node)

    print(f'Height of the tree is {tree.get_height()} levels\n')
    level_values = tree.width_traverse()
    for key, values in level_values.items():
        print(f'Level({key}) contains these values: {values}')

    tree.remove_node(3)

    level_values = tree.width_traverse()
    print('')
    for key, values in level_values.items():
        print(f'Level({key}) contains these values: {values}')

    RESULT = tree.find(3)
    assert RESULT is False, 'Completed successfully'
