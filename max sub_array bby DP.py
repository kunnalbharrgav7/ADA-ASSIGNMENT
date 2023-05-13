# Implement a dynamic programming algorithm to find the maximum sum subarray in Python

def max_sum_subarray(arr):
    """
    Returns the maximum sum subarray and its sum using dynamic programming.
    """
    n = len(arr)
    max_sum = arr[0]
    current_sum = arr[0]
    start_index = end_index = 0

    for i in range(1, n):
        if current_sum + arr[i] > arr[i]:
            current_sum += arr[i]
        else:
            current_sum = arr[i]
            start_index = i

        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i

    return arr[start_index:end_index + 1], max_sum
