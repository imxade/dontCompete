**Combinatorics: Counting Theory Note**
=====================================

**Introduction**
---------------

Combinatorics is a branch of mathematics that deals with counting and arranging objects. It involves finding the number of ways to select or arrange items, often subject to certain constraints or rules. In this note, we will focus on the fundamental concepts and formulas required for solving combinatorial problems.

**Core Concepts**
----------------

*   **Permutations**: A permutation is an arrangement of objects in a specific order. For example, the letters "abc" can be arranged as "bca", "cab", etc.
*   **Combinations**: A combination is a selection of objects without considering their order. For instance, selecting 3 items from a set of 5 can be represented as {a, b, c} or {c, b, d}, but not {a, b, c} and {b, a, c}.
*   **Binomial Coefficients**: A binomial coefficient is the number of ways to choose k objects from n items without repetition. It is denoted as "n choose k" and calculated using the formula:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

where n! represents the factorial of n (i.e., the product of all positive integers up to n).

**Key Formulas/Theorems**
-------------------------

### **The Pigeonhole Principle**

If k items are put into n containers, with k > n, then at least one container must contain more than one item.

$$\text{Pigeonhole Principle: } \quad k > n \Rightarrow \exists i \in \{1, 2, ..., n\} \text{ s.t. } m_i > 1$$

### **The Multiplication Principle**

If there are n ways to choose one item and m ways to choose another item, then the total number of ways to choose both items is the product of these counts:

$$\text{Multiplication Principle: } \quad (n)(m) = nm$$

**Problem Solving Patterns**
---------------------------

### **Pattern 1: Counting Combinations with Restrictions**

*   Identify the constraint(s)
*   Determine the total number of combinations without restrictions
*   Apply the principle of inclusion-exclusion to account for overcounting or undercounting due to constraints

### **Pattern 2: Using Permutations and Combinations Together**

*   Use permutations when order matters
*   Use combinations when order does not matter

**Examples with Solutions**
---------------------------

### **Example 1**

Three students (A, B, C) need to sit in a row. How many different seating arrangements can be made?

Solution:

Using the multiplication principle and considering the permutations of each student:

$$\text{Total Arrangements} = \binom{3}{1}\cdot \binom{2}{1} \cdot \binom{1}{1} = 6$$

### **Example 2**

A set consists of 4 letters: {a, b, c, d}. How many unique subsets can be formed?

Solution:

We will use the formula for combinations (n choose k), where n is the total number of items and k is the number of items to choose. Here, we want to find the number of subsets with any size from 0 to 4.

$$\text{Total Subsets} = \binom{4}{0} + \binom{4}{1} + \binom{4}{2} + \binom{4}{3} + \binom{4}{4}$$

Applying the combination formula and summing up:

$$\text{Total Subsets} = 5 + 4 + 6 + 4 + 1 = 20$$

**Common Pitfalls**
------------------

*   Failure to account for overcounting or undercounting when applying combinatorial formulas
*   Incorrect application of permutation versus combination rules
*   Failing to recognize the Pigeonhole Principle's applicability