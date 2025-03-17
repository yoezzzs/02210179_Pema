# Task 1: Implement the Node and List Class Structure 
# Create two classes: 
# 1. Node class that contains: - 
# Data field to store the element - 
# Next field to reference the next node 
# 2. LinkedList class that contains: - 
# Head reference to the first node - - 
# Tail reference to the last node (optional but recommended) 
# Size counter to track the number of elements

#Answer
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("Created new LinkedList")
        print(f"Current size: {self.size}")
        print(f"Head: {self.head}")

# Create a LinkedList instance to see the output
ll = LinkedList()

# Task 2: Implement Basic Operations 
# Implement the following basic operations: 
# 1. append(element) - Add an element to the end of the list 
# 2. get(index) - Retrieve an element at a specific index 
# 3. set(index, element) - Replace an element at a specific index 
# 4. size() - Return the current number of elements 
# 5. prepend(element) - Add an element at the beginning of the list

#Answer
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("Created new LinkedList")
    
    # Append element at the end of the list
    def append(self, element):
        new_node = Node(element)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1
        print(f"Appended {element} to the list")
    
    # Get element at a specific index
    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}: {current.data}")
        return current.data
    
    # Set element at a specific index
    def set(self, index, element):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}")
    
    # Return the current size of the list
    def size(self):
        return self.size
    
    # Prepend element at the beginning of the list
    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1
        print(f"Prepend {element} to the list")
    
    # Print the Linked List
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Print Linked list :", " ".join(elements))  # Join elements with a space

# Test the LinkedList operations
ll = LinkedList()
ll.append(5)
ll.get(0)
ll.set(0, 10)
ll.get(0)
print(f"Current size: {ll.size}")
ll.prepend(10)
ll.print_list()
