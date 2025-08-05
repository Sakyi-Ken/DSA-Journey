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
