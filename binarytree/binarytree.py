"""
Programming for linguists

Implementation of the data structure "Binarytree"
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left_element = None
        self.right_element = None


class BinaryTree():
    def __init__(self, tree, root):
        self.root = None

    def add(self,node, element):
        if self.root is None:
            self.root=Node(element)
        else:
            if node is None:
                node=self.root
            if element>node.element:
                if node.right_element is None:
                    node.right_element = Node(element)
                self.add(node.right_element, element)
            else:
                if node.left.element is None:
                    node.left_element = Node(element)
                self.add(node.left_element, element)

    def find(self, node, key ):

        if self.root is None:
            print ('The root is empty')
        if node is None:
            node = self.root
        if node.key == key or node.left_element or node.right_element:
            return True
        if key < node.key and node.left_element:
            return self.find(node.left, key)
        if key > node.key and node.right_element:
            return self.find(node.right_element, key)
        return False

    def remove(self, node, element):
        if self.root is None:
            print('The root is empty')
        if self.find(None,element) is True:
            if node is None:
                node = self.root
            if element < node.element and node.left_element:
                if node.left_element == element:
                    node.left_element=None
                self.remove(node.left_element,element)
            if element > node.element and node.right_element:
                if element == node.right_element:
                    node.right_element = None
                self.remove(node.right_element,element)
        else:
            print("there is no node")


    def get_height(self):
        pass
