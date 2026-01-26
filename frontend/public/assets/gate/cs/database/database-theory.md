**Database Theory**
====================

### Introduction
-----------------

Database theory forms the foundation of database systems, providing a rigorous mathematical framework for understanding data models, operations, and consistency. This note covers essential concepts, including functional dependencies, superkeys, and more.

### Core Concepts
------------------

#### Functional Dependencies (FDs)
A functional dependency is a relation between two attributes in a table, where one attribute uniquely determines the other. It's denoted as `X → Y`, meaning if all values of X are known, then all values of Y can be determined.

#### Superkeys
A superkey is a minimal set of attributes that uniquely identify each tuple in a relation. A candidate key is a subset of a superkey that has no repeating values.

### Key Formulas/Theorems
---------------------------

### Problem Solving Patterns
-----------------------------

When dealing with functional dependencies and superkeys, consider the following patterns:

1.  **Determining FDs**: Identify attribute pairs where one attribute determines the other.
2.  **Finding Superkeys**: Look for minimal sets of attributes that uniquely identify each tuple.

### Examples with Solutions
---------------------------

**Example 1: Functional Dependencies**

Suppose we have a relation `R(A, B, C, D)` with FDs:

*   `A → B`
*   `BC → D`

We want to find the number of superkeys.

```mermaid
graph LR
    A[Functional Dependency] -->|A → B|> B[Attribute B]
    A -->|BC → D|> BC[Attribute Pair (B, C)]
```

Since `A` determines `B`, and `(B, C)` together determine `D`, we can conclude that:

*   `AB` is a superkey.
*   `BC` is a superkey.

However, `ABC` is not a minimal superkey because `BC` already uniquely identifies each tuple. Therefore, the number of superkeys is 2 (excluding the trivial case where an attribute alone forms a superkey).

**Solution**: The number of superkeys = 2

### Common Pitfalls
-------------------

1.  **Missing Trivial Superkeys**: Ensure to count all minimal sets that uniquely identify each tuple.
2.  **Overlooking Attribute Dependencies**: Be cautious when dealing with attribute pairs and their dependencies.

### Quick Summary
---------------

*   Functional Dependency: `X → Y`
*   Superkey: Minimal set of attributes that uniquely identify each tuple
*   Key Patterns:
    *   Determining FDs by identifying attribute pairs where one determines the other.
    *   Finding superkeys by looking for minimal sets of attributes.

### References
--------------

For further study, refer to:

*   Ullman, J. (1980). Principles of Database Systems.
*   Silberschatz, A., & Korth, H. F. (2016). Database System Concepts.