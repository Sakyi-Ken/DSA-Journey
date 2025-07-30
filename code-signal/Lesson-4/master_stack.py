# Problem 1: Previous Value Finder
def find_previous_value(stack, current_value): #copilot solution
  # Create a temporary stack to hold popped values
  temp_stack = []
  found = False

  # Pop elements from the original stack
  while stack:
    value = stack.pop()
    if value == current_value:
      found = True
      break
    temp_stack.append(value)

  # Push the popped values back onto the original stack
  while temp_stack:
    stack.append(temp_stack.pop())

  # If the current value was found, return the previous value
  if found and stack:
    return stack[-1]
  return None

def findSmallerPreceeding(numbers):
  result = [-1]
  stack = []
  for num in numbers:
    while stack and stack[-1] >= num:
      stack.pop()
    result.append(stack[-1] if stack else -1)
    stack.append(num)
  return result[1:]

# Example usage
print(findSmallerPreceeding([2, 5, 1, 3, 4]))  # Output: [-1, 2, -1, 1, 3]

# Problem 2: Stack Minimizer
# Works as Stack but supports a special feature that allows
# Retrieving the minimum value in the stack.
class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []

    def push(self, value):
      self.stack.append(value)
      if not self.min_stack or value <= self.min_stack[-1]:
        self.min_stack.append(value)
    
    def pop(self):
      if self.stack:
        if self.stack[-1] == self.min_stack[-1]:
          self.min_stack.pop()
        return self.stack.pop()

    def top(self):
      return self.stack[-1] if self.stack else None

    def get_min(self):
      return self.min_stack[-1] if self.min_stack else None

# Problem4: Temperature Tracker
def days_until_cooler(temps):
  result = [0] * len(temps)
  stack = []

  # You are given a list of temperature, and you need to find out how many days it 
  # will take until a cooler temperature occurs for each day.
  # For each day, you will track the number of days until a cooler temperature occurs.
  # A cooler temperature is lesser than a higher temperature.
  # We have two ways to do this:
  # 1. Starting from the left, before you'd get a cooler day, the current value should be greater than the preceeding value.
  # 2. Beginning from the right, the current value should be lesser than the previous value.
  # If there is no cooler temperature, return -1 for that day.
  # For example, for the input [30, 60, 90, 120, 60, 30], the output should be [-1, 4, 2, 1, 1, -1].

  # Method 1
  for i in range(len(temps) -1, -1, -1):
    while stack and temps[stack[-1]] >= temps[i]:
      stack.pop()
    # if stack:
    #   result[i] = stack[-1] - i
    #   stack.append(i)
    # else:
    #     stack.append(i)
    result[i] = stack[-1] - i if stack else -1
    stack.append(i)
  return result

  # Method 2
  # for i, temp in enumerate(temps):
  #   while stack and temps[stack[-1]] > temp:
  #     j = stack.pop()
  #     result[j] = i - j
  #   stack.append(i)
  #   return result
  
  # Method 3
    # for i in range(len(temps)):
    #   result[i] = 0
    #   for j in range(i + 1, len(temps)):
    #     if temps[j] < temps[i]:
    #       result[i] = j - i
    #       break

  # return result

# Example usage
print(days_until_cooler([30, 60, 90, 120, 60, 30]))  # Expected: [-1, 4, 2, 1, 1, -1]
print(days_until_cooler([100, 95, 90, 85, 80, 75]))  # Expected: [1, 1, 1, 1, 1, -1]
print(days_until_cooler([1]))  # Expected: [-1]