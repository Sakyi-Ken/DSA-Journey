# Mastering continuous functions with binary search

# Define a function
def f(x):
  return x * x - 2

# Define the binary search function
def binary_search(target, left, right, precision):
  while right - left > precision:
    mid = (left + right) / 2
    if f(mid) < target:
      left = mid
    else:
      right = mid
  return left 

# Example usage
epsilon = 1e-6
result = binary_search(0, 1, 2, epsilon)
print("x for which f(x) is approximately 0:", result)