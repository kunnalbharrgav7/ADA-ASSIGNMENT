# . Implement a linear search algorithm for an array of integers

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

Here's an example of how to use this function:

arr = [5, 3, 8, 4, 2, 9]
target = 4
result = linear_search(arr, target)
if result == -1:
    print("Target value not found in the array.")
else:
    print(f"Target value found at index {result}.")

