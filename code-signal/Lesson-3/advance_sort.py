# Problem 1: Find the K-th Ordinal Statistic in a list.

# Simple solution using sorting.
def find_kth_statistic(values, k):
  if k < 1 or k > len(values):
    raise ValueError("k must be between 1 and the length of the list")
  sorted_values = sorted(values)
  return sorted_values[k - 1]

# Problem 1.1: Find the K-th Ordinal Statistic in a list using Quickselect.
def quickselect(values, k):
    if k < 1 or k > len(values):
      raise ValueError("k must be between 1 and the length of the list")
    
    def partition(left, right, pivot_index): # Takes the pivot from the right
      pivot_value = values[pivot_index]
      values[pivot_index], values[right] = values[right], values[pivot_index]
      store_index = left
      for i in range(left, right):
        if values[i] < pivot_value: # Organize very well when there are duplicates.
          values[store_index], values[i] = values[i], values[store_index]
          store_index += 1
      values[right], values[store_index] = values[store_index], values[right]
      return store_index

    left, right = 0, len(values) - 1
    while left <= right:
      pivot_index = (left + right) // 2
      pivot_index = partition(left, right, pivot_index)
      
      if pivot_index == k - 1:
        return values[pivot_index]
      elif pivot_index < k - 1:
        left = pivot_index + 1
      else:
        right = pivot_index - 1
  
    raise ValueError("k is out of bounds")

# Problem 1.2: Find the K-th Ordinal Statistic in a list using a Binary Search.
def find_kth_statistic_binary_search(values, k):
    if k < 1 or k > len(values):
      raise ValueError("k must be between 1 and the length of the list")
    
    def count_less_equal(x):
      return sum(1 for value in values if value <= x)
    
    left, right = min(values), max(values)
    while left < right:
      mid = (left + right) // 2
      if count_less_equal(mid) < k:
        left = mid + 1
      else:
        right = mid
    
    return left

# Problem 1.3: Find the K-th Ordinal Statistic in a list using a Counting Sort.
def find_kth_statistic_counting_sort(values, k):
  if k < 1 or k > len(values):
    raise ValueError("k must be between 1 and the length of the list")
  
  max_value = max(values)
  count = [0] * (max_value + 1)
  
  for value in values:
    count[value] += 1
  
  current_count = 0
  for i in range(len(count)):
    current_count += count[i]
    if current_count >= k:
      return i
  raise ValueError("k is out of bounds")

# Problem 1.4: Using Quick sort
import random

def find_kth_smallest(numbers, k):
  if numbers:
    pos = partition(numbers, 0, len(numbers) - 1)
    if k - 1 == pos:
      return numbers[pos]
    elif k - 1 < pos:
      # We use numbers[:pos], k because k is the position in the original list,
      # and the left part contains indices 0 to pos-1, so k remains unchanged.
      return find_kth_smallest(numbers[:pos], k)
    else:
      # For the right part, we use numbers[pos + 1:], k - pos - 1 because
      # we have skipped pos + 1 elements, so the k-th smallest is now (k - pos - 1)-th in the right part.
      return find_kth_smallest(numbers[pos + 1:], k - pos - 1)

def partition(nums, l, r): # Takes the pivot from the left.
  # Choosing a random index to make the algorithm less deterministic
  rand_index = random.randint(l, r)
  nums[l], nums[rand_index] = nums[rand_index], nums[l]
  pivot_index = l
  for i in range(l + 1, r + 1):
    if nums[i] < nums[l]:
      pivot_index += 1
      nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
  nums[l], nums[pivot_index] = nums[pivot_index], nums[l]
  return pivot_index

# Problem 2: Count the Number of Inversions in a list.
def count_inversions(values):
  def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0

    while i <= mid and j <= right:
      if arr[i] <= arr[j]:
        temp_arr[k] = arr[i]
        i += 1
      else:
        temp_arr[k] = arr[j]
        inv_count += (mid - i + 1)
        j += 1
      k += 1

    while i <= mid:
      temp_arr[k] = arr[i]
      i += 1
      k += 1

    while j <= right:
      temp_arr[k] = arr[j]
      j += 1
      k += 1

    for i in range(left, right + 1):
      arr[i] = temp_arr[i]

    return inv_count

  def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
      mid = (left + right) // 2

      inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
      inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
      inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

  n = len(values)
  temp_arr = [0] * n
  return merge_sort_and_count(values, temp_arr, 0, n - 1)

def alt_count_inversions(arr):
  if len(arr) <= 1:
    return arr, 0
  else:
    middle = int(len(arr) / 2)
    left, a = alt_count_inversions(arr[:middle])
    right, b = alt_count_inversions(arr[middle:])
    result, c = merge_count_inversions(left, right)
    return result, a + b + c

def merge_count_inversions(x, y):
  count = 0
  i, j = 0, 0
  merged = []
  while i < len(x) and j < len(y):
    if x[i] <= y[j]:
      merged.append(x[i])
      i += 1
    else:
      merged.append(y[j])
      j += 1
      # Here, we update the number of inversions
      # Every element from x[i:] and y[j] forms an inversion
      # because they are greater than y[j]
      count += len(x) - i
  merged += x[i:]
  merged += y[j:]
  return merged, count 

# Problem 3: Sort a list of strings by their lengths.
def sort_strings_by_length(strings):
  return sorted(strings, key=len)