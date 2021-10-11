"""
Programming for linguists
Start module for BinaryTree
"""

from binary_tree.main import BinaryTree


if __name__ == "__main__":
    y = BinaryTree(8)
    y.add_node(9)
    print(y.get_max_tree_height())

    y.delete_node(9)
    print(y.get_max_tree_height())

    for node in [1, 2, 3, 9, 10, 11]:
        y.add_node(node)
    print(y.get_max_tree_height())