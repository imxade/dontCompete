**Complex Variables**
======================

### Introduction
-----------------

Complex variables are a fundamental tool for solving problems in various fields, including electrical engineering, control systems, and signal processing. In this note, we will cover the basics of complex variables and their applications.

### Core Concepts
------------------

*   **Definition**: A complex number is defined as $z = x + jy$, where $x$ and $y$ are real numbers, and $j$ is the imaginary unit satisfying $j^2 = -1$. The complex conjugate of a complex number $z$ is denoted by $\overline{z}$.

*   **Polar Form**: A complex number can be expressed in polar form as $z = re^{j\theta}$, where $r$ is the magnitude and $\theta$ is the argument.

### Key Formulas/Theorems
-------------------------

*   **Magnitude**: The magnitude of a complex number $z = x + jy$ is given by $|z| = \sqrt{x^2 + y^2}$. The magnitude of a polar form representation is simply the radius, $r$.
    $$\begin{aligned}
    |z| &= \sqrt{x^2 + y^2} \\
    r &= \sqrt{x^2 + y^2}
    \end{aligned}$$
*   **Argument**: The argument of a complex number $z = x + jy$ is given by $\theta = \tan^{-1}\left(\frac{y}{x}\right)$. The argument of a polar form representation is the angle, $\theta$.
    $$\begin{aligned}
    \theta &= \tan^{-1}\left(\frac{y}{x}\right) \\
    \theta &= \text{angle in polar form}
    \end{aligned}$$

### Problem Solving Patterns
---------------------------

*   **Inverse Function Mapping**: Given the function $f(z) = z^{-1}$, where $z$ is a complex number, this maps the unit circle centered at the origin to itself.
    $$\begin{aligned}
    f(z) &= \frac{1}{z} \\
    &={}\frac{1}{x + jy} \\
    &={}\frac{x - jy}{(x)^2 + (y)^2} \\
    &={}(x)^2 + (y)^2\\
    &={}\text{Inverse function maps the unit circle to itself.}
    \end{aligned}$$

### Examples with Solutions
-------------------------

*   **Q1**: The inverse function $f^{-1}(z) = z^{-1}$, where $z$ is a complex number, maps the real axis to which of the following? (From source question in_2023_39)
    $$\begin{aligned}
    f(z)&=\frac{1}{z}\\
    &={}\frac{1}{x+jy} \\
    \end{aligned}$$

**Solution**

When $y = 0$, the function becomes $f(x) = \frac{1}{x}$, which is a real number.

Therefore, the inverse function maps the real axis to the unit circle with its center at the origin. The correct answer is (A).

*   **Q2**: Let $f(z) = z^6 + 9z^2$ defined in the complex plane. This integral $\int f(z)\ dz$ over the contour of a circle $c$ with center at the origin and unit radius is _______.

**Solution**

Since the function $f(z)$ has no singularities inside the contour, the value of the integral is zero by Cauchy's theorem.

Therefore, the correct answer is (A) 0.

### Common Pitfalls
--------------------

*   Make sure to check if there are any singularities or discontinuities in the function within the given region.
*   Be careful when using theorems like Cauchy's theorem. Always ensure that all conditions for its application are met.

### Quick Summary
-----------------

*   A complex number is defined as $z = x + jy$, where $x$ and $y$ are real numbers, and $j$ is the imaginary unit.
*   The magnitude of a complex number is given by $|z| = \sqrt{x^2 + y^2}$.
*   The argument of a complex number is given by $\theta = \tan^{-1}\left(\frac{y}{x}\right)$.
*   Cauchy's theorem states that the integral of an analytic function over a closed contour is zero if all singularities are outside the contour.