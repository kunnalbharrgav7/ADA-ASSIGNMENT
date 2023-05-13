# Implement a branch and bound algorithm for the Traveling Salesman Problem.


import numpy as np
import itertools

def tsp_branch_and_bound(dist_matrix):
    n = len(dist_matrix)
    # Initialize the priority queue with the root node
    pq = [(0, [0], set([0])) # (lower_bound, path, visited)
    best_path = None
    best_cost = np.inf
    while pq:
        # Pop the node with the lowest lower bound
        lower_bound, path, visited = pq.pop(0)
        # Check if this node can lead to a better solution than the best found so far
        if lower_bound >= best_cost:
            continue
        # Check if the path is a complete tour
        if len(path) == n:
            # Compute the cost of the tour and update the best solution if needed
            cost = sum(dist_matrix[path[i-1], path[i]] for i in range(1, n))
            if cost < best_cost:
                best_path = path
                best_cost = cost
            continue
        # Generate all possible extensions of the current path
        for i in range(n):
            if i not in visited:
                # Compute the lower bound for the extension
                extension_lb = lower_bound + np.min(dist_matrix[path[-1], :]) + np.min(dist_matrix[:, i])
                # Add the extension to the priority queue
                pq.append((extension_lb, path + [i], visited | set([i])))
        # Sort the priority queue by increasing lower bound
        pq.sort()
    return best_path, best_cost
