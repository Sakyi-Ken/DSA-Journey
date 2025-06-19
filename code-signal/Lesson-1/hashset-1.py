# Problem1: Array Intersection
def arrangement(list1, list2):
  set1 = set(list1)
  set2 = set(list2)
  intersection = set1 & set2
  return sorted(list(intersection))

# Problem2: Not Repeating Elements
def non_repeating_elements(nums):
  seen, repeated = set(), set()
  for num in nums:
    if num in seen:
      repeated.add(num)
    else:
      seen.add(num)
  return list(seen - repeated)

# Problem3: Find the Missing Number
def find_missing_number(nums):
  n = len(nums)
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return expected_sum - actual_sum

# Problem4: Unique Elements
def unique_elements(list1, list2):
  set1 = set(list1)
  set2 = set(list2)
  unique1 = sorted(list(set1 - set2))
  unique2 = sorted(list(set2 - set1))
  return (unique1, unique2)

# Problem5: Repeating Elements
def repeating_elements(nums):
  seen, repeated = set(), set()
  for num in nums:
    if num in seen:
      repeated.add(num)
    else:
      seen.add(num)
  return sorted(list(repeated))

# Problem6: Uniqueness in strings
def exclusive_products(inventory1, inventory2):
  # implement this
  list1 = []
  list2 = []
  
  unique1 = set()
  unique2 = set()
  
  for char1 in inventory1:
    cap_char = char1.upper()
    list1.append(cap_char)
  for char2 in inventory2:
    upper_char = char2.upper()
    list2.append(upper_char)
  
  set1 = set(list1)
  set2 = set(list2)
  
  for char1 in set1:
    if char1 not in set2:
      unique1.add(char1)
  for char2 in set2:
    if char2 not in set1:
      unique2.add(char2)
  return (list(unique1), list(unique2))

inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])