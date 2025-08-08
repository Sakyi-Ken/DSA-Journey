from collections import deque

def BFS(tree, root):
  visited = set() # Set to keep track of visited nodes
  visit_order = [] # List to keep visited nodes in order they are visited  
  queue = deque() # A queue to add nodes for visiting

  level = {root: 0}

  queue.append(root) # We will start at the root 

  while queue: # While there are nodes to visit
    node = queue.popleft() # Visit the first node in the queue
    visit_order.append(node) # Add it to the list of the visited nodes
    visited.add(node) # And mark as visited

    level_of_node = level[node]

    # Now add all unvisited children to the queue
    for child in tree[node]:
      if child not in visited:
        queue.append(child)
        level[child] = level_of_node + 1
        
  return (visit_order, level) # Return the order of visited nodes and their levels

# Tree definition
tree = {
  'A' : ['B', 'C', 'D'],
  'B' : ['A', 'E'],
  'C' : ['A', 'F','G'],
  'D' : ['A', 'H'],
  'E' : ['B', 'I'],
  'F' : ['C'],
  'G' : ['C', 'J'],
  'H' : ['D'],
  'I' : ['E'],
  'J' : ['G']
}

print(BFS(tree, 'A'))
# Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']