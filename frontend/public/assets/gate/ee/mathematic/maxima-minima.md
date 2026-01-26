**Maxima Minima**
================

### Introduction

Maxima and minima are critical concepts in mathematical optimization, which deals with finding the maximum or minimum of a function. In this note, we'll focus on maxima minima, covering essential principles, laws, formulas, and problem-solving techniques to tackle questions like GATE CS exam problems.

### Core Concepts

#### Definition of Maxima Minima

*   **Local Maximum**: A point $t$ is called a local maximum if there exists an interval $(a,b)$ containing $t$, such that for all $x\in (a,b)$, $f(t)\geq f(x)$.
*   **Local Minimum**: A point $t$ is called a local minimum if there exists an interval $(a,b)$ containing $t$, such that for all $x\in (a,b)$, $f(t)\leq f(x)$.

#### Conditions for Maxima Minima

A function $f$ has a maximum or minimum at a point $c$ if and only if the derivative of $f$ at $c$ is zero. In other words:

$$
\begin{aligned}
&amp; \text{If } f'(c) = 0, \text{ then } c \text{ is a critical point.} \\
&amp; \text{If } f''(c) > 0, \text{ then } c \text{ is a local minimum.} \\
&amp; \text{If } f''(c) < 0, \text{ then } c \text{ is a local maximum.}
\end{aligned}
$$

### Key Formulas/Theorems

*   The second derivative test:
    $$
    \begin{aligned}
    &amp;\text{ If } f''(x) > 0, \text{ then } x \text{ is a local minimum.} \\
    &amp;\text{ If } f''(x) < 0, \text{ then } x \text{ is a local maximum.}
    \end{aligned}
    $$
*   The sufficient condition for a function to have a local maximum or minimum at a point $c$ is that its derivative at $c$ should be zero and the second derivative at $c$ should not be zero.

### Problem Solving Patterns

1.  **First Derivative Test**: If $f'(x) = 0$, then $x$ is a critical point.
2.  **Second Derivative Test**: If $f''(x) > 0$, then $x$ is a local minimum; if $f''(x) < 0$, then $x$ is a local maximum.

### Examples with Solutions

Example 1:
Given $f(x)=3x^4-7x^2+5$, find the local maxima or minima.

Solution: To find critical points, we set $f'(x)=0$. In this case:

$$
\begin{aligned}
12x^3 -14x &= 0 \\
x(12x^2 -14) &= 0 \\
x &= 0 \text{ or } x^2 = \frac{14}{12} \\
x &= 0, \sqrt{\frac{7}{6}}, -\sqrt{\frac{7}{6}}
\end{aligned}
$$

We evaluate $f''(x)$ at these points to determine the nature of the critical points:

$$
\begin{aligned}
&amp; f''(0) = -14 < 0 \Rightarrow x=0 \text{ is a local maximum} \\
&amp; f''(\sqrt{\frac{7}{6}}) = 24\sqrt{\frac{7}{6}} > 0 \Rightarrow x=\sqrt{\frac{7}{6}} \text{ is a local minimum} \\
&amp; f''(-\sqrt{\frac{7}{6}}) = -24\sqrt{\frac{7}{6}} < 0 \Rightarrow x=-\sqrt{\frac{7}{6}} \text{ is a local maximum}
\end{aligned}
$$

### Common Pitfalls

1.  **Failing to evaluate the second derivative**: Always ensure that you have evaluated both $f'(x)$ and $f''(x)$ for each critical point.
2.  **Misinterpreting the results of the second derivative test**:

The second derivative is greater than zero (i.e., $f''(c) > 0$), it does not necessarily mean that there will be a minimum value.

If the second derivative at a critical point is positive, then we have found a local minima. However, the absolute minimum may still be somewhere else in the function’s domain.



### Quick Summary

*   **Maxima Minima Conditions**:
    *   To determine maxima or minima for $f$, find critical points using $f'(x)=0$.
    *   Apply second derivative test: if $f''(c) > 0$, then $c$ is a local minimum; if $f''(c) < 0$, then $c$ is a local maximum.

**Revision Tips**

1.  Practice finding maxima and minima for various functions.
2.  Be meticulous in evaluating both the first and second derivatives of the function at each critical point.
3.  Use these concepts to solve problems from past year papers, such as the one mentioned above (GATE CS exam paper).