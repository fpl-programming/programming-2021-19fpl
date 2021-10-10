from binarytree.binarytree import BinaryTree

if __name__ == '__main__':
    tree = BinaryTree()
    elements = [1, 7, 9, 4, 6, 2]

    for element in elements:
        tree.add(element)
    print(tree)

    tree.add(8)
    print(tree)

    find_element = tree.find(6)
    print(find_element)

    tree.remove(6)
    print(tree)

    RESULT = tree.get_height()

    assert RESULT == 4, 'BST does not work'
