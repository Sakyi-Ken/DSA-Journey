# What you will learn

- Hash Functions: Discover how hash functions create unique data mappings, enabling quick lookups.
- Dictionaries: Learn to store and retrieve data with key-value pairs for optimal performance.
- Sets: Understand how sets manage unique elements efficiently for fast operations.
- Collision Handling: Explore techniques to manage hash collisions for reliable data storage.
- Complexity Analysis: Analyze the efficiency of operations to write optimized code.

# Hashing

## Definitions

- **Hash function** is a specific function that take an input (also known as a message) and return a fixed-size string of bytes.
- **Hash set** uses hash functions to point directly to the location of the interaction, making operations efficient and timely,
  thus making it preferable when you want to prevent duplicates.

### Characteristics

- `Uniqueness of elements`
- `Inherent unordered property`

### Hash Maps / Hash Tables

- **Hash maps** (also known as dictionaries in Python) are data structures that store key-value pairs.
- They use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
- Hash maps provide average-case constant time complexity, O(1), for insertion, deletion, and lookup operations.
- Keys must be hashable (immutable types like strings, numbers, or tuples).
- Hash maps handle collisions using techniques like chaining or open addressing.
- They are widely used for fast data retrieval and efficient storage of associative data.

`Hash function` plays a crucial role - it takes the keys as input and generates an index, mapping keys to different slots or indices in the table.

Each index of the array holds a bucket that ultimately contains the key-value pair. The pairing of keys with values enhances the data retrieval process. The efficiency of retrieving values depends on the hash function's ability to distribute data across the array uniformly.

**Collision Handling in Hash Tables**

There are instances when two different keys produce the same index after being processed through the hash function. This situation is known as a collision. When a collision occurs, we are faced with a dilemma - where do we store the new key-value pair since that index is already occupied?

`Chaining`: In this method, each index (or bucket) in the array hosts a linked list of all key-value pairs that hash to the same index. When a collision occurs, we simply go to the collided index and append the new key-value pair to the existing linked list.

`Open Addressing`: Upon encountering a collision, the hash table searches for another free slot or index in the table (possibly the next available empty slot) and assigns that location to the new key-value pair. This approach requires a suitable probing strategy to ensure efficient use of table space.

_Python provides a built-in implementation of hash tables, known as dictionaries. Dictionaries in Python work similarly to hash tables. They allow the use of arbitrary keys to access values and handle collisions seamlessly behind the scenes, ensuring consistent and quick access to stored data._

- `Counter` is a subclass of dict designed to count hashable items.
- If words is an iterable (like a list of words or a string), _Counter(words)_ creates a dictionary where each unique item is a key, and its value is the count of how many times it appears.

- In Python, a hashable item is an object that can be used as a key in a dictionary or as an element in a set. Hashable objects have a hash value that does not change during their lifetime (they are immutable), such as strings, numbers, and tuples. Lists and dictionaries are not hashable because they can be changed after creation.
