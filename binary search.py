#  Implement a binary search algorithm for an array of integers.


def binary_search(arr, target):
    """
    Search for the index of the target in the array using binary search.

    Args:
        arr (list of int): the sorted array to search in.
        target (int): the target value to find.

    Returns:
        int: the index of the target in the array, or -1 if it's not found.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
