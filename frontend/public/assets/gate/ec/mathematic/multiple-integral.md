**Multiple Integral Theory Note**
=====================================

### Introduction
-----------------

A multiple integral is a mathematical operation used to find the volume under a surface or between two surfaces in n-dimensional space. In this note, we'll focus on double integrals and cover essential concepts, formulas, and problem-solving patterns required for the GATE CS exam.

### Core Concepts
-----------------

*   **Double Integral**: A double integral is an integral of the form $\iint_{D} f(x,y) \,dxdy$, where $D$ is a region in two-dimensional space.
*   **Region of Integration**: The region $D$ can be defined explicitly or implicitly and may have various shapes and boundaries.

### Key Formulas/Theorems
-------------------------

$$\iint_{D} f(x,y) \,dxdy = \int_{x=a}^{x=b} \left( \int_{y=g_1(x)}^{g_2(x)} f(x,y) \,dy \right) dx$$

or equivalently,

$$\iint_{D} f(x,y) \,dxdy = \int_{y=c}^{y=d} \left( \int_{x=h_1(y)}^{h_2(y)} f(x,y) \,dx \right) dy$$

where $g_1(x)$, $g_2(x)$, $h_1(y)$, and $h_2(y)$ are the limits of integration.

### Problem Solving Patterns
---------------------------

*   **Breaking Down Complex Regions**: Divide complex regions into simpler sub-regions to evaluate the double integral.
*   **Changing Order of Integration**: Swap the order of integration if possible, especially when dealing with rectangular or triangular regions.

### Examples with Solutions
-----------------------------

**Example 1:**

Find $\iint_{D} (x^2 + y) \,dxdy$, where $D$ is the region bounded by $x=0$, $y=0$, and $y=x^2$.

Solution:
To evaluate this integral, we'll change the order of integration:

$$\iint_{D} (x^2 + y) \,dxdy = \int_{0}^{1} \left( \int_{0}^{x^2} (x^2 + y) \,dy \right) dx$$

Evaluate the inner integral first:
$$\int_{0}^{x^2} (x^2 + y) \,dy = x^4 + \frac{x^6}{3}$$
Now integrate with respect to $x$:

$$\iint_{D} (x^2 + y) \,dxdy = \int_{0}^{1} \left( x^4 + \frac{x^6}{3} \right) dx$$

Perform the integration:
$$= \left[ \frac{x^5}{5} + \frac{x^7}{21} \right]_0^1 = \frac{1}{5} + \frac{1}{21} = \frac{46}{105}$$

### Common Pitfalls
---------------------

*   **Incorrect Order of Integration**: Be careful when changing the order of integration, as it may lead to incorrect results.
*   **Missing Limits of Integration**: Always include the limits of integration for each variable.

### Quick Summary
------------------

| Concept | Description |
| --- | --- |
| Double Integral | A mathematical operation used to find volume under a surface or between two surfaces in 2D space. |
| Region of Integration | The region $D$ can be defined explicitly or implicitly and may have various shapes and boundaries. |
| Key Formulas/Theorems | $\iint_{D} f(x,y) \,dxdy = \int_{x=a}^{x=b} \left( \int_{y=g_1(x)}^{g_2(x)} f(x,y) \,dy \right) dx$ or $\iint_{D} f(x,y) \,dxdy = \int_{y=c}^{y=d} \left( \int_{x=h_1(y)}^{h_2(y)} f(x,y) \,dx \right) dy$ |
| Problem Solving Patterns | Breaking down complex regions into simpler sub-regions and changing the order of integration. |

Note: This theory note is a starting point for studying multiple integrals. It's essential to practice solving problems from previous years' questions and other resources to become proficient in this topic.