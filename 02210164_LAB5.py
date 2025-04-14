# Part 1: Sequential Search Implementation
# Implementthe Sequential Search Algorithm
# Create a function called sequential_search that:
# ● Takes a list/array and a target value as parameters
# ● Returns the index of the target if found, or -1 if not found
# ● Counts and returns the number of comparisons made
#Done by Biran-02210164 


def sequential_search(arr, target):
    comparisons = 0
    
    for index, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return index, comparisons  # Target found
    
    return -1, comparisons  # Target not found

# Example usage
data = [23, 45, 12, 67, 89, 34, 56]
target = 67

print("List:", data)
print(f"Searching for {target} using Sequential Search")

index, comparisons = sequential_search(data, target)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

print(f"Number of comparisons: {comparisons}")
