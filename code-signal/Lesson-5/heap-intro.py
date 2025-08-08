import heapq

minHeap = [4, 7, 2, 8, 1, 3]
heapq.heapify(minHeap)  # Transform list into a heap in-place

# Display the heap
print("Heapify Method:", minHeap)
# Output: Heapify Method: [1, 4, 2, 8, 7, 3]

heap = []

# Insert in heap
heapq.heappush(heap, 4)
heapq.heappush(heap, 9)
heapq.heappush(heap, 6)

print("Heap after insertions:", heap)
# Output: Heap after insertions: [4, 9, 6]

# Delete the minimum element
min_element = heapq.heappop(heap)
print("Deleted minimum element:", min_element)
# Output: Deleted minimum element: 4

print("Heap after deletion:", heap)
# Output: Heap after deletion: [6, 9]

# Extract the minimum element without deleting it
min_element_peek = heap[0]
print("Minimum element (peek):", min_element_peek)
# Output: Minimum element (peek): 6

smallest = heapq.nsmallest(1, heap)[0]
print("Smallest element in heap:", smallest)
# Output: Smallest element in heap: 6

maxHeap = [-x for x in minHeap]  # Convert to max-heap by negating values
heapq.heapify(maxHeap)
print("Max Heap:", [-x for x in maxHeap])
# Output: Max Heap: [8, 7, 3, 4, 1, 2]

def heap_sort(arr):
  import heapq
  heapq.heapify(arr)
  return [heapq.heappop(arr) for _ in range(len(arr))]
  # heapq.heapify(arr)  # Transform list into a heap in-place
  # sorted_arr = []
  # while arr:
  #   sorted_arr.append(heapq.heappop(arr))  # Pop elements from the heap
  # return sorted_arr

print("Sorted array using heap sort:", heap_sort([4, 7, 2, 8, 1, 3]))
# Output: Sorted array using heap sort: [1, 2, 3, 4, 7, 8]

# Import necessary libraries
import heapq

# Create an empty MinHeap
minHeap = []

# Function to insert nodes maintaining the heap property
def insertNode(node_list):
  for node in node_list:
    heapq.heappush(minHeap, node)

# Function to delete node from heap
def deleteNode():
  try:
    return heapq.heappop(minHeap)
  except:
    return None

# insert nodes into the MinHeap
insertNode([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# print MinHeap after insertions
print("Heap after insertions: ", minHeap)

# Delete a node from MinHeap
deleteNode()

# print MinHeap after deletion
print("Heap after deleting the minimum node: ", minHeap)

maxHeap = []

def insertMaxNode(node_list):
  for node in node_list:
    heapq.heappush(maxHeap, -node)  # Negate the value to simulate max-heap

def deleteMaxNode():
  try:
    return -heapq.heappop(maxHeap)  # Negate again to get the original value
  except:
    return None

# Insert nodes into the MaxHeap
insertMaxNode([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
# Print MaxHeap after insertions
print("Max Heap after insertions: ", [-x for x in maxHeap])
# Delete a node from MaxHeap
deleteMaxNode()
# Print MaxHeap after deletion
print("Max Heap after deleting the maximum node: ", [-x for x in maxHeap])
# Convert back to positive for display
# Output: Max Heap after deleting the maximum node: [6, 5, 5, 4, 1, 2, 3]