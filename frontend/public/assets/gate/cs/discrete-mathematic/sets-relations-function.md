**Sets, Relations, and Functions**
=====================================

**Introduction**
---------------

In Discrete Mathematics, sets, relations, and functions are fundamental concepts that underlie many areas of computer science. This note covers the theoretical aspects of these topics, with a focus on their applications in problem-solving.

**Core Concepts**
----------------

### Sets

A set is an unordered collection of unique elements, denoted by curly brackets `{}`. For example, `{a, b, c}` is a set containing three distinct elements.

#### Set Operations

*   **Union**: The union of two sets A and B, denoted as `A ∪ B`, is the set of all elements that are in A or in B or in both.
*   **Intersection**: The intersection of two sets A and B, denoted as `A ∩ B`, is the set of all elements that are in both A and B.
*   **Difference**: The difference of two sets A and B, denoted as `A \ B`, is the set of all elements that are in A but not in B.

### Relations

A relation R between two sets A and B is a subset of the Cartesian product `A × B`. It can be represented using ordered pairs `(a, b)` where `a ∈ A` and `b ∈ B`.

#### Types of Relations

*   **Reflexive**: A relation R on a set A is reflexive if for every `a ∈ A`, `(a, a) ∈ R`.
*   **Symmetric**: A relation R on a set A is symmetric if for every `a, b ∈ A`, `(a, b) ∈ R` implies `(b, a) ∈ R`.
*   **Transitive**: A relation R on a set A is transitive if for every `a, b, c ∈ A`, `(a, b) ∈ R` and `(b, c) ∈ R` imply `(a, c) ∈ R`.

### Functions

A function f from a set A to a set B is a relation that satisfies two properties:

*   **Functionality**: For every `a ∈ A`, there exists at most one `b ∈ B` such that `(a, b) ∈ f`.
*   **Totality**: For every `a ∈ A`, there exists exactly one `b ∈ B` such that `(a, b) ∈ f`.

#### Types of Functions

*   **Injection**: A function f from a set A to a set B is an injection if for every `a1, a2 ∈ A`, `(a1, b) ∈ f` and `(a2, b) ∈ f` imply `a1 = a2`.
*   **Surjection**: A function f from a set A to a set B is a surjection if for every `b ∈ B`, there exists an `a ∈ A` such that `(a, b) ∈ f`.
*   **Bijection**: A function f from a set A to a set B is a bijection if it is both an injection and a surjection.

**Key Formulas/Theorems**
-------------------------

### Inclusion-Exclusion Principle

For any sets `A`, `B`, and `C`:

\[|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|\]

### Schröder-Bernstein Theorem

If there exists an injection from a set `A` to a set `B`, and an injection from `B` to `A`, then `A` and `B` have the same cardinality.

**Problem Solving Patterns**
---------------------------

*   **Use of Counterexamples**: When proving that something is impossible, try to find a counterexample.
*   **Analysis of Relations**: When working with relations, identify their types (reflexive, symmetric, transitive) and use them to deduce properties of the relation.

**Examples with Solutions**
---------------------------

### Example 1: Sets

Let `A = {a, b}` and `B = {1, 2, 3}`. Find the union, intersection, and difference of `A` and `B`.

```markdown
Union: A ∪ B = {a, b, 1, 2, 3}
Intersection: A ∩ B = ∅ (empty set)
Difference: A \ B = {a, b}
```

### Example 2: Relations

Let R be a relation on the set `A = {a, b}` such that `(a, b) ∈ R` and `(b, a) ∈ R`. Show that R is symmetric.

```markdown
Since (a, b) ∈ R and (b, a) ∈ R, by definition of symmetry,
we have (b, a) ∈ R. Therefore, R is symmetric.
```

### Example 3: Functions

Let `f` be a function from the set `{1, 2}` to the set `{a, b}` such that `f(1) = a` and `f(2) = b`. Show that `f` is both an injection and a surjection.

```markdown
Since f(1) = a and f(2) = b, for every a ∈ {a, b}, there exists exactly one x ∈ {1, 2} such that f(x) = a.
Therefore, f is an injection. Since every element in the codomain {a, b} has a corresponding element in the domain {1, 2},
f is also a surjection. Hence, f is a bijection.
```

**Common Pitfalls**
------------------

*   Failing to distinguish between different types of relations (reflexive, symmetric, transitive).
*   Confusing functionality and totality for functions.
*   Not analyzing the properties of sets and relations thoroughly enough.

**Quick Summary**
----------------

*   Sets: unordered collections of unique elements
*   Relations: subsets of Cartesian products with specific types (reflexive, symmetric, transitive)
*   Functions: satisfy functionality and totality
*   Types of functions: injection, surjection, bijection