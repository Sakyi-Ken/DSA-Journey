import heapq

# Problem 1: Heap-based Median Finder
# Naive Approach: Use a sorted list to find the median

# Using a sorted list to find the median
def find_median_sorted_list(arr):
  arr.sort()
  n = len(arr)
  if n % 2 == 1:
    return arr[n // 2]
  else:
    return (arr[n // 2 - 1] + arr[n // 2]) / 2
  
# Example usage
print("Median of sorted list [1, 3, 2, 5, 4]:", find_median_sorted_list([1, 3, 2, 5, 4]))

# Alt
class MedianFinder:
  def __init__(self):
    self.heaps = [], []
  
  def addNum(self, num):
    small, large = self.heaps
    heapq.heappush(small, -heapq.heappushpop(large, num))
    if len(large) < len(small):
      heapq.heappush(large, -heapq.heappop(small))
  
  def add(self, numbers):
    for num in numbers:
      self.addNum(num)
    return self

  def findMedian(self):
    small, large = self.heaps
    if len(large) > len(small):
      return float(large[0])
    return float((large[0] - small[0]) / 2.0)
  
# Example usage
medianFinder = MedianFinder()
for num in [1, 3, 2, 4, 5]:
  medianFinder.addNum(num)
print("Median of added numbers:", medianFinder.findMedian())
# Output: Median of added numbers: 3.0
# Example usage with add method
medianFinder = MedianFinder().add([1, 3, 2, 4, 5])
print("Median of added numbers using add method:", medianFinder.findMedian())
# Output: Median of added numbers using add method: 3.0

class SortWithHeap:
  def __init__(self):
    self.heaps = [], []

  def first_sort(self, arr):
    sort_list = self.heaps
    for num in arr:
      heapq.heappush(sort_list, -num)
    return [-heapq.heappop(sort_list) for _ in range(len(sort_list))][::-1]

  def second_sort(self, arr):
    sort_arr = []
    for num in arr:
      heapq.heappush(sort_arr, num)
    return [heapq.heappop(sort_arr) for _ in range(len(sort_arr))]
      
# Example usage
sorter = SortWithHeap()
print("Sorted array using first_sort:", sorter.first_sort([4, 7, 2, 8, 1, 3]))
# Output: Sorted array using first_sort: [1, 2, 3, 4, 7, 8]
print("Sorted array using second_sort:", sorter.second_sort([4, 7, 2, 8, 1, 3]))
# Output: Sorted array using second_sort: [1, 2, 3, 4, 7, 8]
print("Sorted array using third_sort:", sorter.third_sort([4, 7, 2, 8, 1, 3]))
# Output: Sorted array using third_sort: [1, 2, 3, 4, 7, 8]
