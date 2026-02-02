**Linear Signal Theory**
========================

### Introduction
Signal processing and linear systems are fundamental concepts in electrical engineering. The goal of this note is to provide a comprehensive overview of linear signal theory, focusing on the principles, formulas, and problem-solving strategies required for GATE CS exam.

### Core Concepts
A linear system is one where the output is directly proportional to the input, with no distortion or change in waveform. Mathematically, this can be represented as:

$$y(n) = x(n) \ast h(n)$$

where $x(n)$ is the input signal, $h(n)$ is the impulse response of the system, and $y(n)$ is the output signal.

**Linearity Property**: A linear system satisfies the following two properties:

1. Homogeneity: If the input signal is scaled by a factor $\alpha$, then the output is also scaled by the same factor:
$$\alpha x(n) \ast h(n) = \alpha (x(n) \ast h(n))$$
2. Additivity: The output of a linear system to two separate inputs is equal to the sum of their individual outputs:
$$(x_1(n) + x_2(n)) \ast h(n) = (x_1(n) \ast h(n)) + (x_2(n) \ast h(n))$$

### Key Formulas/Theorems
**Convolution**: The convolution of two discrete-time signals $x(n)$ and $h(n)$ is defined as:

$$y(n) = x(n) \ast h(n) = \sum_{k=-\infty}^{\infty} x(k)h(n-k)$$

**Discrete Fourier Transform (DFT)**: The DFT of a discrete-time signal $x(n)$ is given by:

$$X[k] = \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi}{N}nk}$$

where $N$ is the number of samples in the signal.

**Inverse DFT (IDFT)**: The IDFT of a sequence $X[k]$ is given by:

$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]e^{j\frac{2\pi}{N}nk}$$

### Problem Solving Patterns
When dealing with linear systems, the following problem-solving patterns are common:

*   Use the convolution property to find the output signal.
*   Apply the linearity properties (homogeneity and additivity) as needed.

### Examples with Solutions
**Example 1**: Find the output of a linear system with input $x[n] = \{1, 2, 3\}$ and impulse response $h[n] = \{0.5, 1, 0.5\}$. Use convolution to find the output signal.

```mermaid
graph LR
A[Input: x(n)] --> B[Impulse Response: h(n)]
B --> C[Convolution]
C --> D[Output: y(n)]
```

Using the formula for convolution:

$$y[n] = \sum_{k=0}^{N-1} x[k]h[n-k]$$

Substituting the values, we get:

$$\begin{align*}
y[0] &= x[0]h[0] + x[1]h[-1] + x[2]h[2] \\
&= 1 \times 0.5 + 2 \times (-1) + 3 \times 0.5 \\
&= 1 - 2 + 1.5 = 0.5
\end{align*}$$

Similarly, we can find the values of $y[1]$ and $y[2]$. The output signal is:

$$y[n] = \begin{cases}
0.5 & n=0 \\
-0.5 & n=1 \\
1 & n=2
\end{cases}$$

### Common Pitfalls
Students often miss the linearity properties (homogeneity and additivity) or incorrectly apply the convolution formula.

### Quick Summary
*   Linearity property: Homogeneity and Additivity.
*   Convolution: $y(n) = x(n) \ast h(n)$.
*   DFT: $X[k] = \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi}{N}nk}$.
*   IDFT: $x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]e^{j\frac{2\pi}{N}nk}$.