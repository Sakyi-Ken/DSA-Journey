def alt_binary_search_iterative(data, target):
  left, right = 0, len(data) - 1
  while left <= right:
    mid = (left + right) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

def alt_binary_search_recursive(data, target, left=0, right=None):
  if right is None:
    right = len(data) - 1
  if left > right:
    return -1
  mid = (left + right) // 2
  if data[mid] == target:
    return mid
  elif data[mid] < target:
    return alt_binary_search_recursive(data, target, mid + 1, right)
  else:
    return alt_binary_search_recursive(data, target, left, mid - 1)
  
def binary_search_iterative(data, target):
  low = 0
  high = len(data)
  while high - low > 1:
    mid = (low + high) // 2
    if target < data[mid]:
      high = mid
    else:
      low = mid
  return low if data[low] == target else None

def binary_search_recursive(data, target, low=0, high=None):
  if high is None:
    high = len(data)
  if high - low <= 1:
    return low if data[low] == target else None
  mid = (low + high) // 2
  if target < data[mid]:
    return binary_search_recursive(data, target, low, mid)
  else:
    return binary_search_recursive(data, target, mid, high)

def binary_search_recursive2(data, target, low=0, high=None):
  if high is None:
    high = len(data)
  if low >= high:
    return None
  mid = (low + high) // 2
  if data[mid] == target:
    return mid
  elif data[mid] < target:
    return binary_search_recursive2(data, target, mid, high)
  else:
    return binary_search_recursive2(data, target, low, mid)
  
def binary_search_iterative2(data, target):
  low, high = 0, len(data)
  while low < high:
    mid = (low + high) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      low = mid
    else:
      high = mid
  return None if low >= len(data) or data[low] != target else low

def binary_search_iterative3(data, target):
  low, high = 0, len(data) - 1
  while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return None if low >= len(data) or data[low] != target else low

def custom_binary_search(data, target):
  low, high = 0, len(data)
  while high - low > 1:
    mid = (low + high) // 2
    if target < data[mid]:
      high = mid
    elif target > data[mid]:
      low = mid
    else:
      return mid
  return low if data[low] == target else None

product_prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def search_price(customer_query):
  result = custom_binary_search(product_prices, customer_query)
  if result is not None:
    print(f"Product of price ${customer_query} is found at position {result} in the list.")
    return f"Price found: {product_prices[result]}"
  else:
    print(f"No product is found with price ${customer_query}.")
  return "Price not found."

search_price(30)  # Example usage
search_price(25)  # Example usage



