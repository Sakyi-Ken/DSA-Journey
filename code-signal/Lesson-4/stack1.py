# Are Brackets Balanced?
def alt_brackets_balanced(input_str):
  stack = []
  brackets = {'(': ')', '{':'}', '[':']'}
  for char in input_str:
    if char in brackets: # If it's an opening bracket
      stack.append(char)
    elif char in brackets.values():  # If it's a closing bracket
      if not stack or brackets[stack.pop()] != char:
        return False  # Mismatched or unbalanced brackets
      
  return not stack  # If stack is empty, brackets are balanced

def are_brackets_balanced(input_str):
  brackets = set(["(", ")", "{", "}", "[", "]"])
  bracket_map = {"(":")", "{":"}", "[":"]"}
  open_par = set(["(", "[", "{"])
  stack = []

  for character in input_str:
    if character not in brackets:
      # Skipping non-bracket characters
      continue
    if character in open_par:
      stack.append(character)
    elif stack and character == bracket_map[stack[-1]]:
      stack.pop()
    else:
      return False
  return len(stack) == 0

# Example
input_str = "{[()()]}"
print(are_brackets_balanced(input_str))  # Output: True

# Problem 2: Reverse a String
def alt_reverse_string(input_str):
  result = input_str[::-1]  # Using slicing to reverse the string
  return result

def reverse_string(input_str):
  stack = []
  for char in input_str:
    stack.append(char) # Push each character onto the stack
  reversed_str = ''
  while stack:
    reversed_str += stack.pop() # Pop each character from the stack
  return reversed_str

def rev_str(input):
  stack = list(input)
  result = ''

  while len(stack):
    result += stack.pop()
  return result

# Example
input_str = "Hello, World!"
print(reverse_string(input_str))  # Output: !dlroW ,olleH
# Problem 3: Check if a string is a palindrome
def is_palindrome(input_str):
  stack = []
  for char in input_str:
    stack.append(char)  # Push each character onto the stack
  reversed_str = ''
  while stack:
    reversed_str += stack.pop()  # Pop each character from the stack
  return input_str == reversed_str  # Check if original and reversed strings are the same

# Problem 4: Postfix Expression Evaluation
def evaluate_postfix(expression):
  stack = []
  for element in expression.split(" "):
    if element.isdigit(): 
      stack.append(int(element))
    else:
      operand2 = stack.pop()
      operand1 = stack.pop()

      if element == "+":
        stack.append(operand1 + operand2)
      elif element == "-":
        stack.append(operand1 - operand2)
      elif element == "*":
        stack.append(operand1 * operand2)
      elif element == "/":
        stack.append(operand1 / operand2)

  return stack[0]

# Example
postfix_expression = "3 4 + 2 * 7 /"
print(evaluate_postfix(postfix_expression))  # Output: 2.0

def string_end(strng, n):
  stack = list(strng)
  result = ''
  while n:
    result += stack.pop()
    n -= 1
  # for i in range(0, n):
  #   result += stack.pop()
  return result

print(string_end("ijkshgegassem tnatropmi", 17))  # Expected output: important message
print(string_end("ffsfatad", 4))  # Expected output: data
print(string_end("IA", 2))  # Expected output: AI