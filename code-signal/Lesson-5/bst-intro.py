class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

# Manual input
root = Node(5)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)

def insert(root, key):
  if root is None:
    return Node(key)
  else:
    if root.value < key:
      root.right = insert(root.right, key)
    else:
      root.left = insert(root.left, key)
  return root

def insert_BST(root, node):
  if root is None:
    root = node
    return
  elif root.value > node.value:
    if root.left is None:
      root.left = node
    else:
      insert_BST(root.left, node)
  else:
    if root.right is None:
      root.right = node
    else:
      insert_BST(root.right, node)  

def search(root, key):
  if root is None or root.value == key:
    return root
  if root.value < key:
    return search(root.right, key)
  return search(root.left, key)

def in_order_traversal(root):
  if root:
    in_order_traversal(root.left)
    print(root.value, end=" -> ")
    in_order_traversal(root.right)

def minValueNode(node):
  # This function finds the node with the smallest value in a BST
  current = node
  while current.left is not None:
    current = current.left
  return current

def maxValueNode(node):
  current = node
  while current.right is not None:
    current = current.right
  return current

def deleteNode(root, key):
  if root is None:
    return root
  
  if key < root.value:
    root.left = deleteNode(root.left, key)
  elif key > root.value:
    root.right = deleteNode(root.right, key)
  else:
    # If the key is equal to the root's value, then this is the node to be deleted

    # If a node with only one child or no child,
    # the root's right child replaces the root if the left does not exist
    if root.left is None:
      temp = root.right
      root = None
      return temp
    elif root.right is None:
      temp = root.left
      root = None
      return temp
    
    # If node has two children, get the inorder successor (smallest in the right subtree)
    temp = minValueNode(root.right)
    # temp = maxValueNode(root.left)

    # Copy the inorder successor's content to this node
    root.value = temp.value

    # Delete the inorder successor
    root.right = deleteNode(root.right, temp.value)
  return root

# Driver Code:
root = Node(6)
insert_BST(root, Node(8))
insert_BST(root, Node(2))
insert_BST(root, Node(5))
insert_BST(root, Node(4))
insert_BST(root, Node(9))
print("In-order traversal:")
in_order_traversal(root)
print("In-order traversal after deleting:")
root = deleteNode(root, 2)
in_order_traversal(root)