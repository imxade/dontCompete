**Discrete Time Fourier Series Representation**
=====================================================

### Introduction
-----------------

The Discrete-Time Fourier Series (DTFS) representation of a signal is an extension of the Continuous-Time Fourier Series. It allows us to represent periodic discrete-time signals using their frequency components.

### Core Concepts
------------------

A discrete-time periodic signal $x[n]$ with period $N$ can be represented as:

$$
\begin{aligned}
x[n] &= \sum_{k=0}^{N-1} a_k e^{\frac{j2\pi kn}{N}} \\
&= a_0 + a_1e^{\frac{j2\pi n}{N}} + a_2e^{\frac{j4\pi n}{N}} + \ldots + a_{N-1}e^{\frac{j(N-1)2\pi n}{N}}
\end{aligned}
$$

where $a_k$ are the Fourier coefficients.

### Key Formulas/Theorems
---------------------------

*   The DTFS representation of a discrete-time periodic signal is given by:

$$
x[n] = \sum_{k=0}^{N-1} a_k e^{\frac{j2\pi kn}{N}}
$$

*   The Fourier coefficients $a_k$ are given by the summation of the product of the signal and the complex exponential terms:

$$
a_k = \frac{1}{N} \sum_{n=0}^{N-1} x[n] e^{-\frac{j2\pi kn}{N}}
$$

### Problem Solving Patterns
-----------------------------

*   To find the DTFS representation of a given signal, first identify the period $N$ and the non-zero Fourier coefficients.
*   Use the formula for $a_k$ to calculate the values of the Fourier coefficients.

### Examples with Solutions
---------------------------

**Example 1**

Given:

$$
\begin{aligned}
x[n] &= \pi^{-1} jn e^n \\
&= 0.5jne^ne^{-j2\pi n/3} + 0.2e^{j4\pi n/3} + 0.1e^{-j6\pi n/3}
\end{aligned}
$$

Find the DTFS representation of $x[n]$.

**Solution**

Identify the period $N = 3$ and non-zero Fourier coefficients:

$a_2 = \frac{j}{2}$, $a_4 = 0.2$, $a_6 = 0.1$

Use the formula for $a_k$ to calculate the values of the Fourier coefficients.

The DTFS representation is given by:

$$
\begin{aligned}
x[n] &= a_0 + a_2e^{\frac{j4\pi n}{3}} + a_4e^{j8\pi n/3} \\
&= 1.5je^{\frac{j4\pi n}{3}}
\end{aligned}
$$

### Common Pitfalls
---------------------

*   Failing to identify the correct period $N$ and non-zero Fourier coefficients.
*   Incorrectly calculating the values of the Fourier coefficients.

### Quick Summary
------------------

*   The DTFS representation is an extension of the CTFS for discrete-time periodic signals.
*   A signal can be represented as a sum of complex exponential terms with frequencies that are integer multiples of the fundamental frequency $\frac{2\pi}{N}$.

This completes the comprehensive theory note on Discrete Time Fourier Series Representation.