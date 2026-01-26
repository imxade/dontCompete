**Array Theory Note**
=====================

### Introduction
------------

An array is a fundamental data structure used to store and manipulate collections of elements of the same data type. It provides efficient access, storage, and manipulation capabilities for large datasets. This note covers the key concepts, formulas, and problem-solving patterns required to tackle questions related to arrays.

### Core Concepts
-----------------

#### Array Representation

An array can be represented as a one-dimensional list of elements, where each element is identified by its index or position in the list.

```mermaid
graph LR
A[Array] -->|Elements|> B[List]
```

#### Indexing and Subscript Notation

Arrays use indexing to access and manipulate individual elements. The indexing starts from 0, meaning the first element has an index of 0, the second element has an index of 1, and so on.

```mermaid
graph LR
A[Array] -->|Indexing|> B[List with Index]
```

### Key Formulas/Theorems
-------------------------

*   **Big O notation for Array operations**

$$
\begin{align*}
T(n) &= O(n) \text{ for access, update, and search}\\
T(n) &= O(1) \text{ for constant-time operations (e.g., array initialization)}
\end{align*}
$$

### Problem Solving Patterns
---------------------------

#### Heaps and Heapification

A heap is a specialized tree-based data structure that satisfies the heap property: the parent node is either greater than or equal to its child nodes (max-heap) or less than or equal to its child nodes (min-heap).

```mermaid
graph LR
A[Heap] -->|Max-Heap Property|> B[Parent >= Child]
```

Heapification is the process of transforming an array into a heap.

#### Example: Heapification

Given the array `[82, 101, 90, 11, 111, 75, 33, 131, 44, 93]`, we can perform heapification to get the final heapified array as `[131, 111, 90, 101, 93, 75, 33, 11, 44, 82]`.

```python
import heapq

def heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_helper(arr, i, n)

def heapify_helper(arr, i, n):
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[i]:
        largest = left_child
    else:
        largest = i

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_helper(arr, largest, n)

# Example usage
arr = [82, 101, 90, 11, 111, 75, 33, 131, 44, 93]
heapify(arr)
print(arr)  # Output: [131, 111, 90, 101, 93, 75, 33, 11, 44, 82]
```

### Examples with Solutions
---------------------------

#### Q1: Heapification

Given the array `[82, 101, 90, 11, 111, 75, 33, 131, 44, 93]`, which one of the following options represents the first three elements in the heapified array?

```python
# Solution
arr = [82, 101, 90, 11, 111, 75, 33, 131, 44, 93]
heapify(arr)
print(arr[:3])  # Output: [131, 111, 90]
```

### Common Pitfalls
-----------------

*   **Incorrect indexing**: Be aware of the starting index (0) and how it affects array operations.
*   **Misunderstanding heap properties**: Ensure you understand the max-heap or min-heap property for correct heapification.

### Quick Summary
---------------

*   Array representation: one-dimensional list with indexing
*   Key formulas/theorems:
	+ Big O notation for Array operations
*   Problem-solving patterns:
	+ Heaps and heapification

This comprehensive note covers the essential concepts, formulas, and problem-solving patterns required to tackle questions related to arrays.