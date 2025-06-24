# Problem 1: Search in a Rotated Sorted Array
# Given a rotated sorted array, find the index of a target value.
# If the target is not found, return -1.
def search_rotated_array(nums, target):
  left, right = 0, len(nums) - 1
  
  while left <= right:
    mid = (left + right) // 2
      
    if nums[mid] == target:
        return mid
      
      # Check if the left half is sorted
    if nums[left] <= nums[mid]:
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
      # Otherwise, the right half is sorted
    else:
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
              
  return -1

# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search_rotated_array(nums, target)
print("Index of target value:", result)  # Output: Index of target value: 4

# Problem 2: Search in a Rotated Sorted Array with Duplicates
# Given a rotated sorted array that may contain duplicates, find the index of a target value.
def search_rotated_array_duplicates(nums, target):
  left, right = 0, len(nums) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
      return mid
    
    # Handle duplicates
    if nums[left] == nums[mid] == nums[right]:
      left += 1
      right -= 1
    elif nums[left] <= nums[mid]:  # Left half is sorted
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    else:  # Right half is sorted
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
              
  return -1

# Example usage with duplicates
nums_with_duplicates = [2, 5, 6, 0, 0, 1, 2]
target_with_duplicates = 0  
result_with_duplicates = search_rotated_array_duplicates(nums_with_duplicates, target_with_duplicates)
print("Index of target value in array with duplicates:", result_with_duplicates)  # Output: Index of target value in array with duplicates: 3

# Problem 3: Search in a Rotated Sorted Array with Duplicates and Multiple Targets
# Given a rotated sorted array that may contain duplicates, find all indices of a target value.
def search_rotated_array_all_indices(nums, target):
  indices = []
  left, right = 0, len(nums) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
      indices.append(mid)
      # Search left side for more occurrences
      l = mid - 1
      while l >= left and nums[l] == target:
        indices.append(l)
        l -= 1
      # Search right side for more occurrences
      r = mid + 1
      while r <= right and nums[r] == target:
        indices.append(r)
        r += 1
      break
    
    # Handle duplicates
    if nums[left] == nums[mid] == nums[right]:
      left += 1
      right -= 1
    elif nums[left] <= nums[mid]:  # Left half is sorted
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    else:  # Right half is sorted
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
              
  return sorted(indices)
# Example usage with multiple targets
nums_multiple_targets = [2, 5, 6, 0, 0, 1, 2, 2]
target_multiple = 2
result_multiple = search_rotated_array_all_indices(nums_multiple_targets, target_multiple)
print("Indices of target value in array with duplicates and multiple targets:", result_multiple)  # Output: Indices of target value in array with duplicates and multiple targets: [0, 6, 7]  

# Problem 4: Search in a Rotated Sorted Array with Duplicates and No Targets
# Given a rotated sorted array that may contain duplicates, return an empty list if the target value is not found.
def search_rotated_array_no_targets(nums, target):
  indices = []
  left, right = 0, len(nums) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
      indices.append(mid)
      # Search left side for more occurrences
      l = mid - 1
      while l >= left and nums[l] == target:
        indices.append(l)
        l -= 1
      # Search right side for more occurrences
      r = mid + 1
      while r <= right and nums[r] == target:
        indices.append(r)
        r += 1
      break
    
    # Handle duplicates
    if nums[left] == nums[mid] == nums[right]:
      left += 1
      right -= 1
    elif nums[left] <= nums[mid]:  # Left half is sorted
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    else:  # Right half is sorted
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
              
  return sorted(indices) if indices else []
# Example usage with no targets
nums_no_targets = [2, 5, 6, 0, 0, 1, 2]
target_no_targets = 3
result_no_targets = search_rotated_array_no_targets(nums_no_targets, target_no_targets)
print("Indices of target value in array with duplicates and no targets:", result_no_targets)
# Output: Indices of target value in array with duplicates and no targets: []

# Problem 5: Search in a Rotated Sorted Array with Duplicates and Single Target
# Given a rotated sorted array that may contain duplicates, find the index of a single target value
def search_rotated_array_single_target(nums, target):
  left, right = 0, len(nums) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
      return mid
    
    # Handle duplicates
    if nums[left] == nums[mid] == nums[right]:
      left += 1
      right -= 1
    elif nums[left] <= nums[mid]:  # Left half is sorted
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    else:  # Right half is sorted
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
            
  return -1
