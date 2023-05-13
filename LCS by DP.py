# Implement the longest common subsequence problem using dynamic programming in  Python.
Analyze the time and space complexity of your implementation and compare it with the time and space complexity of a naive recursive implementation.

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    # create a 2D array to store the length of the longest common subsequence
    lcs_length = [[0] * (n+1) for i in range(m+1)]
 
    # loop through the strings to populate the lcs_length array
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                lcs_length[i][j] = lcs_length[i-1][j-1] + 1
            else:
                lcs_length[i][j] = max(lcs_length[i-1][j], lcs_length[i][j-1])
 
    # build the longest common subsequence using the lcs_length array
    lcs_string = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_string = str1[i-1] + lcs_string
            i -= 1
            j -= 1
        elif lcs_length[i-1][j] > lcs_length[i][j-1]:
            i -= 1
        else:
            j -= 1
 
    return lcs_string


The time complexity of this implementation is O(mn), where m and n are the lengths of the two input strings, because we loop through each character of each string once. The space complexity is also O(mn) because we create a 2D array of that size to store the length of the longest common subsequence.

In contrast, a naive recursive implementation of the longest common subsequence problem would have a time complexity of O(2^n), where n is the length of the shorter of the two input strings. This is because the recursive function would need to consider all possible combinations of characters from both strings. The space complexity of the naive recursive implementation would also be O(n) due to the recursive call stack.

Therefore, the dynamic programming implementation is much more efficient than the naive recursive implementation.
