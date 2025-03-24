#Pema Yoezer(022101790-Part 2)
# Part 2: Stack Implementation using Linked List
# Task 3: Implementthe Node and LinkedStack Class Structure
# Create two classes:
# 1. Node class that contains:
# - Data field to store the element
# - Next field to reference the next node
# 2. LinkedStack class that contains:
# - Top reference to the first node (head ofthe linked list)
# - Size counter to track the number of elements

#Answer:
class Node:
    def __init__(self, data, next=None): self.data, self.next = data, next

class LinkedStack:
    def __init__(self): self.top, self._size = None, 0; print("Created new LinkedStack")
    def is_empty(self): return self.top is None
    def size(self): return self._size
    def push(self, element): self.top, self._size = Node(element, self.top), self._size + 1; print(f"Pushed {element} to the stack")
    def pop(self):
        if self.is_empty(): return print("Stack underflow!"), None
        element, self.top, self._size = self.top.data, self.top.next, self._size - 1
        print(f"Popped element: {element}")
        return element
    def peek(self): return None if self.is_empty() else self.top.data
    def display(self):
        current, elements = self.top, []
        while current: elements.append(str(current.data)); current = current.next
        print("Current stack:", " -> ".join(elements) + " -> null")

# Example usage
stack = LinkedStack()
print("Stack is empty:", stack.is_empty())

#Task 4: Implement Linked List-based Stack Operations
# Implementthe following operations:
# 1. push(element) - Add an elementto the top ofthe stack
# 2. pop() - Remove and return the element atthe top
# 3. peek() - Return the element atthe top without removing it
# 4. is_empty() - Check ifthe stack is empty
# 5. size() - Return the current number of elements
# 6. display() - Show all elements in the stack
#Answer
class Node:
    def __init__(self, data, next=None): self.data, self.next = data, next

class LinkedStack:
    def __init__(self): self.top, self._size = None, 0; print("Created new LinkedStack")
    def is_empty(self): return self.top is None
    def size(self): return self._size
    def push(self, element): self.top, self._size = Node(element, self.top), self._size + 1; print(f"Pushed {element} to the stack")
    def pop(self):
        if self.is_empty(): return print("Stack underflow!"), None
        element, self.top, self._size = self.top.data, self.top.next, self._size - 1
        print(f"Popped element: {element}")
        return element
    def peek(self): return None if self.is_empty() else self.top.data
    def display(self):
        current, elements = self.top, []
        while current: elements.append(str(current.data)); current = current.next
        print("Current stack:", " -> ".join(elements) + " -> null")

# Example usage
stack = LinkedStack()
for i in [10, 20, 30]: stack.push(i); stack.display()
print("Top element:", stack.peek())
stack.pop()
stack.display()
print("Stack size:", stack.size())

# #Task 5: Differentiate between the two approaches of implementing stack. Which one do
# you prefer? Justify your answer
#Answer
# The array-based stack uses a fixed-size array for storage, which makes it simple and fast, with O(1) time complexity
# for push and pop operations (except when resizing is needed). However, it may waste memory if the allocated array is too large
# or require resizing if it is too small. In contrast, the linked list-based stack dynamically allocates memory, ensuring efficient 
# space usage without resizing issues. It also has O(1) time complexity for push and pop operations but incurs additional memory overhead 
# due to storing pointers. While the array-based stack benefits from faster access times due to contiguous memory storage, the linked list-based 
# stack is more flexible and preferable when the number of elements is unpredictable.s
# I prefer the linked list-based stack for cases where we don't know the number of elements beforehand since it allows dynamic memory allocation 
# without resizing overhead. However, for small, fixed-size stacks where speed is critical, an array-based stack is better due to faster access times.
