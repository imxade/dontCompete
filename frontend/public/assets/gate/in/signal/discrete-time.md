**Discrete Time Signal**
=======================

### Introduction

In digital signal processing, discrete time signals are a fundamental concept that deals with sampled continuous-time signals. These signals have values at specific intervals, known as sampling instants, and are represented by their samples.

### Core Concepts

#### Sampling

Sampling is the process of converting a continuous-time signal into a discrete-time signal. It involves measuring the amplitude of the signal at regular intervals, called the sampling period $T_s$. The sampled signal is then represented by its values at these sampling instants.

#### Discrete-Time Signal

A discrete-time signal is a sequence of values that are defined at specific points in time, known as sampling instants. It can be denoted as $x[n]$ or $x(t_n)$, where $n$ is the index of the sample and $t_n$ is the sampling instant.

#### Discrete-Time Fourier Transform (DTFT)

The DTFT is an extension of the continuous-time Fourier transform to discrete-time signals. It transforms a discrete-time signal into its frequency domain representation, which consists of a sequence of complex exponentials. The DTFT is given by:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$

where $X(e^{j\omega})$ is the discrete-time Fourier transform of $x[n]$ and $\omega$ is the frequency.

### Key Formulas/Theorems

* **Discrete-Time Fourier Transform (DTFT)**: $$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$
* **Inverse DTFT**: $$x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\omega}) e^{j\omega n} d\omega$$

### Problem Solving Patterns

When solving problems involving discrete-time signals, follow these steps:

1. **Analyze the problem**: Understand what is being asked and identify the key concepts involved.
2. **Draw a diagram**: Use Mermaid diagrams to represent the signal flow or relationships between variables.
3. **Apply DTFT**: Use the DTFT to transform the discrete-time signal into its frequency domain representation.
4. **Solve for the desired variable**: Apply algebraic manipulations and theorems to solve for the desired variable.

### Examples with Solutions

**Example 1**

Given a discrete-time signal $x[n] = \cos(\omega_0 n)$, find its DTFT.

```latex
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}
= \sum_{n=-\infty}^{\infty} \cos(\omega_0 n) e^{-j\omega n}
= \frac{1}{2} \left( e^{j\omega/2} - e^{-j\omega/2} \right)
= j \sin(\omega/2) / (j \sin(\omega_0/2))
```

**Example 2**

Given a discrete-time signal $x[n] = x_0 + x_1 n$, find its DTFT.

```latex
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}
= (x_0 + x_1 n) \sum_{n=-\infty}^{\infty} e^{-j\omega n}
= 2 \pi j x_1 / (e^{j\omega} - 1)
```

### Common Pitfalls

* **Incorrectly applying the DTFT**: Remember to apply the correct formulas and theorems.
* **Ignoring periodicity**: Discrete-time signals are often periodic, so be sure to consider this when solving problems.

### Quick Summary

* **Discrete-Time Signal**: A sequence of values defined at specific points in time.
* **DTFT**: Transforms a discrete-time signal into its frequency domain representation.
* **Key Formulas/Theorems**:
	+ DTFT: $$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$
	+ Inverse DTFT: $$x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\omega}) e^{j\omega n} d\omega$$

Note: This is a basic outline of the discrete-time signal topic. You may need to expand on this or add more details depending on your specific needs.