"""
Programming for linguists

Example of the data structure "Binary Search Tree"
"""
from tree.search_tree import Node

if __name__ == '__main__':
    print(r"""One example of a tree
             12
           /   \
          5     16
               / \
               14  19
                \    \
                 15   20
    """)

    tree = Node(12)
    for element in [5, 16, 14, 19, 15, 20]:
        tree.insert(element)
    print('The first thing to check is the height')
    height = tree.find_height(tree)
    print(f'The height is {height} and expected is 4')
    print('We will try to delete a node 16 and see a tree in width')
    print('Expected to get [12, 5, 19, 14, 20, 15]')
    tree.delete_node(tree, 16)
    print(tree.in_width())
