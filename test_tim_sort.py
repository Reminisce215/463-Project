import random
import time
from pympler import asizeof






# Sort a segment of the list using the insertion sort algorithm.
def insertion_sort(arr, left, right):
    """
    Sorts a subarray of 'arr' from index left to right using the insertion sort
    It iteratively picks an element and inserts it into the sorted part of the subarray.
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Merge two sorted lists into a single sorted list.
def merge(left, right):
    """
    Merges two sorted lists, left and right, into a single sorted list.
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


# Sort a list using the custom Timsort algorithm.
def custom_timsort(arr):
    """
    Sorts the list 'arr' using timsort algorithm.
    The list is divided into smaller parts(runs) which are sorted using insertion sort.
    These runs are then merged together in a specific order to get the sorted list.
    """
    minrun = calculate_minrun(arr)  # Calculate the minimum run size based on data variance.
    n = len(arr)

    # Sort individual runs using insertion sort.
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(arr, start, end)

    # Merge runs.
    size = minrun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)
            if mid < right:
                arr[left:right + 1] = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
        size *= 2


# Calculate the minimum run size based on the variance of the data.
def calculate_minrun(arr):
    """
    Calculates the minimum run size for Timsort
    It uses the variance of the data to determine the optimal run size.
    A high variance means the data is spread out, and a smaller run size is preferred.
    A low variance means the data is close together, and a larger run size is preferred.
    """
    variance = calculate_variance(arr)  # Calculate the variance of the list.
    max_minrun = 32  # Set a maximum value for the minimum run size.
    if variance > 0.5:
        return max_minrun // 2
    else:
        return max_minrun


# Calculate the variance of a list of numbers.
def calculate_variance(arr):
    """
    This function calculates the variance of a list of numbers.
    Variance is a measure of how spread out the numbers in the list are.
    A high variance means the numbers are spread out, and a low variance means they are close together.
    """
    mean = sum(arr) / len(arr)  # Calculate the mean of the list.
    # Calculate the sum of squared differences from the mean.
    return sum((x - mean) ** 2 for x in arr) / len(arr)



# Generate a random list of integers for testing
arr = [random.randint(1, 1000) for _ in range(1000)]


# Example usage
print("Original array:", arr)
# Measure the execution time
start_time = time.time()
custom_timsort(arr)  # Sort the list using the custom Timsort algorithm.
end_time = time.time()
execution_time = end_time - start_time
print("Sorted array:", arr)


# Measure the memory usage
mem_usage = asizeof.asizeof(arr)
print("Execution time: {:.6f} seconds".format(execution_time))
print("Memory usage: {:.2f} MB".format(mem_usage / (1024 * 1024)))

