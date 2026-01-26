**Theory Note: Trees**
=======================

### Introduction
---------------

A tree is a fundamental data structure consisting of nodes connected by edges, forming a hierarchical structure. It's used for efficient storage and retrieval of data, particularly when the data has a natural hierarchy or ordering.

### Core Concepts
-----------------

#### Definition

A tree is defined as an undirected graph with:

* No cycles (i.e., there are no paths that start and end at the same node).
* A single root node.
* All other nodes have exactly one parent node except for leaves, which have none.

#### Types of Trees

* **Binary Tree**: Each node has at most two children (left child and right child).
* **B-Tree**: A self-balancing search tree with a specific structure to ensure efficient insertion, deletion, and searching operations.
* **Heap**: A specialized tree-based data structure that satisfies the heap property: the parent node is either greater than (max heap) or less than (min heap) its children.

### Key Formulas/Theorems
---------------------------

#### Binary Heap

For a binary min-heap with $n$ elements:

$$\text{Number of internal nodes} = \left \lfloor \frac{n}{2} \right \rfloor$$

$$\text{Number of leaf nodes} = n - 2 \cdot \left \lfloor \frac{n}{2} \right \rfloor$$

### Problem Solving Patterns
---------------------------

#### Analyzing Trees

When analyzing trees, consider the following:

* **Height**: The maximum number of edges on any path from the root to a leaf.
* **Depth**: The length of the longest path from the root to a node.
* **Width**: The number of nodes at a given depth.

### Examples with Solutions
---------------------------

**Example 1: Binary Min-Heap**

Suppose we have a binary min-heap with $105$ elements. Find the number of possible values of $k$, where $k$ is the index (in the underlying array) of the maximum element stored in the heap.

```latex
\begin{align*}
n & = 105 \\
\text{Number of internal nodes} & = \left \lfloor \frac{n}{2} \right \rfloor = \left \lfloor \frac{105}{2} \right \rfloor = 52 \\
\text{Number of leaf nodes} & = n - 2 \cdot \left \lfloor \frac{n}{2} \right \rfloor \\
& = 105 - 2 \cdot 52 \\
& = 1
\end{align*}
```

Hence, there is only $1$ possible value of $k$, which is the index of the maximum element.

### Common Pitfalls
------------------

#### Misunderstanding Tree Properties

Be careful when analyzing tree properties. For example:

* A binary min-heap has a root node with no children.
* A B-tree has a specific structure to ensure efficient search, insertion, and deletion operations.

### Quick Summary
---------------

* **Tree**: An undirected graph with no cycles, a single root node, and a hierarchical structure.
* **Binary Tree**: Each node has at most two children (left child and right child).
* **B-Tree**: A self-balancing search tree with a specific structure for efficient operations.
* **Heap**: A specialized tree-based data structure satisfying the heap property.

This theory note covers all the essential concepts, formulas, and problem-solving patterns required to tackle questions related to trees in the GATE CS exam.