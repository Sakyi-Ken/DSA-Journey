# Problem 1: Majority Vote Problem with Dictionaries
def solution(listA):
  count_dict = {}
  for element in listA:
    count_dict[element] = count_dict.get(element, 0) + 1
    if count_dict[element] > len(listA) // 2:
      return element
  return -1

# Alternative solution for majority count
def alt_solution(listB):
  from collections import defaultdict
  count_dict = defaultdict(int)
  for element in listB:
    count_dict[element] += 1
    if count_dict[element] > len(listB) // 2:
      return element
  return -1

# Problem 2: Implement a Keyword Index for search feature
def keyword_index(docs):
  index = {}
  for doc_index, doc in enumerate(docs):
    for word in doc.split():
      if word in index:
        index[word].append(doc_index)
      else:
        index[word] = [doc_index]
  return index

# Example usage 
if __name__ == "__main__":
  docs = ["the quick brown fox", "jumps over the lazy dog", "the quick blue hare"]
  print(keyword_index(docs))  # Output: {'the': [0, 1, 2], 'quick': [0, 2], 'brown': [0], 'fox': [0], 'jumps': [1], 'over': [1], 'lazy': [1], 'dog': [1], 'blue': [2], 'hare': [2]}

# Alternative solution for keyword index using defaultdict
from collections import defaultdict
def alt_keyword_index(docs):
  index = defaultdict(list)
  for doc_index, doc in enumerate(docs):
    for word in doc.split():
      index[word].append(doc_index)
  return dict(index)

def keyword_index(docs):
  index = {}
  for doc_id, doc in enumerate(docs):
    for word in doc.split():
      if word not in index:
        index[word] = {}
      if doc_id not in index[word]:
        index[word][doc_id] = 0
      index[word][doc_id] += 1
  return index

def alt_keyword_index_with_counts(docs):
  index = defaultdict(lambda: defaultdict(int))
  for doc_id, doc in enumerate(docs):
    for word in doc.split():
      index[word][doc_id] += 1
  return {word: dict(doc_counts) for word, doc_counts in index.items()}

docs = ["Hello world", "world of python", "python is a name of a snake but not a snake"]
print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}
print(alt_keyword_index_with_counts(docs))

def alt_keyword_index_counts(docs):
  index = {}
  for doc_index, doc in enumerate(docs):
    words = doc.split()
    for word in words:
      if word in index:
        if doc_index in index[word]:
          index[word][doc_index] += 1
        else:
          index[word][doc_index] = 1
      else:
        index[word] = {doc_index: 1}
  return index
docs = ["Hello world", "world of python", "python is a name of a snake but not a snake"]
print(alt_keyword_index_counts(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 2, 3: 1}}
