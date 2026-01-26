**Relation**
================

### Introduction
----------------

A relation is a mathematical concept used to describe the connection or relationship between objects or elements in a set. It's an essential topic in discrete mathematics and combinatorics, frequently appearing in GATE CS exam questions.

### Core Concepts
-----------------

#### Definition of Relation
A relation R from a set A to a set B is defined as a subset of the Cartesian product A × B. In other words:

$$R \subseteq A \times B$$

This means that for every pair (a, b) in R, a belongs to A and b belongs to B.

#### Types of Relations
There are several types of relations, including:

*   **Reflexive relation**: For all a in A, (a, a) is in the relation.
*   **Symmetric relation**: If (a, b) is in the relation, then (b, a) must also be in the relation.
*   **Transitive relation**: If (a, b) and (b, c) are in the relation, then (a, c) must also be in the relation.

#### Relation Composition
Given two relations R1 from A to B and R2 from B to C, the composition of R1 and R2 is defined as:

$$R1 \circ R2 = {(a, c) | \exists b \in B : (a, b) \in R1 \text{ and } (b, c) \in R2}$$

### Key Formulas/Theorems
---------------------------

### Problem Solving Patterns
---------------------------------

*   **Symmetric Difference**: The symmetric difference of two sets A and B is defined as:
    $$
    A \triangle B = (A \cup B) - (A \cap B)
    $$
    This can be used to find the number of permutations that separate A from B in question Q1.

### Examples with Solutions
---------------------------

**Example 1**

Find the symmetric difference of two sets A and B, where A = {a, b} and B = {b, c}.

**Solution**

Using the definition of symmetric difference:

$$A \triangle B = (A \cup B) - (A \cap B)$$

We have:

*   $A \cup B = {a, b, c}$
*   $A \cap B = {b}$

Therefore,

$$A \triangle B = {a, c}$$

**Example 2**

Find the number of permutations that separate A from B in question Q1.

**Solution**

Using the symmetric difference concept:

*   We want to find the number of permutations of U that separate A from B.
*   This is equivalent to finding the number of permutations of $U - (A \cup B)$ and multiplying it by 2 (for the two possible orderings: A before B or B before A).
*   Therefore, the answer is:

$$\frac{n!}{(n-k)!} \times 2$$

### Common Pitfalls
------------------------

*   Students often confuse symmetric difference with intersection.
*   Be careful when applying relation composition.

### Quick Summary
------------------

*   Definition of relation: A subset of the Cartesian product A × B.
*   Types of relations: Reflexive, Symmetric, Transitive.
*   Relation composition: (a, c) ∈ R1 ∘ R2 if there exists b such that (a, b) ∈ R1 and (b, c) ∈ R2.
*   Symmetric difference: $A \triangle B = (A \cup B) - (A \cap B)$
*   Permutations separating A from B: $\frac{n!}{(n-k)!} \times 2$