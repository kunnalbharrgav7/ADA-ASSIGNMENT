#  Implement a divide-and-conquer algorithm for finding the maximum subarray sum of a given array of integers.

def max_subarray_sum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    mid = n // 2
    left_sum = max_subarray_sum(arr[:mid])
    right_sum = max_subarray_sum(arr[mid:])
    cross_sum = max_crossing_sum(arr, mid)
    return max(left_sum, right_sum, cross_sum)

def max_crossing_sum(arr, mid):
    left_sum = float('-inf')
    right_sum = float('-inf')
    curr_sum = 0
    for i in range(mid-1, -1, -1):
        curr_sum += arr[i]
        left_sum = max(left_sum, curr_sum)
    curr_sum = 0
    for i in range(mid, len(arr)):
        curr_sum += arr[i]
        right_sum = max(right_sum, curr_sum)
    return left_sum + right_sum
