def merge_sort(lst):
  # if it's a single element or an empty list, it's already sorted
  if len(lst) <= 1:
    return lst
  
  # find the middle point
  mid = len(lst) // 2

  # Recursively sort both halves
  left_half = merge_sort(lst[mid:])
  right_half = merge_sort(lst[:mid])

  # Merge the sorted halves
  return merge(left_half, right_half)

def merge(left, right):
  result = []
  i = j = 0

  # Compare the smallest unused elements in both lists and append the smallest to the result
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else: 
      result.append(right[j])
      j += 1
  # Once we've exhausted one list, append all remaining elements from the other list to the result
  # Here, we append both lists, as at least one is an empty list
  result.extend(left[i:])
  result.extend(right[j:])
  return result

import random

# Generate a list of 100 numbers between 1 and 1000
random_numbers = [random.randint(1, 1000) for i in range(100)]
print(f"Original List: {random_numbers}")

sorted_numbers = merge_sort(random_numbers)
print(f"\nSorted List: {sorted_numbers}")

# Example usage
if __name__ == "__main__":
  lst = [38, 27, 43, 3, 9, 82, 10]
  print("Original list:", lst)
  sorted_lst = merge_sort(lst)
  print("Sorted list:", sorted_lst)
  
  # Test with an empty list
  empty_list = []
  print("Sorted empty list:", merge_sort(empty_list))
  
  # Test with a single element
  single_element_list = [42]
  print("Sorted single element list:", merge_sort(single_element_list))
  
  # Test with already sorted list
  already_sorted_list = [1, 2, 3, 4, 5]
  print("Sorted already sorted list:", merge_sort(already_sorted_list))

# Test with a list containing duplicate elements
  duplicate_list = [5, 3, 8, 3, 2, 5, 1]
  print("Sorted list with duplicates:", merge_sort(duplicate_list))
# Test with a list containing negative numbers
  negative_list = [-3, -1, -4, -2, 0, 2, 1]
  print("Sorted list with negative numbers:", merge_sort(negative_list))
# Test with a list containing large numbers
  large_numbers_list = [1000000, 500000, 2000000, 1500000, 3000000]
  print("Sorted list with large numbers:", merge_sort(large_numbers_list))
# Test with a list containing floating-point numbers
  float_list = [3.14, 2.71, 1.41, 1.73, 0.577]
  print("Sorted list with floating-point numbers:", merge_sort(float_list))
# Test with a list containing strings
  string_list = ["banana", "apple", "cherry", "date"]
  print("Sorted list with strings:", merge_sort(string_list))
# Test with a list containing mixed data types (should raise an error)
  mixed_list = [1, "two", 3.0, "four"]
  try:
    print("Sorted mixed list:", merge_sort(mixed_list))
  except TypeError as e:
    print("Error sorting mixed list:", e) 
# Test with a list containing special characters
  special_char_list = ["@", "#", "$", "%", "&"]
  print("Sorted list with special characters:", merge_sort(special_char_list))
# Test with a list containing Unicode characters
  unicode_list = ["éclair", "café", "jalapeño", "résumé"]
  # Note: Sorting Unicode strings may depend on the locale and Python version
  # This example assumes a simple lexicographical sort
  print("Sorted list with Unicode characters:", merge_sort(unicode_list))
# Test with a list containing boolean values
  boolean_list = [True, False, True, False]   
  print("Sorted list with boolean values:", merge_sort(boolean_list))
# Test with a list containing None values
  none_list = [None, 1, None, 2]
  try:
    print("Sorted list with None values:", merge_sort(none_list))
  except TypeError as e:
    print("Error sorting list with None values:", e)
# Test with a list containing a mix of integers and floats
  mixed_numbers_list = [1, 2.5, 3, 4.5, 5]
  print("Sorted list with mixed integers and floats:", merge_sort(mixed_numbers_list))


  # Import necessary modules
import random

def merge_sort(lst):
  # If it's a single element or an empty list, it's already sorted
  if len(lst) <= 1:
    return lst

  # Find the middle point
  mid = len(lst) // 2

  # Recursively sort both halves
  left_half = merge_sort(lst[:mid])
  right_half = merge_sort(lst[mid:])

  # Merge the two sorted halves
  return merge(left_half, right_half)

def merge(left, right):
  result = []
  i = j = 0

  # Compare the smallest unused elements in both lists and append the smallest to the result
  while i < len(left) and j < len(right):
    if left[i:3] < right[j:3]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # Once we've exhausted one list, append all remaining elements from the other list to the result
  result.extend(left[i:])
  result.extend(right[j:])
  
  return result

# Generate a list of 20 random strings of length 5
random_strings = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)) for i in range(20)]

print("\nOriginal List of random strings: \n", random_strings)

# Apply merge sort
sorted_strings = merge_sort(random_strings)

print("\nSorted List of strings: \n", sorted_strings)