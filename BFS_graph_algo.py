# Implement Breadth First Search (BFS) algorithm to find the shortest path between two nodes in a graph in  Python.

from collections import deque

def bfs_shortest_path(graph, start, end):
    # create a queue for BFS
    queue = deque()
    # add the starting node to the queue
    queue.append(start)
    # keep track of visited nodes
    visited = set()
    visited.add(start)
    # keep track of the parent node for each node
    parent = {}
    parent[start] = None

    # loop until the queue is empty
    while queue:
        # remove the first node from the queue
        current_node = queue.popleft()
        # if we have reached the end node, return the path
        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return list(reversed(path))

        # explore the neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)

    # if we reach here, there is no path between the nodes
    return None

