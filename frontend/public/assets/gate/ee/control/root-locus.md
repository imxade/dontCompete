**Root Locus**
================

### Introduction
----------------

The root locus is a graphical representation of the roots of a closed-loop system as a parameter, typically the gain (K), varies. It is an essential tool for analyzing and designing control systems.

### Core Concepts
-----------------

*   **Closed-Loop System**: A system with feedback, where the output is used to adjust the input.
*   **Roots**: The values of s that make the characteristic equation equal to zero.
*   **Gain (K)**: A parameter that scales the forward path transfer function.

### Key Formulas/Theorems
-------------------------

The root locus can be determined using the following equations:

$$\frac{s + p_1}{s + \sigma} = -\frac{p_0 + q_0s}{q_1 + q_2s}$$

where:
*   $p_1$ and $\sigma$ are real poles
*   $p_0$, $q_0$, $q_1$, and $q_2$ are coefficients of the characteristic equation

The angle of departure from a pole is given by:

$$\theta = \frac{180^\circ}{N + 1} (M - N)$$

where:
*   $\theta$ is the angle of departure
*   $N$ is the number of poles on the real axis to the left of the complex pole
*   $M$ is the total number of poles

### Problem Solving Patterns
---------------------------

1.  **Identify Poles and Zeros**: Count the number of poles and zeros in the system.
2.  **Draw the Root Locus**: Start with a real axis and draw a line at an angle $\theta$ for each pole, as described above.
3.  **Determine Breakaway Points**: Find where the root locus branches away from a pole.

### Examples with Solutions
---------------------------

**Example 1**

Consider the system with the transfer function:

$$G(s) = \frac{1}{s + 2}$$

The closed-loop characteristic equation is:

$$1 + G(s)H(s) = s^2 + (3 + K)s + 2K = 0$$

To find the breakaway point, set the derivative of the characteristic equation equal to zero:

$$(3 + K)(s + 2) - (s^2 + (3 + K)s + 2K) = 0$$

Solving for s gives us the breakaway point.

**Solution**

The breakaway point is at $s = -1$.

### Common Pitfalls
------------------

*   **Ignoring complex poles**: Remember to consider all poles, including complex ones.
*   **Incorrect counting of poles and zeros**: Double-check your counts to ensure accuracy.

### Quick Summary
----------------

*   Root locus is a graphical representation of the roots of a closed-loop system as a parameter (K) varies.
*   Key formulas include the characteristic equation and the angle of departure from a pole.
*   Breakaway points occur when the root locus branches away from a pole.

**Mermaid Diagram**
```mermaid
graph LR
    A[Start] --> B[Identify Poles and Zeros]
    B --> C[Draw the Root Locus]
    C --> D[Determine Breakaway Points]
```

Note: Please ensure that any external images or URLs are stable and accurate.

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve root locus problems.