**Functional Dependencies**
==========================

### Introduction

In the context of relational databases, functional dependencies are a fundamental concept in database design. They describe how attributes of one relation depend on the values of another relation. Understanding functional dependencies is crucial for designing optimal database schemas and ensuring data consistency.

### Core Concepts

#### Definition of Functional Dependency

Given two relations $R(A_1, A_2, \ldots, A_n)$ and $S(B_1, B_2, \ldots, B_m)$, a functional dependency (FD) is denoted as:

$$\{A_i\} \rightarrow \{B_j\}$$

where $\{A_i\}$ is called the determinant and $\{B_j\}$ is called the determined attribute.

#### Types of Functional Dependencies

*   **Simple FD**: A basic functional dependency where a single attribute determines another.
*   **Compound FD**: An FD with multiple determinants.
*   **Transitive FD**: An FD that can be inferred from other FDs in the relation.

### Key Formulas/Theorems

*   **Augmentation Rule**: If $A \rightarrow B$, then $AC \rightarrow BC$ for any set of attributes $C$.
*   **Decomposition Rule**: If $AB \rightarrow C$, then we can remove $B$ from the dependency.
*   **Transitivity Rule**: If $A \rightarrow B$ and $B \rightarrow C$, then $A \rightarrow C$.

### Problem Solving Patterns

When dealing with functional dependencies, consider the following steps:

1.  Analyze the given FDs and identify any immediate conclusions that can be drawn using the augmentation or decomposition rules.
2.  Look for transitive relationships between attributes to infer new FDs.
3.  Apply the transitivity rule to establish FDs between distant attributes.

### Examples with Solutions

**Example 1**

Given the relation $R(A, B, C)$ and the following FDs:

$$A \rightarrow B, BC \rightarrow D$$

Using the augmentation rule, we can infer that:

$$AC \rightarrow BD$$

This example demonstrates how simple FDs can be combined to form compound FDs.

**Example 2**

Suppose we have two relations $R(A, B)$ and $S(B, C)$ with the following FDs:

$$A \rightarrow B, BC \rightarrow D$$

Applying the transitivity rule, we conclude that:

$$AC \rightarrow BD$$

This example showcases how transitive FDs can be used to establish relationships between distant attributes.

### Common Pitfalls

*   Failing to apply the augmentation or decomposition rules when possible.
*   Missing opportunities for transitive inference.
*   Misinterpreting the direction of functional dependencies.

### Quick Summary

Key concepts:

*   Functional dependency definition
*   Types of FDs (simple, compound, transitive)
*   Augmentation rule
*   Decomposition rule
*   Transitivity rule

Common pitfalls:

*   Failing to apply augmentation or decomposition rules
*   Missing opportunities for transitive inference
*   Misinterpreting the direction of functional dependencies