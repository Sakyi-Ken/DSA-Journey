def quick_sort(arr):
  # import random 
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  # pivot = random.choice(arr)  # Uncomment to use a random pivot
  # pivot = arr[random.randint(0, len(arr) - 1)] # Another way to choose a random pivot
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if  x > pivot]
  return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]))

def quick_sort_in_place(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quick_sort_in_place(arr, low, pi - 1)
    quick_sort_in_place(arr, pi + 1, high)
# This function sorts the array in place using the Quick Sort algorithm
# It uses the partition function to find the pivot and recursively sorts the sub-arrays
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def quick_sort_wrapper(arr):
  quick_sort_in_place(arr, 0, len(arr) - 1)
  return arr

print(quick_sort_wrapper([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]))

def quick_sort_iterative(arr):
  stack = []
  stack.append((0, len(arr) - 1))
  
  while stack:
    low, high = stack.pop()
    if low < high:
      pi = partition(arr, low, high)
      stack.append((low, pi - 1))
      stack.append((pi + 1, high))
  
  return arr

import random 

def partition(arr, low, high):
  pivot = arr[low]
  i = low + 1
  j = high
  done = False
  while not done:
    # Descending order partitioning
    #while i <= j and arr[i] >= pivot:
    #  i += 1
    #while arr[j] <= pivot and j >= i:
      # Ascending order partitioning
    while i <= j and arr[i] <= pivot:
      i += 1
    while arr[j] >= pivot and j >= i:
      j -= 1
    if j < i:
      done = True
    else:
      arr[i], arr[j] = arr[j], arr[i]
  arr[low], arr[j] = arr[j], arr[low]
  return j

def quick_sort(arr, low, high):
  if low < high:
    split_point = partition(arr, low, high)
    quick_sort(arr, low, split_point - 1)
    quick_sort(arr, split_point + 1, high)

# Generate a list of random numbers between 10 and 50
random_list = [random.randint(10, 50) for i in range(15)]

print("Original List:", random_list)

quick_sort(random_list, 0, len(random_list) - 1)
print("List After Quick Sort:", random_list)