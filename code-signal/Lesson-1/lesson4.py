# Problem1 - First Unique String
def find_unique_string(words):
  ''' list -> (str)
  This function finds the first unique string in a list of words.
  '''
  seen = set()
  duplicates = set()

  for word in words:
    if word in seen:
      duplicates.add(word)
    seen.add(word)

  for word in words:
    if word not in duplicates:
      return word
    
  return None

# Problem2 - Anagram Pairs in Two Lists
def find_anagram_pairs(list_1, list_2):
  '''' list, list -> (list of tuples)
  This function finds all pairs of anagrams from list1 and list2 to return them as a list of tuples.
  '''
  sorted_tuples_1 = set(tuple(sorted(word)) for word in list_1)
  sorted_tuples_2 = set(tuple(sorted(word)) for word in list_2)

  common_tuples = sorted_tuples_1 & sorted_tuples_2

  list_1_output = [word for word in list_1 if tuple(sorted(word)) in common_tuples] # contains anagrams from list_1
  list_2_output = [word for word in list_2 if tuple(sorted(word)) in common_tuples] # contains anagrams from list_2

  output = []
  for word1 in list_1_output:
    for word2 in list_2_output:
      # traversing every pair of words in filtered lists
      if tuple(sorted(word1)) == tuple(sorted(word2)):
        # if words in the pair are anagrams, add them to the output list
        output.append((word1, word2))
  return output

print(find_anagram_pairs(['listen', 'silent', 'enlist'], ['inlets', 'google', 'gooogle']))
# Output: [('listen', 'inlets'), ('silent', 'inlets'), ('enlist', 'inlets')]
print(find_anagram_pairs(['abc', 'def'], ['fed', 'cba']))
# Output: [('abc', 'cba'), ('def', 'fed')]

# Problem3: Last unique string in a list
def last_unique_character(words):
  ''' list -> (str)
  This function finds the last unique string in a list of words and returns it.
  '''
  seen = set()
  duplicates = set()
  for word in words:
    if word in seen:
      duplicates.add(word)
    seen.add(word)

  for word in reversed(words):
    if word not in duplicates:
      return word
  
  return ''

# Example usage
print(last_unique_character(['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi']))
# Output: 'kiwi'

# Alternative implementation for the last unique string
def find_unique_string(words):
  # implement this
  seen = set()
  repeated = set()
  unique = []
  
  for word in words:
    if word in seen:
      repeated.add(word)
    seen.add(word)
  
  for word in words:
    if word not in repeated:
      unique.append(word)
          
  for i in range(len(unique)):
    return unique[len(unique) - 1]
  
  return ''

print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
print(find_unique_string([]))  # It should print: ''


def find_anagram_words(list_1, list_2):
  # implement this
  sorted_tuples_1 = set(tuple(sorted(word)) for word in list_1)
  sorted_tuples_2 = set(tuple(sorted(word)) for word in list_2)
  
  common_tuples = sorted_tuples_1 & sorted_tuples_2 
  
  list_1_output = [word for word in list_1 if tuple(sorted(word)) in common_tuples]
  list_2_output = [word for word in list_2 if tuple(sorted(word)) in common_tuples]
  
  output = []
  
  for word_1 in list_1_output:
    for word_2 in list_2_output:
      if tuple(sorted(word_1)) == tuple(sorted(word_2)):
        output.append(word_1)
        output.append(word_1)

  return list(set(output))

print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []