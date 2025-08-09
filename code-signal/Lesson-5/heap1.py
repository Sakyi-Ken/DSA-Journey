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

  def findMedian(self):
    small, large = self.heaps
    if len(large) > len(small):
      return float(large[0])
    return float((large[0] - small[0]) / 2.0)