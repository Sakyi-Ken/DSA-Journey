# Problem 1: Search in a rotated sorted array
def search_rotated(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    if nums[left] <= nums[mid] and nums[left] <= target < nums[mid]:
      right = mid - 1
    elif nums[mid] <= nums[right] and nums[mid] < target <= nums[right]:
      left = mid + 1
    elif nums[mid] > nums[right]: # and (target < nums[mid] or target >= nums[left])
      left = mid + 1
    else: 
      right = mid - 1
  return -1
# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search_rotated(nums, target)
print("Index of target in rotated sorted array:", result)

# Problem 2: Locate the First and Last Position of an Element in a Sorted Array
def get_first_last_pos(nums, target):
  def binary_search(left, right, find_first):
    if left <= right:
      mid = (left + right) // 2
      if nums[mid] > target or (find_first and target == nums[mid]):
        return binary_search(left, mid - 1, find_first)
      else:
        return binary_search(mid + 1, right, find_first)
    return left 
  
  first = binary_search(0, len(nums) - 1, True)
  last = binary_search(0, len(nums) -1, False) - 1

  if first <= last:
    return [first, last]
  else:
    return [-1, -1]

def search_range(nums, target):
  def find_left(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return left

  def find_right(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] <= target:
        left = mid + 1
      else:
        right = mid - 1
    return right

  left_index = find_left(nums, target)
  right_index = find_right(nums, target)

  if left_index <= right_index:
    return [left_index, right_index]
  else:
    return [-1, -1]
# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = search_range(nums, target)
print("First and last position of target in sorted array:", result)

def alt_search_range(nums, target):
  def find_last_less(nums, target):
    left, right = -1, len(nums) - 1
    while left < right:
      mid = (left + right + 1) // 2
      if nums[mid] < target:
        left = mid
      else: 
        right = mid - 1
    return left
  
  def find_last_less_equal(nums, target):
    left, right = -1, len(nums) - 1
    while left < right:
      mid = (left + right + 1) // 2
      if nums[mid] <= target:
        left = mid
      else:
        right = mid - 1
    return left
  
  left = find_last_less(nums, target)
  right = find_last_less_equal(nums, target)
  if left + 1 <= right: #< len(nums) and nums[left + 1] == target
    return [left + 1, right]
  else:
    return [-1, -1]
# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = alt_search_range(nums, target)
print("Alternative first and last position of target in sorted array:", result)

# Problem 3: Search in a 2D Matrix
def search_matrix(matrix, target):
  if not matrix or not matrix[0]:
    return False

  rows, cols = len(matrix), len(matrix[0])
  left, right = 0, rows * cols - 1

  while left <= right:
    mid = (left + right) // 2
    mid_value = matrix[mid // cols][mid % cols]

    if mid_value == target:
      return True
    elif mid_value < target:
      left = mid + 1
    else:
      right = mid - 1

  return False
# Example usage
matrix = [  
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60],
  [60, 61, 62, 63]
]
target = 3
result = search_matrix(matrix, target)
print("Target found in 2D matrix:", result)

# Problem 4: Find or Define Insert Position in a Sorted List
def search_insert(nums, target):
  nums.append(float('inf'))  # Append infinity to handle edge cases
  left, right = 0, len(nums)
  while right - left > 1:
    mid = (left + right) // 2
    if nums[mid] < target:
      left = mid
    else:
      right = mid
  return left 

def test_search_rotated(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    
    # Check if the current segment is ascending or descending
    if nums[left] < nums[right]: # Ascending
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    elif nums[left] > nums[right]: # Descending
      if nums[mid] > target:
        left = mid + 1
      else:
        right = mid - 1
    else:
      # Handles duplicates or single element
      if nums[left] == target:
        return left
      left += 1
  return -1

def alt_search_rotated(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid

    if nums[left] >= nums[mid]:
      if nums[left] >= target > nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    else:  # Right half is sorted (decreasing)
      if nums[mid] > target >= nums[right]:
        left = mid + 1
      else:
        right = mid - 1

# Example usage
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
target = 6
result = test_search_rotated(nums, target)
print("Index of target in (possibly rotated) sorted array:", result)

result = alt_search_rotated(nums, target)
print("Index of target in (possibly rotated) sorted array:", result)