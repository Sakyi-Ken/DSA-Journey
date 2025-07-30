class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # Function to add a node to the beginning of the linked list
  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  # Insertion
  def insert(self, value):
    if self.head is None:
      self.head = Node(value)
      self.tail = self.head
    else:
      new_node = Node(value)
      self.tail.next = new_node
      self.tail = new_node

  # Defining search method
  def search(self, value):
    temp = self.head
    while temp is not None:
      if temp.value == value:
        return True
      temp = temp.next
    return False

  def append(self, data):
    if not self.head:
      self.head = Node(data)
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = Node(data)
    self.size += 1

  def remove(self, data):
    temp = self.head
    prev = None
    while temp:
      if temp.value == data:
        if prev:
          prev.next = temp.next
          self.size -= 1
          return
        else:
          self.head = temp.next
          self.size -= 1
          return
      prev = temp
      temp = temp.next
      

  # Defining delete method
  def delete(self, value):
    temp = self.head    
    if (temp is not None):
      if temp.value == value:
        self.head = temp.next
        temp = None
        return
    
    while (temp is not None):
      if temp.value == value:
        break
      prev = temp
      temp = temp.next
    
    if temp == None:
      return
    prev.next = temp.next
    temp = None

  # Traversal
  def print(self):
    temp = self.head
    while temp is not None:
      print(temp.value, end=" => ")
      temp = temp.next

list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.print() # Output: 1 => 2 => 3 =>
list.delete(2)
list.print() # Output: 1 => 3 =>
print()
list.append(4)
list.append(5)
list.append(6)
list.push(0)
list.print() # Output: 0 => 1 => 3 => 4 => 5 => 6 =>
print()
print("Size of the linked list after insertions: ", list.size)  # Expected output: Size of the linked list after insertions: 4
list.remove(6)
print("Size of the linked list after deletion: ", list.size)  # Expected output: Size of the linked list after deletion: 3
list.print()  # Output: 0 => 1 => 3 => 4 => 5 => 
print()
print("Search for 3 in the linked list: ", list.search(3))  # Expected output: Search for 3 in the linked list: True