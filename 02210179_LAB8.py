# Done by Pema Yoezer (02210179_)
# Part 2: Red-Black Tree Implementation 
# Implement a complete Red-Black Tree with the following requirements: 
# ● Create a class RedBlackTree with the following methods: 
# ○ insert(value): Insert a new value into the Red-Black tree 
# ○ delete(value): Delete a value from the Red-Black tree 
# ○ search(value): Search for a value in the tree 
# ○ get_black_height(): Return the black height of the tree 
# ● Implement color-based insertion and deletion rules 
# ● Implement necessary rotation methods 
# ● Maintain Red-Black tree properties: 
# ○ Every node is either red or black 
# ○ Root is always black 
# ○ All leaves (NIL) are black 
# ○ If a node is red, both its children must be black 
# ○ Every path from a node to its descendant leaves contains the same number 
# of black nodes 
# Example Usage: 
# rb_tree = RedBlackTree() 
# rb_tree.insert(10) 
# rb_tree.insert(20) 
# rb_tree.insert(30) 
# print(rb_tree.get_black_height()) # Should return appropriate 
# black height
#Answer:
class Node:
    def __init__(self, value, color='red', left=None, right=None, parent=None):
        self.value = value
        self.color = color  # 'red' or 'black'
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(value=None, color='black')  # Sentinel NIL node
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value=value, left=self.NIL, right=self.NIL, parent=None)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, value):
        return self._search_tree_helper(self.root, value)

    def _search_tree_helper(self, node, key):
        if node == self.NIL or key == node.value:
            return node != self.NIL
        if key < node.value:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

    def get_black_height(self):
        def black_height(node):
            if node == self.NIL:
                return 1  # NIL nodes are black
            left_height = black_height(node.left)
            if node.color == 'black':
                return left_height + 1
            else:
                return left_height
        return black_height(self.root)

    def delete(self, value):
        def transplant(u, v):
            if u.parent is None:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            v.parent = u.parent

        def minimum(node):
            while node.left != self.NIL:
                node = node.left
            return node

        z = self.root
        while z != self.NIL:
            if z.value == value:
                break
            elif value < z.value:
                z = z.left
            else:
                z = z.right

        if z == self.NIL:
            return  # Node not found

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            transplant(z, z.left)
        else:
            y = minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

# Example Usage
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    rb_tree.insert(10)
    rb_tree.insert(20)
    rb_tree.insert(30)
    rb_tree.insert(15)
    rb_tree.insert(5)
    print("Black Height:", rb_tree.get_black_height())
    print("Search 15:", rb_tree.search(15))  # True
    rb_tree.delete(15)
    print("Search 15 after deletion:", rb_tree.search(15))  # False
    print("Black Height after deletion:", rb_tree.get_black_height())
