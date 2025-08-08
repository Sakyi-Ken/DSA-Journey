# Notes on Trees

**A tree** in computer science is a non-linear data structure representing a hierarchical and connected
arrangement of entities known as nodes.
**A binary tree** is a specific type of tree data structure where each node has at most two children: one left node and one right node.
**A non-binary tree**, also known as a multi-way tree, can have more than two children per node.

## Terminology:

- **Root**: The topmost node in a tree.
- **Edge**: The connection between one node to another.
- **Leaf**: A node that doesn't have any children.
- **Depth of a Node**: The number of edges from the node to the tree's root node.
- **Height of a Tree**: The maximal depth of the tree nodes.
- **Subtree**: Any node and its descendants form a subtree of the original tree.

## Tree properties:

- **Path**: A sequence of nodes and edges connecting a node with a descendant.
- **Acyclic**: Trees cannot have cycles, which are paths where the start and end points are the same.
- **Connected**: All nodes in a tree are connected by paths.
- **E=V−1**: For any tree, the number of edges (E) is always one less than the number of vertices (V), illustrating the tree's connectivity without cycles.

## Binary Tree Traversal

**Traversal** of the binary tree is a process of visiting all nodes of a tree and possibly printing their values.

- **In Order**: In this method the left subtree is visited first, then the root, and the right subtree.
- **Pre Order**: In this method, the root node is visited first, then the left subtree and the right subtree.
- **Post Order**: In this method, the root node is visited last, the left subtree first and the right subtree follows.

## Complexity Analysis: Binary and Non-Binary Trees

**For binary trees**, the worst-case time complexity for searching, insertion, or deletion is O(n), where n is the number of nodes.
This complexity arises because, in the worst case, you might have to traverse all nodes. However,
in ideal circumstances (where the tree is perfectly balanced), operations on binary trees run in O(logn) time.

**Comparatively**, for non-binary trees, searching for or deleting a node can still be O(n), but insertion may be more efficient —
O(1) — if we keep track of where the next insertion should happen; if we don't, the complexity is the same as in binary tree.

## DFS Algorithm

_Explore the depth before the breadth_

- The DFS algorithm starts at the root node, marking it as visited.
- For every child node of the starter node:
- If the child hasn't been visited, the algorithm recursively executes from the child node.
- If the child has already been visited, the algorithm skips this node and proceeds to the next child.
- The algorithm automatically finishes when all achievable nodes have been visited.

## DFS Time and Space Complexity

For DFS, the time complexity is O(V+E), where V represents the number of vertices (or nodes), and E represents the number of edges.
DFS needs to visit every edge and vertex at least once, which dictates its time complexity.
For trees specifically, as E=V−1, the dfs time complexity is O(V).

The space complexity of DFS is O(V).

## BFS Algorithm

The potent search algorithm explores nodes level-by-level, examining all siblings before moving on to the children.
In this algorithm, we aim to visit nodes closest to the root node first before moving deeper into the tree.
**BFS** compared to **DFS** is like exploring your neighbourhood before moving to the next town, while **DFS** would be like
driving straight across the country, visiting towns and routes, before coming back to your neighbourhood town.

- Start with the root node.
- Visit the root node and add all the its direct children to the queue.
- Visit each node in the queue, adding all its unvisited children to the queue. Repeat this exercise until the queue is empty

## BFS Time and Space Complexity

Performing BFS requires inspecting all vertices and edges, resulting in a `time complexity` of O(V+E) As for trees E=V−1, the time complexity is O(V).
The `space complexity` is O(V).

## HEAP

A **heap** is a complete binary tree that satisfies a special property known as the heap property.
Essentially, the heap property stipulates that if _`P`_ is a parent node of _`C`_, the value of node _`P`_ is either greater than or equal
to (in the case of a Max Heap) or lesser than or equal to (in a Min Heap) the value of node _`C`_.
In simpler terms, in a `Max Heap`, each parent node is greater than or equal to its child node(s), and in a `Min Heap`, each parent node is less than or equal to its child node(s).

## Heap Operations

_Heaps support numerous operations, such as:_

1. **Insert**: Inserting a new node in a heap may disrupt the heap property. To maintain the heap property after each insertion, the node is swapped with the parent node if the heap property is violated. This process continues until the heap property is retained for all nodes.

2. **Delete**: The deletion of a node also disrupts the heap property. After deleting a node, the heap property is restored either by swapping the node with its parent, similar to the Insert operation or by swapping it with one of its children. The swapping process continues until the heap property is retained for all nodes.

3. **Extract**: Extracting the maximum (for Max Heap) or minimum (for Min Heap) is a constant-time operation, as the maximum or the minimum element is always at the root of the heap.

The `"Heapify"` method is an intriguing function used to rearrange elements in heap data structures. It assists in preserving the heap property within the heap. In Python, this operation can be executed using the heapify() function

## Heap Sort

- Build a MinHeap out of the array
- Repeatedly remove the minimum element from the heap and insert it into the sorted array while ensuring the heap retains the MinHeap property.
- Heap sort is a comparison-based sorting algorithm and is particularly efficient when dealing with large datasets due to its O(nlogn) time complexity.
  The algorithm removes the minimal element in O(logn) time and repeats this operation n times.
