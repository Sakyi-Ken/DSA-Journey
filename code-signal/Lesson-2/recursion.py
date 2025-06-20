# Problem1: Fibonacci Sequence
# Naive Recursion Solution
def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n - 1) + fib(n - 2)

# Trace for memoization
def fibo_trace(n, computed = {0: 0, 1: 1}, depth=0):
  indent = "  " * depth
  if n not in computed:
    print(f"{indent}Computing fibo({n})")
    computed[n] = fibo_trace(n - 1, computed, depth+1) + fibo_trace(n - 2, computed, depth+1)
  else:
    print(f"{indent}Using cached fibo({n}) = {computed[n]}")
  return computed[n]

# Trace for iteration
def fib_iter_trace(n):
  print(f"fib_iter({n}):")
  if n <= 1:
    print(f"  Return {n}")
    return n
  a, b = 0, 1
  print(f"  a=0, b=1")
  for i in range(2, n + 1):
    a, b = b, a + b
    print(f"  i={i}: a={a}, b={b}")
  return b

# Example usage
if __name__ == "__main__":
  n = 10
  print("Memoization trace:")
  result_memo = fibo_trace(n)
  print(f"Result (Memoization): {result_memo}\n")

  print("Iterative trace:")
  result_iter = fib_iter_trace(n)
  print(f"Result (Iterative): {result_iter}")
  
# Efficient Solution using Memoization
def fibo(n, computed = {0: 0, 1: 1}):
  if n not in computed:
    computed[n] = fibo(n - 1, computed) + fibo(n - 2, computed)
  return computed[n]

# Example usage
if __name__ == "__main__":
  n = 10
  print(f"Fibonacci of {n} (Naive): {fib(n)}")  # Output: 55
  print(f"Fibonacci of {n} (Memoization): {fibo(n)}")  # Output: 55

# Problem 2: Summing Array Elements
def arraySum(arr, index=0): 
  if index == len(arr): 
    return 0 
  else:
    return arr[index] + arraySum(arr, index + 1)
  
def alt_arraySum(arr):
  if not arr:
    return 0
  return arr[0] + alt_arraySum(arr[1:])

def alt_arraySum_iter(arr):
  total = 0
  for num in arr:
    total += num
  return total

def alt_arraySum_iter2(arr):
  return sum(arr)

def alt_arraySum_iter3(arr):
  total = 0
  for i in range(len(arr)):
    total += arr[i]
  return total

# Example usage for array sum
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  print(f"Recursive sum: {arraySum(arr)}")  # Output: 15
  print(f"Alternative recursive sum: {alt_arraySum(arr)}")  # Output: 15
  print(f"Iterative sum: {alt_arraySum_iter(arr)}")  # Output: 15
  print(f"Built-in sum: {alt_arraySum_iter2(arr)}")  # Output: 15
  print(f"Iterative sum with index: {alt_arraySum_iter3(arr)}")  # Output: 15

# Problem 3: Factorial Calculation
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n -1)

def factorial_iter(n):
  if n == 0 or n == 1:
    return 1
  result = 1
  for i in range(2, n + 1):
    result *= i
  return result

def alt_factorial(num):
  if num < 0:
    return None
  elif num == 0 or num == 1:
    return 1
  else:
    return num * alt_factorial(num - 1)

def factorials(nums):
  results = []
  for num in nums:
    fact = alt_factorial(num)
    if fact is not None:
      results.append(fact)
    else:
      results.append('Error')
  return results

# Example usage for factorial
if __name__ == "__main__":
  n = 5
  print(f"Factorial of {n} (Recursive): {factorial(n)}")  # Output: 120
  print(f"Factorial of {n} (Iterative): {factorial_iter(n)}")  # Output: 120
  nums = [0, 1, 2, 3, 4, 5]
  print(f"Factorials of {nums}: {factorials(nums)}")  # Output: [1, 1, 2, 6, 24, 120]