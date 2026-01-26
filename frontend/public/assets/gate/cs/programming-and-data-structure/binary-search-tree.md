**Binary Search Tree**
=======================

### Introduction
-----------------

A binary search tree (BST) is a data structure in which each node has at most two children, referred to as left child and right child. The nodes of a BST are arranged in such a way that for any given node, all elements in its left subtree are less than the node's value, and all elements in its right subtree are greater.

### Core Concepts
----------------

*   **Root Node**: The topmost node of the tree.
*   **Left Child**: The node to the left of another node.
*   **Right Child**: The node to the right of another node.
*   **Leaf Nodes**: Nodes with no children (i.e., the bottom-most nodes).

### Key Formulas/Theorems
-------------------------

None

### Problem Solving Patterns
---------------------------

1.  **Finding an Element in a BST**: Given a value, find the node containing that value in a BST.

    ```mermaid
    graph LR;
        A[Root] --> B[Compare];
        B -->|Less| C[Left Child];
        B -->|Greater| D[Right Child];
    ```
2.  **Finding an Element Smaller than Max**: Given the maximum element, find another element smaller than it.

    ```mermaid
    graph LR;
        A[Root] --> B[Compare with Max];
        B -->|Smaller| C[Left Subtree];
        B -->|Greater or Equal| D[Right Subtree or Root itself];
    ```

### Examples with Solutions
---------------------------

**Q1: Find an element in a BST**

*   Given a BST and a value `x`, find the node containing `x`.
*   Start at the root.
*   If `x` is less than the current node's value, move to the left child. Otherwise, move to the right child.
*   Repeat until `x` is found or the leaf nodes are reached.

**Q2: Find an element smaller than Max**

*   Given a BST and its maximum element, find another element smaller than it.
*   If the root has a right subtree, the root itself is smaller than the maximum value.
*   Otherwise, if the root does not have a right subtree, the left child of the root is the required element.

### Common Pitfalls
------------------

1.  **Not considering edge cases** (e.g., an empty tree).
2.  **Misunderstanding node relationships** (e.g., mixing up left and right subtrees).

### Quick Summary
-----------------

*   Binary Search Trees have nodes with at most two children.
*   Elements in the left subtree are less than the node's value, and elements in the right subtree are greater.
*   Finding an element involves comparing values with node values.
*   Finding an element smaller than Max requires considering node relationships.

This theory note provides a comprehensive overview of binary search trees, including their core concepts, problem-solving patterns, examples, common pitfalls, and quick summary.