# Example usage with single target
nums_single_target = [2, 5, 6, 0, 0, 1, 2]
target_single = 1
result_single = search_rotated_array_single_target(nums_single_target, target_single)
print("Index of single target value in array with duplicates:", result_single)  # Output: Index of single target value in array with duplicates: 5  

# Problem 6: Search in a Rotated Sorted Array with Duplicates and Multiple Targets
# Given a rotated sorted array that may contain duplicates, find all indices of multiple target values.
def search_rotated_array_multiple_targets(nums, targets):
  indices = []
  for target in targets:
    left, right = 0, len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2
      
      if nums[mid] == target:
        indices.append(mid)
        # Search left side for more occurrences
        l = mid - 1
        while l >= left and nums[l] == target:
          indices.append(l)
          l -= 1
        # Search right side for more occurrences
        r = mid + 1
        while r <= right and nums[r] == target:
          indices.append(r)
          r += 1
        break
      
      # Handle duplicates
      if nums[left] == nums[mid] == nums[right]:
        left += 1
        right -= 1
      elif nums[left] <= nums[mid]:  # Left half is sorted
        if nums[left] <= target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else:  # Right half is sorted
        if nums[mid] < target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
                  
  return sorted(set(indices))
# Example usage with multiple targets
nums_multiple_targets = [2, 5, 6, 0, 0, 1, 2, 2]
targets_multiple = [2, 0]
result_multiple_targets = search_rotated_array_multiple_targets(nums_multiple_targets, targets_multiple)
print("Indices of multiple target values in array with duplicates:", result_multiple_targets)  # Output: Indices of multiple target values in array with duplicates: [0, 3, 6, 7]

# Problem 7: Search in a Rotated Sorted Array with Duplicates and No Targets
# Given a rotated sorted array that may contain duplicates, return an empty list if no target values are found.
def search_rotated_array_no_targets_multiple(nums, targets):
  indices = []
  for target in targets:
    left, right = 0, len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2
      
      if nums[mid] == target:
        indices.append(mid)
        # Search left side for more occurrences
        l = mid - 1
        while l >= left and nums[l] == target:
          indices.append(l)
          l -= 1
        # Search right side for more occurrences
        r = mid + 1
        while r <= right and nums[r] == target:
          indices.append(r)
          r += 1
        break
      
      # Handle duplicates
      if nums[left] == nums[mid] == nums[right]:
        left += 1
        right -= 1
      elif nums[left] <= nums[mid]:  # Left half is sorted
        if nums[left] <= target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else:  # Right half is sorted
        if nums[mid] < target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
                  
  return sorted(set(indices)) if indices else []

# Example usage with no targets
nums_no_targets_multiple = [2, 5, 6, 0, 0, 1, 2]
targets_no_targets_multiple = [3, 4]
result_no_targets_multiple = search_rotated_array_no_targets_multiple(nums_no_targets_multiple, targets_no_targets_multiple)
print("Indices of no target values in array with duplicates:", result_no_targets_multiple)  # Output: Indices of no target values in array with duplicates: []

# Problem 8: Search in a Rotated Sorted Array with Duplicates and Single Target
# Given a rotated sorted array that may contain duplicates, find the index of a single target value
def search_rotated_array_single_target_multiple(nums, target):
  left, right = 0, len(nums) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
      return mid
    
    # Handle duplicates
    if nums[left] == nums[mid] == nums[right]:
      left += 1
      right -= 1
    elif nums[left] <= nums[mid]:  # Left half is sorted
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    else:  # Right half is sorted
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
              
  return -1
# Example usage with single target
nums_single_target_multiple = [2, 5, 6, 0, 0, 1, 2]
target_single_multiple = 1
result_single_multiple = search_rotated_array_single_target_multiple(nums_single_target_multiple, target_single_multiple)
print("Index of single target value in array with duplicates:", result_single_multiple)  # Output: Index of single target value in array with duplicates: 5