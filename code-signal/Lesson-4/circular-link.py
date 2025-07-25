# Python program to create a circular linked list

# Node class
class Node:
  # Constructor to initialize the node
  def __init__(self, data):
    self.data = data
    self.next = None

# Class to form a Circular LinkedList with basic operations
class CircularLinkedList:
    
  # Constructor to initialize the linked list
  def __init__(self):
    self.head = None
  
  # Function to add new node to the end of Circular Linked List
  def append(self, data):
    if not self.head:
      self.head = Node(data)
      self.head.next = self.head
    else:
      new_node = Node(data)
      cur = self.head
      while cur.next != self.head:
        cur = cur.next
      cur.next = new_node
      new_node.next = self.head
    
    # Function to display all nodes of Circular LinkedList
  def display(self):
    nodes = []
    cur = self.head
    cycle_count = 0
    while True:
      nodes.append(cur.data)
      if cur.next == self.head:
        cycle_count += 1
        if cycle_count == 2:
          break
      cur = cur.next
    print(" -> ".join(map(str, nodes)))

  # Deleting a node
  def delete(self, data):
    if self.head is None:
      return
    if self.head.data == data:
      if self.head.next == self.head:
        self.head = None
      else:
        last = self.head
        while last.next != self.head:
          last = last.next
        last.next = self.head.next
        self.head = self.head.next
      return
    
    temp = self.head
    prev = None
    while True:
      if temp.data == data:
        prev.next = temp.next
        return
      prev = temp
      temp = temp.next
      if temp == self.head:
        break
    print("Node not found")

  # if self.head is None:
  #     return
    
  #   temp = self.head
  #   prev = None

    # while True:
    #   if temp.data == data:
    #     if prev is None:
    #       if temp.next == self.head:
    #         self.head = None
    #       else:
    #         last = self.head
    #       while last.next != self.head:
    #         last = last.next
    #         self.head = temp.next
    #         last.next = self.head
    #     else:
    #       prev.next = temp.next
    #       return
    #   prev = temp
    #   temp = temp.next
    #   if temp == self.head:
    #     break
    # print("Node not found")

clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.display()  # Expected output: 1 -> 2 -> 3 -> 1 -> 2 -> 3
clist.delete(2)
clist.display()  # Expected output: 1 -> 3 -> 1 -> 3
clist.delete(1)
clist.display()  # Expected output: 3 -> 3
