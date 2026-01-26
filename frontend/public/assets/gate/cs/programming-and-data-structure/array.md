**Array Theory Note**
=======================

**Introduction**
---------------

An array is a fundamental data structure in computer science that represents a collection of elements of the same data type stored in contiguous memory locations. In this note, we will cover the theoretical concepts and formulas required to solve problems related to arrays.

**Core Concepts**
----------------

### Array Representation

An array can be represented as:

*   A one-dimensional array: `a[i]` where `i` is an index
*   A multi-dimensional array: `a[i][j]` where `i` and `j` are indices

### Array Indexing

Array indexing starts from 0, which means the first element of an array is at index 0.

### Array Operations

Common array operations include:

*   Accessing an element: `a[i]`
*   Modifying an element: `a[i] = x`
*   Assigning a value to an entire array: `a = [x, y, z]`

**Key Formulas/Theorems**
-------------------------

### Array Subscripts

For a multi-dimensional array `a` of size `m x n`, the subscripts are given by:

```latex
i \in {0, 1, ..., m-1}
j \in {0, 1, ..., n-1}
```

**Problem Solving Patterns**
---------------------------

### Identifying Array Indices

In a multi-dimensional array, each dimension has its own index. To access an element at position `(i, j)`, you need to use both indices.

### Handling Array Bounds

When accessing or modifying elements in an array, ensure that the indices are within the bounds of the array.

**Examples with Solutions**
---------------------------

### Example 1: ANSI C Programme

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    int a[3][3][3] = {{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
                     {{10, 11, 12}, {13, 14, 15}, {16, 17, 18}},
                     {{19, 20, 21}, {22, 23, 24}, {25, 26, 27}}};
    int i = 0, j = 0, k = 0;

    for (i = 0; i < 3; i++) {
        for (k = 0; k < 3; k++)
            printf("%d ", a[i][j][k]);
        printf("\n");
    }

    return 0;
}
```

Solution:

```markdown
1   2    3
10  11  12
19  20  21
```

### Example 2: Longest Subarray with Two Distinct Integers

Suppose we have an array `X` of size `n` containing positive integers. We want to find the length of the longest subarray that contains at most two distinct integers.

```c
int maxlen = 0;
int first = 0, second = 0;

for (int i = 0; i < n; i++) {
    if (X[i] == first) {
        len2++;
        len1++;
    } else if (X[i] == second) {
        len2++;
        len1 = (P); // missing expression
        second = first;
    } else {
        len2 = (Q); // missing expression
        len1 = 1; second = first;
    }

    if (len2 > maxlen)
        maxlen = len2;
}
```

Solution:

*   `(P)` should be `len1 - 1`
*   `(Q)` should be `0`

**Common Pitfalls**
-----------------

### Array Indexing Errors

Ensure that indices are within the bounds of the array to avoid segmentation faults or undefined behavior.

### Incorrect Array Operations

Be mindful of the order of operations when accessing or modifying elements in an array.

**Quick Summary**
-----------------

*   Arrays are represented as contiguous memory locations.
*   Multi-dimensional arrays use subscripts for indexing.
*   Be aware of array bounds and correct index usage.
*   Solve problems using correct array operations.

Note: This note is designed to be a starting point for your studies. Practice problems and additional examples are recommended to reinforce the concepts presented here.