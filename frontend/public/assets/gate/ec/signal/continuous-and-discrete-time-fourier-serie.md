**Continuous and Discrete Time Fourier Series**
=============================================

**Introduction**
---------------

The Fourier series is a mathematical tool for representing periodic signals as a sum of sinusoids. In this note, we'll focus on both continuous time (CTFS) and discrete time (DTFS) Fourier series.

**Core Concepts**
-----------------

### Periodic Signals

A signal $x(n)$ is said to be periodic with period $N$ if:

$$x(n+N) = x(n) \quad \forall n$$

### Discrete Time Fourier Series (DTFS)

The DTFS of a discrete time periodic signal $x(n)$ with period $N$ can be represented as:

$$X[k] = \frac{1}{N} \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}nk}$$

where $k = 0, 1, 2, ..., N-1$.

**Key Formulas/Theorems**
-------------------------

### Inverse DTFS

The inverse DTFS can be obtained by:

$$x(n) = \sum_{k=0}^{N-1} X[k] e^{-j\frac{2\pi}{N}nk}$$

### Parseval's Theorem (DTFS)

Parseval's theorem states that the energy of a discrete time periodic signal is equal to the sum of the squared magnitudes of its DTFS coefficients:

$$\sum_{n=0}^{N-1} |x[n]|^2 = \frac{1}{N} \sum_{k=0}^{N-1} |X[k]|^2$$

### Relationship between CTFS and DTFS

For a discrete time periodic signal, the CTFS can be obtained by taking the limit of the DTFS as $N$ approaches infinity:

$$F(e^{j\omega}) = \lim_{N \to \infty} X[k]$$

where $\omega = \frac{2\pi}{N}$.

**Problem Solving Patterns**
---------------------------

### Finding the Sum of a Discrete Time Fourier Series

Given the DTFS coefficients, we can find the sum of the series by applying Parseval's theorem:

$$x(n) = \sum_{k=0}^{N-1} X[k] e^{-j\frac{2\pi}{N}nk}$$

**Examples with Solutions**
---------------------------

### Example 1: Discrete Time Fourier Series Coefficients

Given the DTFS coefficients $X[k]$ for a periodic signal with period $N=5$:

$$X[0] = \frac{1}{5}, X[1] = -\frac{3}{5} e^{-j\frac{2\pi}{5}}, X[2] = \frac{2}{5}$$

Find the value of the sum at $n=4$.

Solution:

$$x(4) = \sum_{k=0}^{4} X[k] e^{-j\frac{2\pi}{5}4k}$$
$$= \frac{1}{5} + (-\frac{3}{5})e^{-j\frac{8\pi}{5}} + \frac{2}{5}$$

Simplifying, we get:

$$x(4) = -10$$

### Example 2: Relationship between CTFS and DTFS

Given the DTFS coefficients $X[k]$ for a periodic signal with period $N=5$:

$$X[0] = \frac{1}{5}, X[1] = e^{-j\frac{\pi}{5}}, X[2] = -e^{j\frac{\pi}{10}}$$

Find the CTFS of the signal.

Solution:

Since $\lim_{N \to \infty} X[k] = F(e^{j\omega})$, we can take the limit as $N$ approaches infinity:

$$F(e^{j\omega}) = \lim_{N \to \infty} X[k]$$
$$= \frac{1}{5}, e^{-j\frac{\pi}{5}}, -e^{j\frac{\pi}{10}}$$

**Common Pitfalls**
-------------------

### Failure to Consider the Period of the Signal

When working with discrete time signals, it's essential to keep track of the period $N$.

### Inconsistent Application of Parseval's Theorem

Parseval's theorem should be applied consistently for both DTFS and CTFS.

**Quick Summary**
-----------------

* Periodic signals can be represented using DTFS or CTFS.
* DTFS: $X[k] = \frac{1}{N} \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}nk}$.
* Parseval's theorem relates the energy of a signal to its DTFS coefficients.
* Relationship between CTFS and DTFS: $\lim_{N \to \infty} X[k] = F(e^{j\omega})$.