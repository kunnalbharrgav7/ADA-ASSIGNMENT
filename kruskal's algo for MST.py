#  Implement Kruskal's algorithm to find the minimum spanning tree of a given graph in Python.

# Define a class to represent each edge in the graph
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
 
# Define a class to represent the graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
 
    def add_edge(self, src, dest, weight):
        self.graph.append(Edge(src, dest, weight))
 
    # Find the parent of a given vertex
    def find_parent(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find_parent(parent, parent[vertex])
 
    # Union two sets using rank
    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)
 
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
 
    # Kruskal's algorithm
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda edge: edge.weight)
        parent = []
        rank = []
 
        # Create a parent and rank array
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
 
        while e < self.vertices - 1:
            edge = self.graph[i]
            i += 1
            x = self.find_parent(parent, edge.src)
            y = self.find_parent(parent, edge.dest)
 
            if x != y:
                e += 1
                result.append(edge)
                self.union(parent, rank, x, y)
 
        # Print the minimum spanning tree
        for edge in result:
            print(f"{edge.src} - {edge.dest}: {edge.weight}")
 
# Driver code
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.kruskal()

