**Permutation**
===============

**Introduction**
---------------

A permutation of a set is an arrangement of its elements in a particular order. In this note, we'll focus on permutations that separate two subsets `A` and `B` within a larger set `U`.

**Core Concepts**
-----------------

### Permutations

*   A permutation of a set is a bijection from the set to itself.
*   The number of permutations of a set with `n` elements is `n!`, read as "n factorial".

### Symmetric Difference

The symmetric difference of two sets `A` and `B` is defined as:

```latex
\Delta = A \cup B - (A \cap B)
```

This can be thought of as the set of elements that are in either `A` or `B`, but not both.

**Key Formulas/Theorems**
-------------------------

### Number of Permutations Separating Two Sets

Let `U` be a set with `n` elements, and let `A` and `B` be two subsets such that `A ∩ B = φ`. We say that a permutation of `U` separates `A` from `B` if all members of `A` appear before any member of `B`, or vice versa.

The number of permutations of `U` that separate `A` from `B` is:

```latex
\frac{n!}{k!(n-k)!}
```

where `k` is the size of `A`.

### Proof

Consider the permutation of `U` that starts with all elements of `A`. There are `n - k` positions remaining for elements of `B`, which can be arranged in `(n - k)!` ways. The remaining `k` positions must be filled by elements of `A`, which can be done in `k!` ways.

Since either all elements of `A` or `B` appear first, we multiply the result by 2 to get the total number of permutations that separate `A` from `B`.

**Problem Solving Patterns**
---------------------------

*   When counting permutations that separate two sets, think about the "first" set and how many ways its elements can be arranged.
*   Use the formula for combinations (`C(n, k) = n! / (k!(n-k)!)` ) to find the number of ways to arrange the remaining set.

**Examples with Solutions**
---------------------------

### Example 1

Suppose we have a set `U` with 5 elements and two subsets `A` and `B`, where `A` has 2 elements and `B` has 3 elements. Find the number of permutations that separate `A` from `B`.

```latex
n = 5, k = 2
```

The number of permutations is:

```latex
\frac{5!}{2!(5-2)!} = \frac{120}{2*6} = 10
```

### Example 2

Suppose we have a set `U` with 7 elements and two subsets `A` and `B`, where `A` has 3 elements and `B` has 4 elements. Find the number of permutations that separate `A` from `B`.

```latex
n = 7, k = 3
```

The number of permutations is:

```latex
\frac{7!}{3!(7-3)!} = \frac{5040}{6*24} = 35
```

**Common Pitfalls**
-------------------

*   Don't confuse the symmetric difference with the union or intersection.
*   When applying formulas, make sure to check units and signs.

**Quick Summary**
-----------------

*   Permutations that separate two sets: `n! / (k!(n-k)!)`
*   Symmetric difference: `A ∪ B - (A ∩ B)`
*   Use the formula for combinations when counting permutations

This comprehensive note covers the theory of permutations separating two sets, including core concepts, key formulas and theorems, problem-solving patterns, examples with solutions, common pitfalls, and a quick summary for revision.