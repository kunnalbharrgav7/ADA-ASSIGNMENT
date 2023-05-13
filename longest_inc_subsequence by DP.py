# Develop a dynamic programming algorithm to find the longest increasing subsequence in  Python.


def find_lis(arr):
    """
    This function takes an array of integers as input and returns the length of the longest increasing subsequence
    """
    n = len(arr)
    lis = [1] * n  # initialize LIS array with 1's
    
    # Find LIS for each element in the array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Return the maximum value in the LIS array
    return max(lis)
