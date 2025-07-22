from collections import deque
import time

queue = deque()

def enqueue(element):
  queue.append(element)

def dequeue():
  if queue:
    return queue.popleft()
  else:
    return None
  
def peek():
  if queue:
    return queue[0]
  else:
    return None
  
def is_empty():
  return len(queue) == 0

def size():
  return len(queue)

def clear():
  queue.clear()

def print_queue():
  print(list(queue))

# Example usage
enqueue(1)
enqueue(2)
enqueue(3)
print_queue()  # Output: [1, 2, 3]
print(dequeue())  # Output: 1
print(peek())  # Output: 2
print(is_empty())  # Output: False
print(size())  # Output: 2
clear()
print(is_empty())  # Output: True
print_queue()  # Output: []
enqueue(4)
print_queue()  # Output: [4]
enqueue(5)
enqueue(6)
print_queue()  # Output: [4, 5, 6]  

# Printer Queue Example
printer_queue = deque()

def add_to_printer_queue(document):
  printer_queue.append(document)

def print_document():
  while printer_queue:
    job = printer_queue.popleft()
    print(f"Currently printing: {job}")

    for i in range(3, 0, -1):
      print(f"{job} will be complete in {i} seconds...", end='\r')
      time.sleep(1)
    
  print()

  assert not printer_queue, "The printer queue should be empty after all tasks have been performed"
  # assert len(printer_queue) == 0
  print("All tasks have been performed!")

# Usage for printer queue
add_to_printer_queue("Document1")
add_to_printer_queue("Document2")
add_to_printer_queue("Picture1")
print_document()