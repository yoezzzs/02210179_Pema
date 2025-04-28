# Part 1: Quick SortImplementation
# Implementthe Quick Sort Algorithm
# Create a function called quick_sort that:
# ● Takes an array/list as input and sorts it in ascending order
# ● Implements the quick sort algorithm with proper partitioning
# ● Counts and returns the number of comparisons and swaps made
# ● Includes at least one optimization (e.g., median-of-three pivot selection)
# Part 1 done by Biran:
def quick_sort(arr):
    comparisons = [0]
    swaps = [0]

    def median_of_three(low, high):
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        if a > b:
            a, b = b, a
        if a > c:
            a, c = c, a
        if b > c:
            b, c = c, b
        # Find the median value and return its index
        if arr[low] == b:
            return low
        elif arr[mid] == b:
            return mid
        else:
            return high

    def partition(low, high):
        pivot_index = median_of_three(low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        swaps[0] += 1

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        swaps[0] += 1
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    original = arr.copy()
    quick_sort_recursive(0, len(arr) - 1)
    return original, arr, comparisons[0], swaps[0]

# Example usage
original_list = [38, 27, 43, 3, 9, 82, 10]
original, sorted_list, comparison_count, swap_count = quick_sort(original_list)

print("Original List:", original)
print("Sorted using Quick Sort:", sorted_list)
print("Number of comparisons:", comparison_count)
print("Number of swaps:", swap_count)
