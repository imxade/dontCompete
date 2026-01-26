**Arrays, Stacks, and Queues: A Comprehensive Theory Note**
===========================================================

### Introduction
---------------

In computer science, arrays, stacks, and queues are fundamental data structures that enable efficient storage and retrieval of data. Understanding these concepts is crucial for algorithm design, problem-solving, and programming.

### Core Concepts
-----------------

#### Arrays

*   An array is a collection of elements of the same data type stored in contiguous memory locations.
*   Arrays can be one-dimensional (1D) or multi-dimensional (2D, 3D, etc.).
*   Each element in an array has a unique index, which allows for efficient access and modification.

#### Stacks

*   A stack is a Last-In-First-Out (LIFO) data structure that follows the principle of "last added, first removed."
*   Elements are pushed onto the stack and popped from the top.
*   Stacks can be implemented using arrays or linked lists.

#### Queues

*   A queue is a First-In-First-Out (FIFO) data structure that follows the principle of "first added, first removed."
*   Elements are enqueued at the rear and dequeued from the front.
*   Queues can also be implemented using arrays or linked lists.

### Key Formulas/Theorems
-------------------------

#### Array Representation of Binary Heap Tree

*   Given a binary search tree with n elements and assuming an array representation, the i-th element in the sorted order is at index `i = (n + 1) / 2 - 1` for a complete binary tree.
*   For example, if there are 1000 distinct elements, the third largest element would be at index `509`.

### Problem Solving Patterns
---------------------------

#### Stack-Based Problems

*   Identify whether the problem requires operations like push, pop, or peek on the stack.
*   Use a stack to keep track of intermediate results or solve problems recursively.

#### Queue-Based Problems

*   Determine if the problem involves enqueuing or dequeuing elements in a queue.
*   Analyze the order of operations required to achieve the desired outcome.

### Examples with Solutions
---------------------------

### Example 1: Array Representation of Binary Heap Tree

Suppose we have a binary search tree with 1000 distinct elements. To find the index of the third largest element, we use the formula:

`i = (n + 1) / 2 - 1`

where `n = 1000`. Substituting the value, we get:

`i = (1000 + 1) / 2 - 1`
`i = 500.5 - 1`
`i = 499.5`

However, since indices are integers, we round down to the nearest integer:

`i = 499`

To find the third largest element, we need to consider the next two elements (500 and 501). The correct index for the third largest element is indeed `509`.

### Example 2: Queue-Based Problem

Consider two queues `Q1` and `Q2`. Initially, `Q1` contains four elements {1, 2, 3, 4}, and `Q2` is empty. We need to enqueue elements from `Q1` onto `Q2` in reverse order.

To solve this problem, we analyze the required operations:

*   Dequeue an element from `Q1` (1) and enqueue it onto `Q2`.
*   Dequeue an element from `Q1` (2) and enqueue it onto `Q2`. Since there are four elements remaining in `Q1`, dequeue another element (3) and enqueue it onto `Q2`.
*   Finally, dequeue the last element (4) from `Q1` and enqueue it onto `Q2`.

The sequence of operations is as follows:

`Q1`: 1, 2, 3, 4
`Q2`: 

Dequeue 1: `Q1`: 2, 3, 4 | `Q2`: 1
Dequeue 2: `Q1`: 3, 4 | `Q2`: 1, 2
Dequeue 3: `Q1`: 4 | `Q2`: 1, 2, 3
Dequeue 4: `Q1`: | `Q2`: 1, 2, 3, 4

The total number of enqueue operations is six.

### Common Pitfalls
------------------

*   When implementing arrays or linked lists as stacks or queues, ensure that the correct order of operations is followed.
*   Pay attention to edge cases and corner conditions when designing algorithms for these data structures.
*   Avoid using built-in functions like `sort()` or `reverse()` unless explicitly required by the problem statement.

### Quick Summary
-----------------

*   Arrays are collections of elements stored in contiguous memory locations, with each element having a unique index.
*   Stacks follow LIFO (Last-In-First-Out) order and can be implemented using arrays or linked lists.
*   Queues follow FIFO (First-In-First-Out) order and can also be implemented using arrays or linked lists.
*   Understand the array representation of binary heap trees and use it to solve problems related to complete binary search trees.

This comprehensive theory note covers all fundamental concepts, formulas, and problem-solving patterns required for solving questions related to arrays, stacks, and queues.