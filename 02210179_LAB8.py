#Done by Pema Yoezer (02210179)
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
    def __init__(self, value, color="RED", left=None, right=None, parent=None):
        self.value = value
        self.color = color  # "RED" or "BLACK"
        self.left = left
        self.right = right
        self.parent = parent


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
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

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
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
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
    rb_tree.insert(10)
    rb_tree.insert(20)
    rb_tree.insert(30)
    rb_tree.insert(15)
    rb_tree.insert(25)
    rb_tree.insert(5)
    
    # Delete element
    rb_tree.delete(15)
    
    # Print tree structure
    print("Tree Structure after insertions and deletion:")
    rb_tree.print_tree()
    
    # Black Height
    print("\nBlack Height of the tree:", rb_tree.get_black_height())
