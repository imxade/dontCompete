Fourier Series
===============

Introduction
------------

The Fourier series is a mathematical tool used to represent periodic functions as an infinite sum of sinusoidal components. This technique has numerous applications in signal processing, data analysis, and many other fields.

Core Concepts
-------------

*   **Periodic Functions**: A function $f(t)$ is said to be periodic if there exists a constant $T$ such that $f(t+T) = f(t)$ for all $t$. The smallest such value of $T$ is called the period of the function.
*   **Fourier Series Representation**: Any periodic function can be represented as an infinite sum of sinusoidal components, given by the equation:

$$
\begin{aligned}
f(t) &= \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos(nt) + b_n \sin(nt))
\end{aligned}
$$

where $a_n$ and $b_n$ are the Fourier coefficients.

Key Formulas/Theorems
----------------------

### Fourier Coefficients

The Fourier coefficients can be calculated using the following formulas:

*   **Average Value**: The average value of a function over one period is given by:

$$
\begin{aligned}
a_0 &= \frac{1}{T} \int_{-T/2}^{T/2} f(t) dt
\end{aligned}
$$

*   **Co-sinusoidal Components**: The co-sinusoidal components are given by:

$$
\begin{aligned}
a_n &= \frac{1}{T} \int_{-T/2}^{T/2} f(t) \cos(nt) dt
\end{aligned}
$$

*   **Sine Components**: The sine components are given by:

$$
\begin{aligned}
b_n &= \frac{1}{T} \int_{-T/2}^{T/2} f(t) \sin(nt) dt
\end{aligned}
$$

Problem Solving Patterns
-------------------------

### Problem 1: Finding Fourier Coefficients

To find the Fourier coefficients, use the formulas provided above. Make sure to substitute $f(t)$ with the given function and calculate the integrals.

Examples with Solutions
-----------------------

**Example 1**

Find the Fourier series representation of the function:

$$
\begin{aligned}
f(t) &= \left\{
\begin{array}{ll}
t &amp; \mbox{for } -\pi < t < \pi \\
-t &amp; \mbox{for } \pi < t < 2\pi \\
\end{array}
\right.
\end{aligned}
$$

### Solution

To find the Fourier series representation, we need to calculate the Fourier coefficients. We first calculate the average value:

```latex
a_0 = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) dt
= \frac{1}{2\pi} \left( \int_{-\pi}^{0} t dt + \int_{0}^{\pi} -t dt \right)
= 0
```

Next, we calculate the co-sinusoidal components:

```latex
a_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) \cos(nt) dt
= \frac{1}{2\pi} \left( \int_{-\pi}^{0} t \cos(nt) dt + \int_{0}^{\pi} -t \cos(nt) dt \right)
```

Integrating by parts, we get:

```latex
a_n = \frac{1}{2\pi} \left[ \frac{-t \sin(nt)}{n} + \frac{\cos(nt)}{n^2} - (-1)^n \left( \frac{\sin(nt)}{n} - \frac{\cos(nt)}{n^2} \right) \right]_{-\pi}^{0}
```

Evaluating the limits, we get:

```latex
a_n = \frac{-(-1)^n}{\pi n^2} \left( 1 - (-1)^n \right)
= \left\{
\begin{array}{ll}
0 &amp; \mbox{for even } n \\
-\frac{2}{\pi n^2} &amp; \mbox{for odd } n
\end{array}
\right.
```

Similarly, we calculate the sine components:

```latex
b_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) \sin(nt) dt
= \frac{1}{2\pi} \left( \int_{-\pi}^{0} t \sin(nt) dt + \int_{0}^{\pi} -t \sin(nt) dt \right)
```

Integrating by parts, we get:

```latex
b_n = \frac{1}{2\pi} \left[ \frac{-t \cos(nt)}{n} + \frac{\sin(nt)}{n^2} - (-1)^n \left( -\frac{t \cos(nt)}{n} + \frac{\sin(nt)}{n^2} \right) \right]_{-\pi}^{0}
```

Evaluating the limits, we get:

```latex
b_n = \left\{
\begin{array}{ll}
1 &amp; \mbox{for } n=1 \\
-1 &amp; \mbox{for } n=-1 \\
0 &amp; \mbox{otherwise}
\end{array}
\right.
```

Therefore, the Fourier series representation of the function is:

$$
\begin{aligned}
f(t) &= \sum_{n=1}^{\infty} \left( -\frac{2}{\pi n^2} \cos(nt) + \sin(nt) \right)
\end{aligned}
$$

Common Pitfalls
-----------------

*   Make sure to calculate the Fourier coefficients correctly.
*   Use the correct formulas for calculating co-sinusoidal and sine components.
*   Be careful when evaluating limits in the calculations.

Quick Summary
--------------

*   Periodic functions can be represented as an infinite sum of sinusoidal components using the Fourier series.
*   The Fourier coefficients can be calculated using the formulas provided above.
*   Use the correct formulas to calculate co-sinusoidal and sine components.
*   Be careful when evaluating limits in the calculations.

```mermaid
graph LR
A[Periodic Function] --> B[Fourier Series Representation]
B --> C[Fourier Coefficients]
C --> D[Co-sinusoidal Components]
D --> E[Sine Components]
E --> F[Evaluate Limits]
F --> G[Final Answer]
