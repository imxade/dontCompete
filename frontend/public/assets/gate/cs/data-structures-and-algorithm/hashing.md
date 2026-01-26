**Hashing**
================

### Introduction
---------------

Hashing is a fundamental concept in data structures and algorithms that enables efficient storage, search, and manipulation of large datasets. It maps keys to specific locations in a table using hash functions.

### Core Concepts
-----------------

#### Hash Functions
A hash function takes an input key (a string or integer) and produces a fixed-size output, known as the hash value or digest. The goal is to produce a unique hash value for each distinct input, minimizing collisions (hash values for different inputs).

#### Hash Tables
Hash tables are data structures that store key-value pairs using hash functions to map keys to indices of an array. Each index corresponds to a slot in the table.

### Key Formulas/Theorems
-------------------------

*   **Expected number of keys in a slot**:
    \[
    E = \frac{n}{m}
    \]
    where $n$ is the number of keys and $m$ is the number of slots.

### Problem Solving Patterns
-----------------------------

1.  **Hashing Schemes**: Identify the type of hashing scheme used (e.g., uniform, non-uniform).
2.  **Collision Resolution**: Understand how collisions are handled (e.g., chaining, open addressing).

### Examples with Solutions
---------------------------

**Example 1: Expected number of keys in a slot**

Suppose we have $n$ keys and $m$ slots in a hash table. If the hashing scheme uses two uniform hash functions, $h_1$ and $h_2$, for odd and even keys respectively, what is the expected number of keys in a slot?

```python
# Import necessary modules
import math

# Define variables
n = 1000  # Number of keys
m = 500   # Number of slots

# Calculate expected number of keys in a slot
expected_keys_per_slot = n / m

print("Expected number of keys per slot:", expected_keys_per_slot)
```

**Solution**: Using the formula $E = \frac{n}{m}$, we get:

\[
E = \frac{1000}{500} = 2
\]

### Common Pitfalls
--------------------

*   **Misunderstanding collision resolution mechanisms**
*   **Failing to consider the expected behavior of hash functions**

### Quick Summary
-----------------

*   Hashing maps keys to specific locations using hash functions.
*   Hash tables store key-value pairs using hash functions.
*   The expected number of keys in a slot is given by $E = \frac{n}{m}$.

Note: This summary will be updated with additional concepts as the theory note evolves.