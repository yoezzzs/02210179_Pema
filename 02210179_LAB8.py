<<<<<<< HEAD
# Done by Pema Yoezer (02210179_)
=======
# Done by Pema Yoezer (02210179)
>>>>>>> 48832ad606b0086b1267a94015c825f2b42df7e4
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
<<<<<<< HEAD
    def __init__(self, value, color='red', left=None, right=None, parent=None):
        self.value = value
        self.color = color  # 'red' or 'black'
=======
    def __init__(self, value, color="RED", left=None, right=None, parent=None):
        self.value = value
        self.color = color  # "RED" or "BLACK"
>>>>>>> 48832ad606b0086b1267a94015c825f2b42df7e4
        self.left = left
        self.right = right
        self.parent = parent

<<<<<<< HEAD
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
=======

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color="BLACK")  # sentinel NIL node
        self.root = self.NIL

    def insert(self, value):
        node = Node(value)
        node.left = node.right = self.NIL
        self._insert_node(node)

    def delete(self, value):
        node = self._find_node(self.root, value)
        if node == self.NIL:
            print(f"Value {value} not found in tree.")
            return
        self._delete_node(node)

    def search(self, value):
        return self._search_node(self.root, value)

    def get_black_height(self):
        return self._black_height(self.root)

    def print_tree(self, node=None, indent="", last=True):
        if node is None:
            node = self.root
        if node != self.NIL:
            print(indent, "`-- " if last else "|-- ", f"{node.value} ({node.color})", sep="")
            indent += "   " if last else "|  "
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

    # Internal Helpers

    def _insert_node(self, z):
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z

        z.color = "RED"
        self._fix_insert(z)

    def _left_rotate(self, x):
>>>>>>> 48832ad606b0086b1267a94015c825f2b42df7e4
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
<<<<<<< HEAD
        if x.parent is None:
=======
        if not x.parent:
>>>>>>> 48832ad606b0086b1267a94015c825f2b42df7e4
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

<<<<<<< HEAD
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

=======
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def _fix_insert(self, z):
        while z.parent and z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._left_rotate(z.parent.parent)
        self.root.color = "BLACK"

    def _find_node(self, node, value):
        while node != self.NIL and value != node.value:
            node = node.left if value < node.value else node.right
        return node

    def _search_node(self, node, value):
        if node == self.NIL or node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_node(node.left, value)
        else:
            return self._search_node(node.right, value)

    def _transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _delete_node(self, z):
>>>>>>> 48832ad606b0086b1267a94015c825f2b42df7e4
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
<<<<<<< HEAD
            transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            transplant(z, z.left)
        else:
            y = minimum(z.right)
=======
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
>>>>>>> 48832ad606b0086b1267a94015c825f2b42df7e4
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
<<<<<<< HEAD
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
=======
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "BLACK":
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    def _black_height(self, node):
        if node == self.NIL:
            return 1
        left_height = self._black_height(node.left)
        right_height = self._black_height(node.right)
        if left_height != right_height:
            raise Exception("Black height violation")
        return left_height + (1 if node.color == "BLACK" else 0)


# ====== Example Usage ======
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    
    # Insert elements
>>>>>>> 48832ad606b0086b1267a94015c825f2b42df7e4
    rb_tree.insert(10)
    rb_tree.insert(20)
    rb_tree.insert(30)
    rb_tree.insert(15)
<<<<<<< HEAD
    rb_tree.insert(5)
    print("Black Height:", rb_tree.get_black_height())
    print("Search 15:", rb_tree.search(15))  # True
    rb_tree.delete(15)
    print("Search 15 after deletion:", rb_tree.search(15))  # False
    print("Black Height after deletion:", rb_tree.get_black_height())
=======
    rb_tree.insert(25)
    rb_tree.insert(5)
    
    # Delete element
    rb_tree.delete(15)
    
    # Print tree structure
    print("Tree Structure after insertions and deletion:")
    rb_tree.print_tree()
    
    # Black Height
    print("\nBlack Height of the tree:", rb_tree.get_black_height())
>>>>>>> 48832ad606b0086b1267a94015c825f2b42df7e4
