Sorting
================

Introduction
------------

Sorting is a fundamental operation in computer science that rearranges elements of an array or list in a specific order, such as ascending or descending. The efficiency of sorting algorithms is crucial in various applications, including data analysis, database management, and web development.

Core Concepts
-------------

### Sorting Algorithms

There are several types of sorting algorithms, each with its own strengths and weaknesses:

1.  **Bubble Sort**: A simple algorithm that repeatedly iterates through the array, comparing adjacent elements and swapping them if they are in the wrong order.
2.  **Selection Sort**: An algorithm that selects the smallest (or largest) element from the unsorted portion of the array and swaps it with the first element of the unsorted portion.
3.  **Insertion Sort**: A stable algorithm that builds the sorted array one item at a time by inserting each new element into its proper position.
4.  **Merge Sort**: A divide-and-conquer algorithm that splits the array into smaller chunks, sorts them recursively, and then merges the sorted chunks back together.
5.  **Quick Sort**: An efficient algorithm that selects a pivot element, partitions the array around it, and recursively sorts the sub-arrays on either side.

Key Formulas/Theorems
----------------------

### Time Complexity

*   Bubble sort: O(n^2)
*   Selection sort: O(n^2)
*   Insertion sort: O(n^2)
*   Merge sort: O(n log n)
*   Quick sort (average case): O(n log n)

Problem Solving Patterns
------------------------

### Identifying the Best Algorithm

When faced with a sorting problem, consider the following factors to choose the most efficient algorithm:

*   **Array size**: For small arrays, insertion sort or selection sort may be sufficient. For larger arrays, merge sort or quick sort might be more suitable.
*   **Data type**: If the array contains duplicate elements or is nearly sorted, insertion sort or bubble sort could be a good choice.
*   **Stability**: If preserving the order of equal elements is crucial, use a stable algorithm like merge sort or insertion sort.

Examples with Solutions
-----------------------

### Example 1: Insertion Sort

Suppose we have an array `[5, 2, 8, 3]` and want to sort it in ascending order using insertion sort:

1.  Compare the first element (5) with the second element (2). Since 2 is smaller, swap them.
    *   `[2, 5, 8, 3]`
2.  Compare the first two elements (2, 5). Since 2 is still smaller, no swap is needed.
    *   `[2, 5, 8, 3]`
3.  Repeat this process until the entire array is sorted: `[2, 3, 5, 8]`

### Example 2: Merge Sort

Given an array `[4, 2, 9, 6, 1]`, let's use merge sort to sort it in ascending order:

```mermaid
graph LR;
    A[4, 2, 9, 6, 1] --> B[Split into [4, 2], [9, 6, 1]];
    C[Split [4, 2] further into [2, 4]] --> D[Merge [2, 4] with remaining elements];
    E[Split [9, 6, 1] further into [1, 6, 9]] --> F[Merge [1, 6, 9] with merged subarray from D];
```

Common Pitfalls
----------------

### Misunderstanding Time Complexity

Be cautious when analyzing time complexity. Remember that:

*   O(n^2) is generally less efficient than O(n log n).
*   Bubble sort and selection sort have the same time complexity, but insertion sort can be more efficient for small arrays.

Quick Summary
--------------

*   **Sorting algorithms**: Bubble sort, selection sort, insertion sort, merge sort, quick sort.
*   **Time complexity**: O(n^2) (bubble sort, selection sort), O(n log n) (merge sort, quick sort).
*   **Problem solving patterns**: Identify the best algorithm based on array size, data type, and stability requirements.