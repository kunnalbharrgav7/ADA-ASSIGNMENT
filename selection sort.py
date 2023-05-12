# Implement a selection sort algorithm for an array of integers

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


Here's an example usage of the function:>>> arr = [64, 25, 12, 22, 11]
>>> selection_sort(arr)
[11, 12, 22, 25, 64]
