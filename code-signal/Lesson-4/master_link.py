class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def LinkedList_reverseTraversal(self):
    node = self.head
    stack = []
    while node is not None:
      stack.append(node.data)
      node = node.next
    while stack:
      print(stack.pop(), end=" => ")

  def LinkedList_length(self):
    current_node = self.head
    length = 0 
    while current_node is not None:
      length  += 1
      current_node = current_node.next
    return length