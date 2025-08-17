# Problem 1: Checking the Balance of a Binary Search Tree
# The tree is balanced if for each vertex, the size of the left subtree differs from the size of the right subtree by at most 1.
# This solution performs with O(n) time complexity, where n is the number of nodes in the tree, as each node is visited only once.

# def is_balanced(root):
#     def check_balance(node):
#         if not node:
#             return 0
#         left_height = check_balance(node.left)
#         right_height = check_balance(node.right)
#         if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
#             return -1
#         return max(left_height, right_height) + 1
#     return check_balance(root) != -1

def is_balanced(root) -> bool:
  def check_balance(node):
    if node is None:
      return 0, True
    
    left_height, left_balanced = check_balance(node.left)
    if not left_balanced:
      return -1, False

    right_height, right_balanced = check_balance(node.right)
    if not right_balanced:
      return -1, False
    
    height = max(left_height, right_height) + 1
    is_balanced = abs(left_height - right_height) <= 1
    return height, is_balanced
  
  height, balanced = check_balance(root)
  return balanced

  #   is_balanced = abs(left_height - right_height) <= 1
  #   current_height = 1 + max(left_height, right_height)
  #   return current_height, is_balanced

  # _, balanced = check_balance(root)
  # return balanced


# Problem 2: Identify the K-th Smallest Element in a Binary Search Tree
# This approach has O(k) time complexity, as we visit at most k vertices in the tree.
# This approach uses inorder traversal
# In order traversal prints all nodes in ascending order.
def kth_smallest(root, k):
  stack = []
  current = root
  while current is not None or stack:
    while current is not None:
      stack.append(current)
      current = current.left
    current = stack.pop()
    k -= 1
    if k == 0:
      return current.val
    current = current.right
  return None

def kthSmallest(root, k):
  # The number of nodes in the left subtree of the root
  left_nodes = countNodes(root.left) if root else 0

  # If K is equal to the number of nodes in the left subtree plus 1,
  # That means we must return the root's value as we've reached the k-th smallest
  if k == left_nodes + 1:
    return root.val
  # If there are more than k nodes in the left subtree,
  # we need to search in the left subtree.
  elif k <= left_nodes:
    return kthSmallest(root.left, k)
  # If there are less than k nodes in the left subtree,
  # The k-th smallest must be in the right subtree.
  else:
    return kthSmallest(root.right, k - 1 - left_nodes)
  
def countNodes(root):
  if not root:
    return 0
  return 1 + countNodes(root.left) + countNodes(root.right)

class AugmentedTreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.size = 1  # size of subtree rooted at this node

def update_size(node):
  if node:
    node.size = 1
    if node.left:
      node.size += node.left.size
    if node.right:
      node.size += node.right.size

def insert_augmented(root, val):
  if not root:
    return AugmentedTreeNode(val)
  if val < root.val:
    root.left = insert_augmented(root.left, val)
  else:
    root.right = insert_augmented(root.right, val)
  update_size(root)
  return root

def kthSmallest(root, k):
  if not root:
    return None
  left_size = root.left.size if root.left else 0
  if k == left_size + 1:
    return root.val
  elif k <= left_size:
    return kthSmallest(root.left, k)
  else:
    return kthSmallest(root.right, k - left_size - 1)

# Example usage
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(7)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(8)

# print(is_balanced(root))  # Output: True
# print(kth_smallest(root, 3))  # Output: 4
# print(kthSmallest(root, 3))

root = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(5)

print(is_balanced(root))  # Output: False
print(kth_smallest(root, 2))  # Output: 3
print(kthSmallest(root, 3))  # Output: 4

# Problem 4: Finding max height difference for every node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def max_height_diff(root):
  def height(node):
    if not node:
      return 0, 0
    left_height, diff_left = height(node.left)
    right_height, diff_right = height(node.right)
    
    node_height = 1 + max(left_height, right_height)
    diff_height = abs(left_height - right_height)
    max_diff = max(diff_height, diff_left, diff_right)
    
    return node_height, max_diff
        
  if root is None:
    return 0, 0
  left_height, diff_left = height(root.left)
  right_height, diff_right = height(root.right)
  diff_height = abs(left_height - right_height)
  max_height = max(diff_height, diff_left, diff_right)
  return max_height 

# Test samples
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)

print(max_height_diff(root)) # Expected output: 1

# Problem 5: Finding the K-th Largest Element in a Binary Search Tree
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def kthLargest(root, k):
  right_nodes = countNodes(root.right) if root else 0
  
  if k == right_nodes + 1:
    return root.val
  elif k <= right_nodes:
    return kthLargest(root.right, k)
  else:
    return kthLargest(root.left, k - 1 - right_nodes)

    
def countNodes(root):
  if not root:
    return 0
  return 1 + countNodes(root.right) + countNodes(root.left)

# Creating the BST
root = Node(50) 
root.left = Node(20)
root.right = Node(60) 
root.left.left = Node(10) 
root.left.right = Node(30)
root.right.left = Node(55)
root.right.right = Node(70)
root.left.right.left = Node(25)
root.left.right.right = Node(35)
root.right.right.left = Node(65)
root.right.right.right = Node(80)

# Now, let's test the function with the new binary tree
print(kthLargest(root, 1))  # Expected output: 80
print(kthLargest(root, 5))  # Expected output: 55
print(kthLargest(root, 10))  # Expected output: 20
print(kthLargest(root, 3))  # Expected output: 65
print(kthLargest(root, 7))  # Expected output: 35