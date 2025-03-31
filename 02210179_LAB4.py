# Pema Yoezer(02210179):

# Part 2: Queue implementation using Linked List 
# Task 3: Implement the Node and LinkedStack Class Structure 
# Create two classes: 
# 1. Node class that contains: 
# ● Data field to store the element 
# ● Next field to reference the next node 
# 2. LinkedQueue class that contains: 
# ● Front reference to the first node 
# ● Rear reference to the last node 
# ● Size counter to track the number of elements

#Answer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        print("Created new LinkedQueue")

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def get_size(self):
        return self.size

# Example usage
queue = LinkedQueue()
print("Queue is empty:", queue.is_empty())

# Task 4: Implement Linked List-based Queue Operations 
# Implement the following operations: 
# 1. enqueue(element) - Add an element to the rear of the queue 
# 2. dequeue() - Remove and return the element at the front 
# 3. peek() - Return the element at the front without removing it 
# 4. is_empty() - Check if the queue is empty 
# 2 
# 5. size() - Return the current number of elements 
# 6. display() - Show all elements in the queue

#Answer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self._size = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
        self._size += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        removed = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self._size -= 1
        print(f"Dequeued element: {removed}")
        return removed

    def peek(self):
        return self.front.data if self.front else "Queue is empty"

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size

    def display(self):
        elements, temp = [], self.front
        while temp:
            elements.append(temp.data)
            temp = temp.next
        print("Display queue:", elements)

# Example Usage
q = Queue()
q.enqueue(10)
q.display()
q.enqueue(20)
q.display()
q.enqueue(30)
q.display()
print("Front element:", q.peek())
q.dequeue()
print("Current queue:", " -> ".join(map(str, [q.front.data, q.rear.data])) + " -> null" if not q.is_empty() else "Queue is empty")
print("Queue size:", q.size())


# Task 5: Differentiate between the two approaches of implementing Queue Which one 
# # do you prefer? Justify your answer

#Answer:
# A queue can be implemented using either an array-based approach or a linked list-based approach. The array-based queue uses a fixed-size or dynamically growing 
# list where elements are added at the rear and removed from the front. While enqueue operations are efficient (O(1) in Python lists), dequeuing takes O(n) time 
# because elements must be shifted forward after removal. This approach is simple to implement and works well when the queue size is known in advance, but it may
# lead to inefficient memory usage due to resizing or pre-allocated space.

# On the other hand, a linked list-based queue dynamically allocates memory using nodes, making it more flexible. It efficiently supports both enqueue and dequeue 
# operations in O(1) time, as there is no need to shift elements. However, it requires extra memory for storing pointers and adds a slight complexity in managing node
# connections. Despite this, a linked list queue is ideal for scenarios where the queue size is unpredictable and frequent insertions and deletions occur. Given its
# efficiency in handling large or dynamic data, I prefer the linked list-based queue over the array-based approach.