**Complexity Analysis**
========================

**Introduction**
---------------

Complexity analysis is a crucial aspect of algorithm design and evaluation, focusing on the amount of resources (time or space) an algorithm requires as the size of the input increases. In this theory note, we'll delve into the principles, formulas, and techniques required to solve questions related to complexity analysis.

**Core Concepts**
-----------------

### Big O Notation

Big O notation is used to describe the upper bound of an algorithm's time or space complexity. It represents the worst-case scenario, where the algorithm performs the maximum number of operations.

*   $O(f(n))$ = Big O notation
*   Examples:
    *   $O(1)$ (constant time)
    *   $O(log n)$ (logarithmic time)
    *   $O(n)$ (linear time)
    *   $O(n log n)$ (n log n time)

### Big Ω Notation

Big Ω notation is used to describe the lower bound of an algorithm's time or space complexity. It represents the best-case scenario, where the algorithm performs the minimum number of operations.

*   $\Omega(f(n))$ = Big Ω notation
*   Examples:
    *   $\Omega(1)$ (constant time)
    *   $\Omega(log n)$ (logarithmic time)
    *   $\Omega(n)$ (linear time)
    *   $\Omega(n^2)$ (quadratic time)

### Time Complexity Classes

Time complexity classes are based on the growth rate of an algorithm's running time.

*   $O(1)$: constant time
*   $O(log n)$: logarithmic time
*   $O(n)$: linear time
*   $O(n log n)$: n log n time
*   $O(n^2)$: quadratic time

### Recurrence Relations

Recurrence relations are a mathematical way to describe the time or space complexity of an algorithm. They often involve a recursive function that calls itself until it reaches a base case.

**Key Formulas/Theorems**
-------------------------

### Master Theorem

The master theorem is used to solve recurrence relations of the form:

$T(n) = aT(\frac{n}{b}) + f(n)$

*   $a \geq 1$
*   $b > 1$

The master theorem states that:

*   If $f(n) = O(n^d)$ and $a < b^d$, then $T(n) = \Theta(n^{\log_b a})$.
*   If $f(n) = O(n^d)$ and $a = b^d$, then $T(n) = \Theta(n^d \log n)$.
*   If $f(n) = O(n^d)$ and $a > b^d$, then $T(n) = \Theta(f(n))$.

### Akra-Bazzi Theorem

The Akra-Bazzi theorem is used to solve recurrence relations of the form:

$T(n) = aT(\frac{n}{b}) + n^p g(n)$

*   $a \geq 1$
*   $b > 1$

The Akra-Bazzi theorem states that:

*   If $g(n) = O(1)$, then $T(n) = \Theta(n^p)$.
*   If $g(n) = \Omega(n^p)$ and $a < b^p$, then $T(n) = \Theta(n^{\log_b a} \log n)$.

**Problem Solving Patterns**
---------------------------

### Solving Recurrence Relations

To solve recurrence relations, we can use the master theorem or Akra-Bazzi theorem. We need to identify the recurrence relation and apply the appropriate theorem.

### Identifying Time Complexity Classes

We can identify time complexity classes by analyzing the growth rate of an algorithm's running time. We can use Big O notation to describe the upper bound of an algorithm's time complexity.

**Examples with Solutions**
---------------------------

### Example 1: Solving a Recurrence Relation using Master Theorem

Suppose we have the following recurrence relation:

$T(n) = 2T(\frac{n}{2}) + n$

We can apply the master theorem to solve this recurrence relation.

*   $a = 2$
*   $b = 2$
*   $f(n) = n$

Since $a < b^1$, we have:

$T(n) = \Theta(n^{\log_2 2}) = \Theta(n)$

### Example 2: Identifying Time Complexity Class

Suppose we have an algorithm that takes as input a list of integers and performs the following operations:

*   Iterate through the list
*   For each element, iterate through the rest of the list to find its pair

We can analyze the growth rate of this algorithm's running time.

*   The outer loop iterates through the list, which has $n$ elements.
*   The inner loop iterates through the rest of the list, which has $n-1$, $n-2$, ..., 1 elements.
*   Since the inner loop runs for each element in the outer loop, the total number of iterations is:

$n + (n-1) + (n-2) + ... + 1 = \frac{n(n+1)}{2}$

Since $\frac{n(n+1)}{2} = O(n^2)$, we can conclude that this algorithm has a time complexity of $O(n^2)$.

**Common Pitfalls**
------------------

### Ignoring Constants

When analyzing the time or space complexity of an algorithm, it's easy to ignore constants. However, in Big O notation, constants are included as part of the complexity class.

*   For example, $O(3n)$ is equivalent to $O(n)$.
*   Similarly, $\Omega(n^2 + 1)$ is equivalent to $\Omega(n^2)$.

### Misapplying Master Theorem

The master theorem requires specific conditions to be met. If these conditions are not met, the master theorem cannot be applied directly.

*   For example, if $f(n) = O(n \log n)$ and $a < b^1$, we cannot apply the master theorem.
*   In this case, we need to use other techniques, such as Akra-Bazzi theorem or manual calculation.

**Quick Summary**
-----------------

*   Big O notation describes the upper bound of an algorithm's time or space complexity.
*   Big Ω notation describes the lower bound of an algorithm's time or space complexity.
*   Time complexity classes are based on the growth rate of an algorithm's running time.
*   Recurrence relations can be solved using master theorem, Akra-Bazzi theorem, or manual calculation.

By following these guidelines and techniques, you should be able to solve questions related to complexity analysis with confidence. Practice problems and exercises will help reinforce your understanding and improve your problem-solving skills.