# Time and Space Complexity of Stack Operations.

- Let's unravel the complexities (pun intended!) behind these Stack operations.
- All three of our basic operations — push, pop, and peek — have a time complexity of O(1),
- meaning they take constant time to complete, regardless of the size of the Stack.

Contrarily, the space complexity is O(n), where n is the number of elements in the Stack.
This is considering an average scenario where elements are continually added and then removed from the Stack.

# Time and Space Complexity of Queue Operations.

- Python lists, however, have a significant drawback: the pop(0) method has O(n) time complexity, while we would like it to be O(1).
- There is another Python module named collections that offers deque, a flexible container that serves both as queue and stack implementations.

_Queues can be more versatile than they might seem at first glance._

- For instance, in Graph theory, the Breadth-First Search (BFS) algorithm makes extensive use of Queues
- to check nodes across levels in the correct order in a graph traversal problem.

# Understanding LinkedLists
- A linked list is a collection of nodes, each acting as a container for its data and a pointer (link) to the next node in the list. 
- This link greatly facilitates sequential traversal through the list.
- A node consists of two parts: Data, which contains the stored value (that could be any type such as number, string, etc.), 
- and Pointer to Next Node, which holds the link to the next node in the sequence. 
- When a node is initially created, next is set to None because there is no subsequent node to point to.

# Linked Lists vrs Arrays
- Memory Usage: Arrays allocate memory in a continuous block during their initialization. 
  Advanced allocation may lead to unused memory if not all spaces are filled. On the other hand, 
  linked lists allocate memory only when required, making efficient use of memory.

- Insertion and Deletion: Inserting or deleting elements in an array is an expensive operation as it generally involves shifting elements to maintain element continuity. 
  With linked lists, these operations are more efficient and take a constant time of O(1).

- Access Time: Arrays provide constant time access to any element. Contrarily, linked lists require iteratively O(n) time for accessing an element. 
  With arrays, you can directly jump to any index, while linked lists necessitate traversal from the start to the desired node

# Complexity Analysis
- Irrespective of the size of the list, insertion or deletion at any place takes constant time, i.e., O(1).
- However, searching for a node in a linked list requires iterative traversal, and this can lead to the worst-case time complexity of O(n).

**Insertion:** When we talk about insertion, we are referring to the process of adding a new node to the existing list.

**Deletion:** Contrarily, deletion describes the action of removing a specific node from the list.

**Traversal:** This operation is involved with accessing and scanning through the elements in the list, one by one.