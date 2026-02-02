# Discrete Time Fourier Series (DTFS)
======================================

## Introduction
---------------

The Discrete Time Fourier Series (DTFS) represents a discrete-time periodic signal as an infinite sum of complex exponentials. It's essential for analyzing and synthesizing periodic signals in discrete-time systems.

## Core Concepts
-----------------

### Periodic Signals

A discrete-time signal $x[n]$ is said to be periodic with period $N$ if it satisfies the condition:

$$x[n] = x[n+N], \quad \forall n \in \mathbb{Z}.$$

The fundamental period of a signal is the smallest positive integer $N$ for which this equation holds.

### Discrete-Time Fourier Series

Given a discrete-time periodic signal $x[n]$ with period $N$, the DTFS representation is:

$$X(k) = \frac{1}{N} \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}kn}, \quad k \in \mathbb{Z}.$$

The coefficients $X(k)$ are the DTFS coefficients, and the complex exponential terms $e^{-j\frac{2\pi}{N}kn}$ form an orthonormal basis for the space of discrete-time periodic signals.

## Key Formulas/Theorems
-------------------------

### Inverse DTFS

Given the DTFS coefficients $X(k)$, we can reconstruct the original signal $x[n]$ as:

$$x[n] = \sum_{k=0}^{N-1} X(k) e^{-j\frac{2\pi}{N}kn}, \quad n \in \mathbb{Z}.$$

### Parseval's Theorem

For a discrete-time periodic signal $x[n]$ with period $N$, the energy of the signal is given by:

$$E_x = \sum_{n=0}^{N-1} |x[n]|^2 = N \sum_{k=0}^{N-1} |X(k)|^2.$$

## Problem Solving Patterns
---------------------------

### Example 1

Suppose we have a discrete-time periodic signal $x[n]$ with period $3$ and DTFS coefficients:

$$a_0 = 2, \quad a_1 = -1 + j\frac{\sqrt{3}}{2}, \quad a_2 = -1 - j\frac{\sqrt{3}}{2}.$$

Using the Inverse DTFS formula, we can reconstruct the original signal $x[n]$ as:

$$x[n] = 2e^{j0n} + (-1 + j\frac{\sqrt{3}}{2}) e^{-j\frac{2\pi}{3}n} + (-1 - j\frac{\sqrt{3}}{2}) e^{j\frac{2\pi}{3}n}, \quad n \in \mathbb{Z}.$$

### Example 2

Suppose we have a discrete-time periodic signal $x[n]$ with period $N$ and DTFS coefficients:

$$X(k) = A_k e^{j\theta_k}, \quad k = 0, 1, ..., N-1.$$

Using Parseval's Theorem, we can calculate the energy of the signal as:

$$E_x = N \sum_{k=0}^{N-1} |A_k|^2 = N \sum_{k=0}^{N-1} |X(k)|^2.$$

## Common Pitfalls
------------------

*   Confusing DTFS with Discrete-Time Fourier Transform (DTFT).
*   Not properly handling periodicity in the signal.
*   Overlooking the importance of Parseval's Theorem.

## Quick Summary
-----------------

*   Periodic signals and their representation using DTFS.
*   Inverse DTFS formula for reconstructing original signals.
*   Parseval's Theorem for calculating energy of discrete-time periodic signals.

**Note:** This is a high-yield theory note that covers the essential concepts, formulas, and insights required to solve DTFS-related questions. Make sure to practice problems from past exams to reinforce your understanding.