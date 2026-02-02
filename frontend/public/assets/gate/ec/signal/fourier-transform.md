**Fourier Transform**
=======================

### Introduction
The Fourier Transform (FT) is a mathematical tool used to decompose a function or sequence into its constituent frequencies. In the context of Signals, it's essential for understanding how a signal can be represented in both time and frequency domains.

### Core Concepts

#### Discrete-Time Fourier Transform (DTFT)
Given a discrete-time signal $x[n]$, the DTFT is defined as:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}$$

The DTFT represents the signal in the frequency domain, with $\omega$ being the angular frequency.

#### Properties of DTFT
- Linearity: $aX(e^{j\omega}) + bY(e^{j\omega}) \leftrightarrow (aX[n] + bY[n])$
- Time-Shifting: $x[n-k] \leftrightarrow e^{-j\omega k} X(e^{j\omega})$
- Conjugation: $x^*[n] \leftrightarrow X^*(e^{j\omega})$

### Key Formulas/Theorems

*   **Convolution Property**:
    $$(F \ast G)[n] \leftrightarrow (2\pi F)X(e^{j\omega})(2\pi G)(e^{j\omega})$$
*   **Multiplication Property**:
    $$x[n]y[n] \leftrightarrow \frac{1}{2\pi} X(e^{j\omega})Y(e^{j\omega})$$

### Problem Solving Patterns

#### 1. DTFT Computation

When computing the DTFT of a given sequence, use the definition and Euler's formula: $e^{j\theta} = \cos{\theta} + j\sin{\theta}$.

**Example:** Find the DTFT of $\{x[n]\} = \{2, 3, 4\}$.
$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}
= 2 + 3e^{-j\omega} + 4e^{-j2\omega}.
$$

#### 2. Parseval's Theorem
Parseval's theorem relates the energy of a signal in both time and frequency domains.
$$
\sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega.
$$

### Examples with Solutions

**Q1:** Consider the signal $x[n] = u[n]$ and $y[n] = 2u[n-1] - u[n-2]$.

Find $\frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega}) + Y(e^{j\omega})|^2 d\omega$.

**Solution:** First, we compute $X(e^{j\omega}) = \sum_{n=0}^{\infty} e^{-j\omega n}$ and $Y(e^{j\omega}) = 2e^{-j\omega}\sum_{n=1}^{\infty} e^{-j\omega(n-1)} - \sum_{n=2}^{\infty} e^{-j\omega (n-2)}$.

Evaluating the integrals, we get:

$$
|X(e^{j\omega})|^2 = \left(\frac{1-e^{-j\omega}}{1-e^{-j\omega}}\right) \left(\frac{e^{-j\omega} - e^{-j2\omega}}{(1 - e^{-j\omega})(1 - e^{-j2\omega})}\right).
$$

Simplifying, we get:
$$
|X(e^{j\omega})|^2 = 4\left|\frac{e^{-j\omega}-e^{-j2\omega}}{(1-e^{-j\omega})(1-e^{-j2\omega})}\right|
= \frac{4}{(1 + e^{\omega})(1+ e^{-2\omega})}.
$$

After some algebraic manipulations, we arrive at:

$\frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega = 8$.

### Common Pitfalls
- Confusing $\omega$ with $e^{j\omega}$.
- Forgetting that Parseval's theorem relates the energy of a signal in both time and frequency domains.

### Quick Summary

*   **DTFT**: Decomposes a discrete-time signal into its constituent frequencies.
*   **Properties**: Linearity, Time-Shifting, Conjugation.
*   **Convolution Property**: $(F \ast G)[n] \leftrightarrow (2\pi F)X(e^{j\omega})(2\pi G)(e^{j\omega})$
*   **Multiplication Property**: $x[n]y[n] \leftrightarrow \frac{1}{2\pi} X(e^{j\omega})Y(e^{j\omega})$

This comprehensive study note provides a thorough understanding of the Fourier Transform, covering all theoretical concepts and formulas required to solve problems like Q1 from GATE 2021.