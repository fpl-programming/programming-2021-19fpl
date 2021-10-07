"""
Longest common subsequence implementation starter
"""
import binary_search_tree.binary_search_tree

if __name__ == '__main__':
    tree = binary_search_tree.BinarySearchTree()
    nodes_to_add = [binary_search_tree.Node(8), binary_search_tree.Node(4),
                    binary_search_tree.Node(2), binary_search_tree.Node(3),
                    binary_search_tree.Node(10), binary_search_tree.Node(16),
                    binary_search_tree.Node(13), binary_search_tree.Node(12),
                    binary_search_tree.Node(11)]
    for node in nodes_to_add:
        tree.add(node)
    print(tree.get_size())
    print(tree.traverse_breadth_tree)
    tree.remove(binary_search_tree.Node(12))
    print(tree.get_size())
    tree.get_max_height()

    RESULT = tree.find(13).root

    assert RESULT == 13, 'Root not found'
