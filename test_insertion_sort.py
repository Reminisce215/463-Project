import random
import time
from pympler import asizeof

# Sort a segment of the list using the insertion sort algorithm.
def insertion_sort(arr):
    """
    This function sorts the list 'arr' using the insertion sort algorithm.
    It iteratively picks an element and inserts it into the sorted part of the list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a random list of integers for testing
arr = [random.randint(1, 1000) for _ in range(1000)]


# Example usage
print("Original array:", arr)
# Measure the execution time
start_time = time.time()
insertion_sort(arr)  # Sort the list using the custom Timsort algorithm.
end_time = time.time()
execution_time = end_time - start_time
print("Sorted array:", arr)


# Measure the memory usage
mem_usage = asizeof.asizeof(arr)
print("Execution time: {:.6f} seconds".format(execution_time))
print("Memory usage: {:.2f} MB".format(mem_usage / (1024 * 1024)))

