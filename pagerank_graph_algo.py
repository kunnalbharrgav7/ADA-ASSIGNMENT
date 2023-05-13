# Implement the PageRank algorithm to rank web pages in a network in Python.

import numpy as np

def pagerank(M, num_iterations=100, d=0.85):
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v /= np.linalg.norm(v, 1)
    for i in range(num_iterations):
        v = d * np.matmul(M, v) + (1 - d) / N
    return v

# Example usage:
# Create an adjacency matrix representing the links between web pages
M = np.array([[0, 1, 1],
              [1, 0, 1],
              [1, 0, 0]])
# Run the PageRank algorithm on the matrix
v = pagerank(M, num_iterations=100, d=0.85)
# Print the resulting PageRank scores for each web page
print(v)
