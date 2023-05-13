# Implement Depth First Search (DFS) algorithm to traverse a graph and find connected components in  Python.

from typing import List, Dict

def dfs(graph: Dict[int, List[int]], start: int, visited: List[bool], connected: List[int]):
    """
    Performs a depth first search (DFS) traversal of a graph starting from a given vertex.
    Marks the visited vertices and adds them to the connected component list.
    """
    visited[start] = True
    connected.append(start)

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, connected)


def find_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Finds all connected components in an undirected graph using Depth First Search (DFS).
    Returns a list of connected component lists.
    """
    n = len(graph)
    visited = [False] * n
    connected_components = []

    for vertex in range(n):
        if not visited[vertex]:
            connected = []
            dfs(graph, vertex, visited, connected)
            connected_components.append(connected)

    return connected_components

