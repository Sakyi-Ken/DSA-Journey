# Problem 1: Sorting Values in a List.
def sort_list(values):
  return sorted(values)

# Problem 1.1: Sorting Values in a List in a Reverse Order.
def sort_list(values):
  return sorted(values, reverse=True)

# Problem 2: Sorting Tuples by the Second Element.
def sort_tuples(tuples):
  return sorted(tuples, key=lambda x: x[1])

# Problem 2.1: Sorting Tuples ties
def sort_tuples_ties(tuples):
  return sorted(tuples, key=lambda x: (x[1], x[0]))

# Alt for 2.1
def sort_ties(values):
  return values.sort(key=lambda x: (x[1], x[0]))

# Problem 3: Sorting a Dictionary Based on Values
def sort_dict(dictionary):
  return sorted(dictionary.items(), key=lambda x: x[1])

# Problem 4: Sorting Values in a List with Custom Sort Order.
def sort_list_custom(values, order):
  if order == 'asc':
    return sorted(values)
  elif order == 'desc':
    return sorted(values, reverse=True)
  else:
    raise ValueError("Order must be 'asc' or 'desc'")

# Problem 4.1: Sorting Values in a List with a Custom Key Function.
def sort_list_custom_key(values, key_func):
  return sorted(values, key=key_func)

# Problem 4.2: Sorting Values in a List with a Custom Key Function and Order.
def sort_list_custom_key_order(values, key_func, order):
  if order == 'asc':
    return sorted(values, key=key_func)
  elif order == 'desc':
    return sorted(values, key=key_func, reverse=True)
  else:
    raise ValueError("Order must be 'asc' or 'desc'")