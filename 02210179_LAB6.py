# Pema Yoezer(02210179)
# Part 2: Merge Sort Implementation 
# Implement the merge sort algorithm 
# Create a function called merge_sort that: 
# ● Takes an array/list as input and sorts it in ascending order 
# ● Implements the merge sort algorithm with proper merging of subarrays 
# ● Counts and returns the number of comparisons and array accesses made 
# ● Includes proper handling of edge cases

#Answer:
def merge_sort(arr):
    comparisons = [0]
    accesses = [0]

    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            accesses[0] += 2  # Accessing left[i] and right[j]
            if left[i] <= right[j]:
                merged.append(left[i])
                accesses[0] += 1  # Writing to merged
                i += 1
            else:
                merged.append(right[j])
                accesses[0] += 1
                j += 1

        while i < len(left):
            merged.append(left[i])
            accesses[0] += 1
            i += 1

        while j < len(right):
            merged.append(right[j])
            accesses[0] += 1
            j += 1

        return merged

    def recursive_merge_sort(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        accesses[0] += len(sub_arr)  # Counting slicing accesses
        left = recursive_merge_sort(sub_arr[:mid])
        right = recursive_merge_sort(sub_arr[mid:])
        return merge(left, right)

    # Copy the array so original is preserved
    sorted_arr = recursive_merge_sort(arr[:])
    return sorted_arr, comparisons[0], accesses[0]


# Example usage
original = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comparisons, accesses = merge_sort(original)

print("Original List:", original)
print("Sorted using Merge Sort:", sorted_arr)
print("Number of comparisons:", comparisons)
print("Number of array accesses:", accesses)
