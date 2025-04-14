#Pema Yoezer(02210179)
# Part 2: Binary Search Implementation 
# Implement the Binary Search Algorithm 
# Create both iterative and recursive versions of the binary search algorithm: 
# ● Function binary_search  that implements binary search 
# ● Should return the index of the target if found, or -1 if not found 
# ● Should count and return the number of comparisons made

#ANSWER
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1  # Only count equality comparison
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def binary_search_recursive(arr, target, low, high, comparisons=0):
    if low > high:
        return -1, comparisons

    mid = (low + high) // 2
    comparisons += 1  # Count equality comparison

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# Example usage
if __name__ == "__main__":
    sorted_list = [12, 23, 34, 45, 56, 67, 89]
    target = 67

    print("Sorted List:", sorted_list)
    print(f"Searching for {target} using Binary Search (Iterative)")
    index, comparisons = binary_search_iterative(sorted_list, target)
    if index != -1:
        print(f"Found at index {index}")
    else:
        print("Not found")
    print(f"Number of comparisons: {comparisons}\n")

    print(f"Searching for {target} using Binary Search (Recursive)")
    index, comparisons = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    if index != -1:
        print(f"Found at index {index}")
    else:
        print("Not found")
    print(f"Number of comparisons: {comparisons}")
