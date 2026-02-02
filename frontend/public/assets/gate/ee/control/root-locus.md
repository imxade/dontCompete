**Root Locus**
================

### Introduction
-----------------

The root locus is a graphical representation of the roots of the characteristic equation of a closed-loop system as a parameter (usually gain) varies. It provides valuable information about the stability and performance of the system.

### Core Concepts
-------------------

#### Definition
A root locus is a plot of the roots of the closed-loop transfer function as a parameter (gain, $K$) varies from 0 to infinity.

#### Properties

*   The number of branches in a root locus is equal to the number of poles of the open-loop transfer function.
*   The root locus starts at the poles of the open-loop transfer function and ends at the zeros of the open-loop transfer function.
*   The angle of departure from a pole is determined by the coefficient of the second highest power of $s$ in the numerator.

### Key Formulas/Theorems
---------------------------

$$\frac{d \sigma}{d K} = \frac{\sum R_i}{\prod (1 + \beta_{ji})}$$

where $\sigma$ is the real part of the root, and $R_i$ are the real parts of the poles.

### Problem Solving Patterns
---------------------------

#### Finding Angle of Departure

To find the angle of departure at a pole, use the following formula:

$$\theta = \frac{\pi}{n} + \frac{(\sigma_r - \sigma_p)}{\sqrt{(1 + k^2)}} \times 180^\circ $$

where $\theta$ is the angle of departure, $n$ is the number of poles at the same location, $\sigma_r$ and $\sigma_p$ are the real parts of the zero and pole, respectively, and $k$ is the coefficient of the second highest power of $s$ in the numerator.

### Examples with Solutions
-----------------------------

**Example 1:**

Consider the closed-loop system shown in the figure below:

![Closed-Loop System](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Control_system.svg/1200px-Control_system.svg.png)

where $G(s) = \frac{2}{s^2 + 5}$ and $K$ is the gain.

Find the angle of departure at the pole $s = -j\sqrt{5}$ for $0 < K < \infty$.

**Solution:**

Using the formula above, we get:

$$\theta = \frac{\pi}{1} + \frac{(0 - (-\sqrt{5}))}{\sqrt{(1 + 4)}} \times 180^\circ $$

Simplifying, we get:

$$\theta = 180^\circ + \frac{\sqrt{5}}{\sqrt{5}} \times 180^\circ = 180^\circ + 36.87^\circ = 216.87^\circ$$

Rounding off to the nearest integer, we get $\boxed{217}$.

### Common Pitfalls
-------------------

*   Students often forget to consider the coefficient of the second highest power of $s$ in the numerator when finding the angle of departure.
*   They may also confuse the real and imaginary parts of the poles and zeros.

### Quick Summary
-----------------

*   The root locus is a graphical representation of the roots of the characteristic equation as the gain varies from 0 to infinity.
*   It has properties such as:
    *   Number of branches equal to number of poles.
    *   Starts at poles, ends at zeros.
    *   Angle of departure determined by coefficient of second highest power of $s$ in numerator.
*   Key formulas include:
    + Formula for $\frac{d \sigma}{d K}$
    + Formula for finding angle of departure.

Note: The source question is Q1 (ID: ee_2024_57). This theory note covers the concepts and techniques required to solve this and similar questions.