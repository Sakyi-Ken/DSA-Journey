# This code defines a single binary tree node class in Python.
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# Creating nodes for the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print("In-order Traversal:")

# In-order traversal of the binary tree
def in_order_traversal(node):
  if node is None:
    return
  in_order_traversal(node.left)  # Visit left subtree
  print(str(node.value) + ' -> ', end='') # Visit root
  in_order_traversal(node.right)  # Visit right subtree
in_order_traversal(root)

print("\nPre-order Traversal:")

# Pre-order traversal of the binary tree
def pre_order_traversal(node):
  if node is None:
    return
  print(str(node.value) + ' -> ', end='') # Visit root
  pre_order_traversal(node.left)  # Visit left subtree
  pre_order_traversal(node.right)  # Visit right subtree
pre_order_traversal(root)

print("\nPost-order Traversal:")

# Post-order traversal of the binary tree
def post_order_traversal(node):
  if node is None:
    return
  post_order_traversal(node.left)  # Visit left subtree
  post_order_traversal(node.right)  # Visit right subtree
  print(str(node.value) + ' -> ', end='')  # Visit root
post_order_traversal(root)

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    self.children.append(child_node)

  def remove_child(self, child_node):
    self.children = [child for child in self.children if child is not child_node]

# Create a Browser History as a Non Binary Tree
browser_history_root = TreeNode("HomePage")

google = TreeNode("Google.com")
youtube = TreeNode("Youtube.com")
codesignal = TreeNode("CodeSignal.com")

browser_history_root.add_child(google)
browser_history_root.add_child(youtube)
browser_history_root.add_child(codesignal)

gmail = TreeNode("Gmail.com")
google.add_child(gmail)

codesignal_tour = TreeNode("CodeSignal.com/Tour")
codesignal_blog = TreeNode("CodeSignal.com/Blog")

codesignal.add_child(codesignal_tour)
codesignal.add_child(codesignal_blog)

print("\nBrowser History Tree:")

def print_history(node): # Using Pre-order traversal
  if node is None:
    return
  else:
    print(f'Visited -> {node.value}')
    for child in node.children:
      print_history(child)

print_history(browser_history_root)

# A non-binary node
class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

# Creating nodes for the tree
root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[2].children = [Node(7)]