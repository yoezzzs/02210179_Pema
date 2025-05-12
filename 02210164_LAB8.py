#Part 1: AVL Tree Implementation 
#Done by Biran Rai-02210164
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _rotate_right(self, z):
        print(f"Right rotation on node {z.value}")
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_left(self, z):
        print(f"Left rotation on node {z.value}")
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def insert(self, value):
        print(f"Inserting {value}")
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # Duplicate

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Rotations
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def delete(self, value):
        print(f"Deleting {value}")
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Rebalance
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, value):
        print(f"Searching for {value}...")
        found = self._search(self.root, value)
        print("Found!" if found else "Not found.")
        return found

    def _search(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def get_height(self):
        height = self._get_height(self.root)
        print(f"Tree height: {height}")
        return height

    def is_balanced(self):
        balanced = self._is_balanced(self.root)
        print(f"Tree is balanced: {balanced}")
        return balanced

    def _is_balanced(self, node):
        if not node:
            return True
        balance = self._get_balance(node)
        return abs(balance) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right)

    # Pretty print the tree sideways
    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1, prefix="R---- ")
        print("     " * level + prefix + str(node.value))
        if node.left:
            self.print_tree(node.left, level + 1, prefix="L---- ")


# Example usage
if __name__ == "__main__":
    avl = AVLTree()

    # Insert values
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.insert(25)

    # Check height and balance
    avl.get_height()
    avl.is_balanced()

    # Search for values
    avl.search(30)
    avl.search(60)

    # Delete some values
    avl.delete(20)
    avl.delete(30)

    # Final check
    avl.get_height()
    avl.is_balanced()

    print("\nFinal AVL Tree Structure:")
    avl.print_tree()
