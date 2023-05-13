#  Implement Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph in  Python.

import heapq

def dijkstra(graph, start, end):
    """
    Finds the shortest path from the start node to the end node in a weighted graph using Dijkstra's algorithm.
    
    Args:
    graph (dict): A dictionary representing the graph, where the keys are nodes and the values are dictionaries
                  representing the edges emanating from that node, where the keys of the inner dictionary are the 
                  destination nodes and the values are the edge weights.
    start (str): The starting node.
    end (str): The ending node.
    
    Returns:
    A tuple containing two elements:
    - The shortest distance from start to end.
    - The path, as a list of nodes, from start to end.
    """
    distances = {node: float('inf') for node in graph}  # Set all distances to infinity initially.
    distances[start] = 0  # Distance from start to start is 0.
    heap = [(0, start)]  # Initialize heap with start node and distance 0.
    visited = set()  # Set of visited nodes.
    previous_nodes = {}  # Dictionary to keep track of the previous node in the shortest path.
    
    while heap:
        (distance, current_node) = heapq.heappop(heap)  # Get node with shortest distance from heap.
        if current_node == end:  # Found shortest path to end node.
            path = []
            while current_node in previous_nodes:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            path.insert(0, start)
            return (distance, path)
        
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))
                    previous_nodes[neighbor] = current_node
    
    return (float('inf'), [])  # No path found.

