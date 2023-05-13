# Create a flowchart for a dynamic programming algorithm that solves the
longest common substring problem

1.Create a matrix of size (m+1)x(n+1), where m and n are the lengths of the two strings to be compared.
2.Initialize all the values in the matrix to 0.
3.For each value in the matrix, if the characters at the corresponding positions in the two strings are the same, set the value to be the value in the top-left diagonal cell plus 1.
4.Keep track of the maximum value seen so far and the corresponding indices in the matrix.
5.Once all values have been calculated, the longest common substring can be obtained by starting at the maximum value and backtracking diagonally until a cell with value 0 is reached.
6.Return the substring obtained by concatenating the characters from the start position to the end position.

This algorithm has a time complexity of O(mn) and a space complexity of O(mn), where m and n are the lengths of the input strings.










