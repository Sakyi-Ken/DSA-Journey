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