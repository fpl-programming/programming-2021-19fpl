"""
Longest common subsequence implementation starter
"""
from binary_search_tree.binary_search_tree import BinarySearchTree, Node

if __name__ == '__main__':
    tree = BinarySearchTree()
    nodes_to_add = [Node(8), Node(4), Node(2), Node(3), Node(10), Node(16),
                    Node(13), Node(12),Node(11)]
    for node in nodes_to_add:
        tree.add(node)
    print(tree.get_size())
    print(tree.traverse_breadth_tree)
    tree.remove(Node(12))
    print(tree.get_size())
    tree.get_max_height()

    RESULT = tree.find(Node(13)).root

    assert RESULT == 13, 'Root not found'
