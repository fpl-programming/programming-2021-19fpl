"""
Programming for linguists
Start module for BinaryTree
"""

from binary_tree.main import BinaryTree


if __name__ == "__main__":
    tree = BinaryTree(8)
    for node in [6, 10, 5, 7, 9, 11, 12, 13]:
        tree.add_node(node)
    for node in [6, 10, 5, 7, 9, 11]:
        print("Searching", node, "we've found", tree.search_node(node).node)
    tree.delete_node(10)
    print('\n')
    for node in [8, 6, 10, 5, 7, 9, 11]:
        print("Searching", node, "we've found", tree.search_node(node).node)

    print('\nThe max tree height is', tree.get_max_tree_height())

    nodes = []
    for node in tree.go_wide():
        nodes.append(node.node)
    print('\nGoing wide we get', nodes)
