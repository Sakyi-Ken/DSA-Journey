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