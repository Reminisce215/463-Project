import random
import time
from pympler import asizeof


#Merge two sorted lists into a single sorted list.
def merge(left, right):
    """
    This function merges two sorted lists, 'left' and 'right', into a single sorted list.
    It sequentially compares the elements of the two lists and appends the smaller one to the result list.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Sort a list using the mergesort algorithm.
def mergesort(arr):
    """
    This function sorts the list 'arr' using the mergesort algorithm.
    The list is divided into two halves, which are sorted independently and then merged together.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

# Generate a random list of integers for testing
arr = [random.randint(1, 1000) for _ in range(1000)]


# Example usage
print("Original array:", arr)
# Measure the execution time
start_time = time.time()
sorted_arr=mergesort(arr)  # Sort the list using the custom Timsort algorithm.
end_time = time.time()
execution_time = end_time - start_time
print("Sorted array:", sorted_arr)


# Measure the memory usage
mem_usage = asizeof.asizeof(arr)
print("Execution time: {:.6f} seconds".format(execution_time))
print("Memory usage: {:.2f} MB".format(mem_usage / (1024 * 1024)))

