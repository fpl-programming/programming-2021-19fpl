"""
BinarySearchTree Implementation
"""
from BinaryTree.binary_search_tree import BinarySearchTree

# create tree
tree = BinarySearchTree()
print('A tree is created!\nNew tree is here:', tree)

# check that new tree is empty
print('New tree is empty:', tree.is_empty(), end='\n\n')

# add new elements in the tree
print('Adding some elements...')
tree.add(8)
tree.add(10)
tree.add(7)
tree.add(11)
tree.add(20.5)
tree.add(6)

print('The root is', tree.root.root)
print('Elements in the tree:', end=' ')
tree.look_dfs()
print('Depth of the tree is', tree.get_max_height(), end='\n\n')

# remove some elements
tree.remove(11)
print('Elements in the tree after removal of 10:', end=' ')
tree.look_dfs()
print('Depth of the tree is', tree.get_max_height(), end='\n\n')

# find an element
found = tree.find(7)
print('tree.find(7):', found)
print('root is', found.root)
print('left node is', found.left_node.root)
print('right node is', found.right_node, end='\n\n')

# kill the tree...
tree.remove(8)
print('tree.remove(tree.root)\ntree.root is ', tree.root)
print('tree\'s max height is', tree.get_max_height())
print('   ☠️')
