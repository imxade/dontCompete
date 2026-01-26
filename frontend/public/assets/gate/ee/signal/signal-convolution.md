**Signal Convolution**
=======================

**Introduction**
---------------

Convolution of signals is a fundamental operation in signal processing, allowing us to combine two or more signals to obtain a new output signal. It's a key concept in understanding how systems process inputs and produce outputs.

**Core Concepts**
-----------------

### What is Convolution?

Convolution of two discrete-time signals $x[n]$ and $y[n]$ is defined as:

$$z[n] = \sum_{k=-\infty}^{\infty} x[k] y[n-k]$$

where $z[n]$ is the output signal.

**Key Formulas/Theorems**
-------------------------

### Convolution Theorem

The convolution theorem states that the Fourier Transform (FT) of the convolution of two signals is equal to the product of their individual FTs:

$$\mathcal{F}\{x[n] \ast y[n]\} = X(e^{j\omega})Y(e^{j\omega})$$

where $X(e^{j\omega})$ and $Y(e^{j\omega})$ are the FTs of $x[n]$ and $y[n]$ respectively.

### Discrete-Time Convolution Property

A key property of discrete-time convolution is that:

$$z[n] = x[n] \ast y[n] = z[n] \ast y[0]$$

**Problem Solving Patterns**
---------------------------

When solving problems involving signal convolution, follow these steps:

1.  Identify the input signals and their properties.
2.  Determine the type of convolution (e.g., discrete-time or continuous-time).
3.  Apply the convolution theorem to find the FT of the output signal.
4.  Use the inverse Fourier Transform (IFT) to obtain the time-domain representation of the output signal.

**Examples with Solutions**
---------------------------

### Example 1

Given:

*   $x[n] = \delta[n-2]$
*   $y[n] = n$

Find the convolution of $x[n]$ and $y[n]$.

**Solution:**

$$z[n] = x[n] \ast y[n] = \sum_{k=-\infty}^{\infty} \delta[k-2] k$$

Using the sifting property of the delta function, we get:

$$z[n] = n$$

However, since $x[n]$ is a delayed impulse, we need to consider the shift in time. Therefore, the correct solution is:

$$z[n] = \begin{cases} 0 & n < 2 \\ n-2 & n \geq 2 \end{cases}$$

### Example 2

Given:

*   $x(t) = e^{-at} u(t)$
*   $y(t) = e^{-bt} u(t)$

Find the convolution of $x(t)$ and $y(t)$.

**Solution:**

Using the convolution theorem, we get:

$$z(t) = \mathcal{F}^{-1}\{X(f)Y(f)\}$$

where:

*   $X(f) = \frac{1}{a + j2\pi f}$
*   $Y(f) = \frac{1}{b + j2\pi f}$

Substituting and simplifying, we get:

$$z(t) = e^{-(a+b)t} u(t)$$

**Common Pitfalls**
------------------

*   Failing to apply the convolution theorem correctly.
*   Not considering time shifts or delays in the input signals.
*   Misinterpreting the properties of the delta function.

**Quick Summary**
-----------------

*   Convolution combines two or more signals to produce a new output signal.
*   The Fourier Transform (FT) of the convolution is equal to the product of individual FTs (convolution theorem).
*   Discrete-time convolution has specific properties, such as the sifting property of the delta function.

This comprehensive study note covers all theoretical concepts and formulas required to solve signal convolution problems. By following the problem-solving patterns and examples provided, students can confidently tackle future questions on this topic.