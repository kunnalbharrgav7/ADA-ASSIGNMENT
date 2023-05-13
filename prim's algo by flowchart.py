#  Implement Prim's algorithm to find the minimum spanning tree of a given graph in flowchart.

Start
   Input: graph G, starting vertex s
   
   Let S be the set of vertices in the minimum spanning tree, initially S = {s}
   Let T be the set of edges in the minimum spanning tree, initially T = {}

   While S != V (the set of all vertices in G)
      Let e be the minimum weight edge with one endpoint in S and the other endpoint not in S
      Add e to T
      Add the endpoint of e not in S to S
   
   Output: The set of edges T
   
End
