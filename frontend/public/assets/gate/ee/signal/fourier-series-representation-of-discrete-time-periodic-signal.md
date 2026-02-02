# Fourier Series Representation of Discrete Time Periodic Signals
===========================================================

## Introduction
---------------

Fourier series representation is a powerful tool for analyzing discrete-time periodic signals. It decomposes the signal into its constituent frequencies, allowing us to understand the signal's behavior and properties in the frequency domain.

## Core Concepts
-----------------

A discrete-time periodic signal is a sequence of values that repeats itself after a certain number of samples. The period of the signal is the number of samples between two consecutive repetitions.

### Periodic Signals

*   A signal `x[n]` is said to be periodic with period `N` if:
    $$
    x[n+N] = x[n]
    $$

### Fourier Series Representation

The Fourier series representation of a discrete-time periodic signal `x[n]` is given by:

$$
x[n] = \sum_{k=0}^{N-1} c_k e^{j\frac{2\pi kn}{N}}
$$

where $c_k$ are the complex coefficients, and $e^{j\theta}$ represents a complex exponential.

## Key Formulas/Theorems
-------------------------

### Fourier Series Coefficients

The complex coefficients $c_k$ can be calculated using the following formula:

$$
c_k = \frac{1}{N} \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi kn}{N}}
$$

### Z-transform and Fourier Series

If we have the Z-transform of a discrete-time signal `x[n]` as $X(z)$, then we can find its Fourier series representation by setting $z = e^{j\omega}$.

## Problem Solving Patterns
---------------------------

*   When given a periodic signal in the time domain, express it as a sum of complex exponentials using the Fourier series representation.
*   Use the Z-transform to find the Fourier series coefficients if the signal's Z-transform is given.

## Examples with Solutions
-----------------------------

### Example 1

Suppose we have a periodic signal `x[n]` with period `N=4`, and its Z-transform is $X(z) = \frac{z}{(z-\alpha)(z-\beta)}$. Find the Fourier series representation of `x[n]`.

*   Step 1: Set up the expression for $c_k$.
    $$
    c_k = \frac{1}{N} \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi kn}{N}}
    $$

*   Step 2: Substitute $X(z)$ and simplify.

### Example 2

If the Z-transform of a finite-duration discrete-time signal `x[n]` is $X(z)$, then find the Z-transform of the signal $y[n] = x[2n]$.

## Common Pitfalls
-------------------

*   Students often confuse the period with the sampling rate.
*   Inverse Z-transform can be tricky; ensure you understand the process and apply it correctly.

## Quick Summary
---------------

### Key Points

*   Periodic signals can be represented as a sum of complex exponentials using the Fourier series representation.
*   The complex coefficients $c_k$ can be calculated using the formula provided.
*   Use the Z-transform to find the Fourier series coefficients if given the signal's Z-transform.

### Relevant Concepts and Formulas

*   Periodic signals
*   Fourier series representation
*   Complex exponentials
*   Z-transform
*   Inverse Z-transform