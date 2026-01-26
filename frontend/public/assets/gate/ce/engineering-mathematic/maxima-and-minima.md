**Maxima and Minima**
=====================

### Introduction
-----------------

Maxima and minima are crucial concepts in calculus, used to analyze the behavior of functions. In this note, we'll cover the principles, key formulas, problem-solving patterns, and common pitfalls.

### Core Concepts
------------------

#### Definition
-----------

A function f(x) is said to have a maximum (or minimum) at x = c if there exists an interval around c such that f(c) ≥ (≤) f(x) for all x in the interval. The point where this occurs is called a local maxima (minima).

#### Types of Maxima and Minima
-------------------------------

*   **Local Maximum**: A function has a maximum at x = c if f'(c) = 0 and f''(c) < 0.
*   **Local Minimum**: A function has a minimum at x = c if f'(c) = 0 and f''(c) > 0.

### Key Formulas/Theorems
-------------------------

1.  **First Derivative Test**:
    $\boxed{f&#39;(c) = 0}$ 
    indicates that the function has a critical point at x = c.
2.  **Second Derivative Test**:

    For local maxima/minima:

    $f&#39;&#39;(c) > 0$ for minima,
    $f&#39;&#39;(c) < 0$ for maxima

3.  **Critical Points**:
    A critical point is where f'(x) = 0.

### Problem Solving Patterns
---------------------------

1.  Find the critical points of a function.
2.  Apply the second derivative test to determine if each critical point corresponds to a local maximum, minimum, or neither.
3.  Analyze the behavior of the function using the first and second derivatives.

### Examples with Solutions
-----------------------------

**Example:** Find the maxima/minima for f(x) = x^3 - 6x^2 + 9x + 2.

1.  **Step 1:** Find critical points by solving f'(x) = 0.
    $f&#39;(x) = 3x^2 - 12x + 9 = (x-1)(3x-9)$
    Critical points: x = 1, x = 3

2.  **Step 2:** Apply the second derivative test.

    $f&#39;&#39;(x) = 6x - 12$

    At x = 1:
    $f&#39;&#39;(1) = 6(1) - 12 < 0$, so it's a local maximum.
    At x = 3:
    $f&#39;&#39;(3) = 6(3) - 12 > 0$, so it's a local minimum.

### Common Pitfalls
-------------------

*   Misidentifying critical points as maxima or minima.
*   Not considering the second derivative test in conjunction with the first derivative test.

### Quick Summary
-----------------

*   Local maxima/minima are found using the second derivative test and first derivative test.
*   Critical points occur when f'(x) = 0.
*   The function's behavior can be analyzed by examining its derivatives.