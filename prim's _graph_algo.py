# Implement the Prim's algorithm to find the minimum spanning tree of a given graph in Python.

import heapq
from collections import defaultdict

def prim_mst(graph):
    # Initialize the minimum spanning tree and the set of visited vertices
    mst = []
    visited = set()

    # Start with the first vertex in the graph
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)

    # Create a heap to store the edges sorted by weight
    heap = [(weight, start_vertex, dest) for dest, weight in graph[start_vertex].items()]
    heapq.heapify(heap)

    # Loop until all vertices have been visited
    while heap:
        weight, src, dest = heapq.heappop(heap)
        if dest not in visited:
            visited.add(dest)
            mst.append((src, dest, weight))
            for next_dest, next_weight in graph[dest].items():
                if next_dest not in visited:
                    heapq.heappush(heap, (next_weight, dest, next_dest))

    return mst

