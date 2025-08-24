# Graphs
**Adjacency Matrix** in essence, it is a square matrix, a two-dimensional array, where each cell (i, j) signifies the weight of the edge between vertices i and j in the graph.

## DFS GRAPH
DFS is an algorithmic solution for traversing or searching through data structures or graph nodes by diving deeper through a graph branch before backtracking when all nodes are visited.

### DFS Space and Time Complexity
`Time complexity is O(V + E) and Space is O(V)` where V indicates number of vertices and E represents the number of edges (connections between vertices).
1. Mark the current node as 'visited' and print the node.
2. For every adjacent unvisited node of the current node:
2.1. Invoke the recursive DFS function.

_In terms of time efficiency, DFS thrives on densely connected graphs where the probability of finding the target quickly exceeds that of BFS._

`However, all tools have their limitations and nuances. DFS does not perform optimally in problems necessitating the shortest path, such as GPS routing problems, where BFS is a superior choice. Additionally, DFS requires careful management when dealing with cycles within the graph, as it could end up in an infinite loop without effective control over the visited nodes.`

_In a graph, a cycle exists if we can start at a node, traverse along the edges, and return to the same node without retracing any edge._