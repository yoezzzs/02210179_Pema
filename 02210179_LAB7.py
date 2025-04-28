# Task 1: Implement the Node and Binary Tree Class Structure 
# Create two classes: 
# 1. Node class with the following attributes: - Value of the node - Left child reference - Right child reference 
# 2. BinaryTree class with: - Root node reference - Constructor to initialize an empty or pre-populated tree

#ANSWER:
# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinaryTree class
class BinaryTree:
    def __init__(self, root_value=None):
        if root_value:
            self.root = Node(root_value)
            print(f"Created new Binary Tree\nRoot: {self.root.value}")
        else:
            self.root = None
            print("Created new Binary Tree\nRoot: None")

# Example usage
if __name__ == "__main__":
    # Creating an empty tree
    tree1 = BinaryTree()

    # Creating a pre-populated tree with root value 10
    tree2 = BinaryTree(10)

# Task 2: Implement Tree Information Methods 
# Create methods to extract information about the tree: 
# 1. height() - Calculate the maximum depth of the tree 
# 2. size() - Count total number of nodes 
# 3. count_leaves() - Count number of leaf nodes 
# 4. is_full_binary_tree() - Check if the tree is a full binary tree 
# 5. is_complete_binary_tree() - Check if the tree is a complete binary 
# tree 
# Example Output: 
# Tree Height: 3 
# Total Nodes: 7 
# Leaf Nodes Count: 4 
# Is Full Binary Tree: True 
# Is Complete Binary Tree: True 

# ANSWER:
from collections import deque

# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinaryTree class
class BinaryTree:
    def __init__(self, root_value=None):
        if root_value:
            self.root = Node(root_value)
            print(f"Created new Binary Tree\nRoot: {self.root.value}")
        else:
            self.root = None
            print("Created new Binary Tree\nRoot: None")

    # Method to calculate height of tree
    def height(self):
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    # Method to calculate total number of nodes
    def size(self):
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)

    # Method to count leaf nodes
    def count_leaves(self):
        def _count_leaves(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return _count_leaves(node.left) + _count_leaves(node.right)
        return _count_leaves(self.root)

    # Method to check if the tree is a full binary tree
    def is_full_binary_tree(self):
        def _is_full(node):
            if not node:
                return True
            if (node.left is None) and (node.right is None):
                return True
            if (node.left is not None) and (node.right is not None):
                return _is_full(node.left) and _is_full(node.right)
            return False
        return _is_full(self.root)

    # Method to check if the tree is a complete binary tree
    def is_complete_binary_tree(self):
        if not self.root:
            return True
        queue = deque()
        queue.append(self.root)
        end = False

        while queue:
            current = queue.popleft()
            if current:
                if end:
                    return False
                queue.append(current.left)
                queue.append(current.right)
            else:
                end = True
        return True

# Example usage
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Tree Height:", tree.height())
    print("Total Nodes:", tree.size())
    print("Leaf Nodes Count:", tree.count_leaves())
    print("Is Full Binary Tree:", tree.is_full_binary_tree())
    print("Is Complete Binary Tree:", tree.is_complete_binary_tree())
