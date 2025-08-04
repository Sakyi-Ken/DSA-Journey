def dfs(tree, root, visited, traversal):
  traversal.append(root)
  visited.add(root)

  for child in tree[root]:
    if child not in visited:
      dfs(tree, child, visited, traversal)

tree = {
  'A' : ['B', 'C', 'D'],
  'B' : ['A', 'E', 'F'],
  'C' : ['A'],
  'D' : ['A', 'G', 'H'],
  'E' : ['B'],
  'F' : ['B', 'I', 'J'],
  'G' : ['D'],
  'H' : ['D'],
  'I' : ['F'],
  'J' : ['F'],
}

visited = set()
traversal = []
dfs(tree, 'A', visited, traversal)

print(' -> '.join(traversal))


def find_path(tree, start, end, visited, path=[]):
  path = path + [start]
  visited.add(start)
  if start == end:
    return path
  for node in tree[start]:
    if node not in visited:
      new_path = find_path(tree, node, end, visited, path)
      if new_path:
        return new_path
  return None

visited = set()
print(find_path(tree, 'A', 'J', visited))


class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

  # Alt to add
  def add_child(self, child_node):
    self.children.append(child_node) # You do this when you have already created the node
    # self.children.append(Node(child_node)) # You do this when you want to create the node on the fly;
    # For this one when adding you need to utilise indexing 
    # Say, cto_branch = root.children[0]
  
  # Alt for traversing
  def dfs(self, visited=None):
    if visited is None:
      visited = set()
    
    visited.add(self.value)
    print(self.value, end=' -> ')

    for child in self.children:
      if child.value not in visited:
        child.dfs(visited)

def add_edges(tree, node, child_values):
  for value in child_values:
    node.children.append(Node(value))

def dfs(node, visited=None):
  if visited is None:
    visited = set()
  
  visited.add(node.value)
  print(node.value, end=' -> ')

  for child in node.children:
    if child.value not in visited:
      dfs(child, visited)

# Constructing a tree
root = Node('Head Office')
add_edges(root, root, ['Marketing', 'Sales', 'R&D'])

node_marketing = root.children[0]
add_edges(root, node_marketing, ['SEO', 'Content'])

node_sales = root.children[1]
add_edges(root, node_sales, ['Domestic', 'International'])

# Perform DFS traversal
print("DFS Traversal:")
dfs(root)
print("end")