# Part 1: Stack Implementation using Array 
#Done by Biran Rai - 02210164
# Task 1: Implementthe ArrayStack Class Structure
# Create a class called ArrayStack that uses an underlying array for storage. Your
# implementation should include:
# ● Private array to store elements
# ● Variable to track the top ofthe stack
# ● Constructor thatinitializes the array with a default capacity

#Solution:

class ArrayStack:
    def __init__(self, capacity=10):
        self._capacity = capacity  # Default capacity of the stack
        self._stack = [None] * self._capacity  # Private array to store elements
        self._top = -1  # Variable to track the top of the stack
        print(f"Created new ArrayStack with capacity: {self._capacity}")

    def is_empty(self):
        return self._top == -1  # Returns True if stack is empty

# Example usage
stack = ArrayStack()
print("Stack is empty:", stack.is_empty())

# Task 2: Implement Array-based Stack Operations
# Implementthe following operations:
# 1. push(element) - Add an elementto the top ofthe stack
# 2. pop() - Remove and return the element atthe top
# 3. peek() - Return the element atthe top without removing it
# 4. is_empty() - Check ifthe stack is empty
# 5. size() - Return the current number of elements
# 1
# 6. display() - Show all elements in the stack

#Solution:

class ArrayStack:
    def __init__(self, capacity=10):
        self._capacity = capacity  # Default capacity of the stack
        self._stack = [None] * self._capacity  # Private array to store elements
        self._top = -1  # Variable to track the top of the stack
        print(f"Created new ArrayStack with capacity: {self._capacity}")

    def is_empty(self):
        return self._top == -1  # Returns True if stack is empty
    
    def push(self, element):
        if self._top + 1 == self._capacity:
            print("Stack is full! Cannot push.")
            return
        self._top += 1
        self._stack[self._top] = element
        print(f"Pushed {element} to the stack")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        popped_element = self._stack[self._top]
        self._stack[self._top] = None  # Clear the value
        self._top -= 1
        print(f"Popped element: {popped_element}")
        return popped_element
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        return self._stack[self._top]
    
    def size(self):
        return self._top + 1
    
    def display(self):
        print("Display stack:", self._stack[:self._top + 1])

# Example usage
stack = ArrayStack()
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
print("Top element:", stack.peek())
stack.pop()
print("Stack size:", stack.size())
stack.display()



