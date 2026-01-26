**Stability Analysis**
======================

**Introduction**
---------------

Stability analysis is a crucial aspect of discrete-time signal processing, ensuring that a system's output remains within acceptable limits despite changes in its input. This concept is vital for understanding and designing systems that can handle real-world inputs.

**Core Concepts**
-----------------

### Bounded Input Bounded Output (BIBO) Stability

A system is said to be BIBO stable if its output is bounded when the input is bounded. Mathematically, this can be represented as:

$$\sum_{k=0}^{\infty} |h_k| < \infty$$

where $h_k$ represents the impulse response of the system.

### Discrete-Time System Stability

For a discrete-time system to be stable, the following condition must hold:

$$\sum_{n=-\infty}^{\infty} |x[n]| < \infty$$

This means that the sum of the absolute values of the input signal over all time is finite.

**Key Formulas/Theorems**
-------------------------

### BIBO Stability Criterion

A system is BIBO stable if and only if:

$$\sum_{k=0}^{\infty} |h_k| < \infty$$

This criterion provides a necessary and sufficient condition for BIBO stability.

**Problem Solving Patterns**
-----------------------------

1.  **Check for Bounded Input**: Before analyzing the system's output, ensure that the input is bounded.
2.  **Analyze Impulse Response**: Study the impulse response of the system to determine its stability.
3.  **Apply Stability Criterion**: Use the BIBO stability criterion to evaluate the system's stability.

**Examples with Solutions**
---------------------------

### Example 1

Consider a discrete-time system defined by:

$$x[n] = \sum_{k=0}^{n} u[k]$$

where $u[k]$ is the unit step function. Determine if this system is BIBO stable.

Solution:

The impulse response of the system can be found by taking the inverse z-transform of $X(z)$. After some calculations, we find that:

$$h[n] = \sum_{k=0}^{n} u[k] = n + 1$$

Since the sum $\sum_{n=-\infty}^{\infty} |h_n|$ is infinite (because it grows without bound as $n$ increases), this system is not BIBO stable.

### Example 2

Consider a discrete-time system defined by:

$$x[n] = \sum_{k=0}^{N-1} u[k]$$

where $u[k]$ is the unit step function and $N$ is a positive integer. Determine if this system is BIBO stable.

Solution:

The impulse response of the system can be found by taking the inverse z-transform of $X(z)$. After some calculations, we find that:

$$h[n] = \sum_{k=0}^{N-1} u[k] = N$$

Since the sum $\sum_{n=-\infty}^{\infty} |h_n|$ is finite (because it is a constant), this system is BIBO stable.

**Common Pitfalls**
-------------------

*   **Assuming Bounded Input**: Always verify that the input is bounded before analyzing the system's stability.
*   **Not Analyzing Impulse Response**: The impulse response provides crucial information about the system's stability.
*   **Incorrect Application of Stability Criterion**: Be cautious when applying the BIBO stability criterion, as small errors can lead to incorrect conclusions.

**Quick Summary**
------------------

*   BIBO stability requires bounded input and output.
*   The impulse response must be summable for BIBO stability.
*   Always verify bounded input before analyzing system stability.
*   Apply the BIBO stability criterion carefully.