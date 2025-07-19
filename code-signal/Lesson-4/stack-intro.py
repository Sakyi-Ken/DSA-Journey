# Create an empty stack
stack = []

# Push elements 
stack.append('A')
stack.append('B')
stack.append('C')

print("Stack after pushing elements:", stack)

# Pop an element
topElement = stack.pop()
print(f"Popped element: {topElement}")

# New top of the stack
newTopElement = stack[-1] if stack else None
print(f"Top Element after Pop: {newTopElement}")

def is_empty(stack):
  return len(stack) == 0

# Create an empty stack
stack = []
print(is_empty(stack))

stack.append('D')

print(is_empty(stack))

stack.append('E')

stack_size = len(stack)
print(f"Stack size: {stack_size}")

# Create a stack to store text changes
# The stack stores all historical versions of editor states, excluding the current state
text_stack = []

# The user inputs text
text_stack.append("Initial text")
text_stack.append("Hello, world!")
text_stack.append("Hello, CodeSignal!")
text_stack.append("Added more text")
text_stack.append("Edited text")
text_stack.append("Final text")

print(text_stack)

# Check if the stack is empty before performing "undo"
if not is_empty(text_stack):
  # The user performs an "undo" operation
  previous_text = text_stack.pop() # Retrieve the last historic change
  print(f'After "undo", the text is {previous_text}')
else:
  print("Cannot perform undo operation. There are no historic changes.")


# Assortment of Practice Exercises
class Stack:
  def __init__(self):
    self.stack = []
    self.maxSize = 10  # assuming a stack size limit for this example

  def push(self, item):
    if len(self.stack) < self.maxSize:
      self.stack.append(item)
    else:
      print("Stack Overflow. Cannot add more items.")

  def pop(self):
    if len(self.stack) > 0:
      print(f"Pop element: {self.stack[-1]}") 
      return self.stack.pop()
    else:
      print("Stack Underflow. Stack is empty.")
      return None  # return a None value when the stack is empty

  def printStack(self):
    print(self.stack)

# create a Stack object
s = Stack()

# Push elements
for i in range(1, 4): # we deliberately try to add elements in the range 1 to 3
  print(f"Pushing Book {i} into the stack")
  s.push(i)

# Print the stack
print("Stack after pushing elements:")
s.printStack()

# Pop an element
topElement = s.pop()
print(f"Popped book: Book {topElement}")

# Print the stack
print("Stack after popping an element:")
s.printStack()