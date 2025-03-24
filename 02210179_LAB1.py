# #Task 1: Task 1: Implement the List Class Structure 
# Create a class called CustomList that uses an underlying array for storage. Your 
# implementation should include:
# ● Private array to store elements 
# ● Variables to track capacity and current size 
# ● Constructor that initializes the array with a default capacity 

#Answer
class CustomList:
    def __init__(self, capacity=10):
        self._capacity = capacity  
        self._size = 0 
        self._array = [None] * self._capacity  
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")
if __name__ == "__main__":
    custom_list = CustomList()
    
# Task 2: Implement Basic Operations 
# Implement the following basic operations: 
# 1. append(element) - Add an element to the end of the list 
# 2. get(index) - Retrieve an element at a specific index 
# 3. set(index, element) - Replace an element at a specific index 
# 4. size() - Return the current number of elements 

#Answer
class CustomList:
    def __init__(self, capacity=10):
        self._array, self._size = [None] * capacity, 0
        print(f"Created new CustomList with capacity: {capacity}\nCurrent size: 0")

    def append(self, element):
        if self._size == len(self._array): self._array += self._array
        self._array[self._size], self._size = element, self._size + 1
        print(f"Appended {element} to the list")

    def get(self, index): return self._array[index] if 0 <= index < self._size else None
    
    def set(self, index, element):
        if 0 <= index < self._size: self._array[index] = element; print(f"Set element at index {index} to {element}")
    
    def size(self): return self._size

lst = CustomList()
lst.append(5)
print(f"Element at index 0: {lst.get(0)}")
lst.set(0, 10)
print(f"Element at index 0: {lst.get(0)}")
print(f"Current size: {lst.size()}")