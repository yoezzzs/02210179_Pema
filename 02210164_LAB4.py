# Part 1: Queue Implementation using Array
# Task 1: Implementthe ArrayQueue Class Structure
# Create a class called ArrayQueue that uses an underlying array for storage. Your
# implementation should include:
# ● Private array to store elements
# ● Variables to track the front and rear indices
# ● Constructor that initializes the array with a default capacity
#Done by Biran 
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        print(f"Created new Queue with capacity: {capacity}")
    
    def is_empty(self):
        return self.front == -1
    
# Example Usage
queue = ArrayQueue()
print("Queue is empty:", queue.is_empty())

# Task 2: Implement Array-based Queue Operations
# Implement the following operations:
# 1. enqueue(element) - Add an element to the rear of the queue
# 1
# 2. dequeue() - Remove and return the element at the front
# 3. peek() - Return the element at the front without removing it
# 4. size() - Return the current number of elements
# 5. display() - Show all elements in the queue

class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        print(f"Created new Queue with capacity: {capacity}")
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, element):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        print(f"Enqueued {element} to the queue")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        element = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Dequeued element: {element}")
        return element
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        return self.queue[self.front]
    
    def size(self):
        if self.is_empty():
            return 0
        return (self.rear - self.front + 1) % self.capacity if self.rear >= self.front else (self.capacity - self.front + self.rear + 1)
    
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        index = self.front
        elements = []
        while index != self.rear:
            elements.append(self.queue[index])
            index = (index + 1) % self.capacity
        elements.append(self.queue[self.rear])
        print("Display queue:", elements)
    
# Example Usage
queue = ArrayQueue()
queue.enqueue(10)
queue.display()
queue.enqueue(20)
queue.display()
queue.enqueue(30)
queue.display()
print("Front element:", queue.peek())
queue.dequeue()
queue.display()
print("Queue size:", queue.size())
