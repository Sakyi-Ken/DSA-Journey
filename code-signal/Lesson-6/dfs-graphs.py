def DFS(graph, start, visited):
  visited.add(start)
  print(start, end=' ')
  
  for next_node in graph[start]:
    if next_node not in visited:
      DFS(graph, next_node, visited)

graph = {
  'A': set(['B', 'C']),
  'B': set(['A', 'D', 'E']),
  'C': set(['A']),
  'D': set(['B']),
  'E': set(['B']),
}

visited = set()
DFS(graph, 'A', visited)  # Output: A B D E C