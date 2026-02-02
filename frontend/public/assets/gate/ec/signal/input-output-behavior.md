**Input Output Behavior - Signal**
=====================================

### Introduction
---------------

In this section, we will delve into the fundamental principles of input output behavior in discrete-time systems. Understanding these concepts is crucial for analyzing and designing digital signal processing systems.

### Core Concepts
-----------------

A discrete-time system is a mathematical model that takes an input sequence `x[n]` and produces an output sequence `y[n]`. The relationship between the input and output sequences can be represented as:

`y[n] = ∑[k=-∞ to ∞] h[k]x[n-k]`

where `h[k]` is the impulse response of the system.

### Key Formulas/Theorems
-------------------------

LaTeX Equation
```latex
\boxed{y[n] = \sum_{k=-\infty}^{\infty} h[k]x[n-k]}
```
This equation represents the convolution sum, which describes how the input sequence `x[n]` is transformed into the output sequence `y[n]` by the system's impulse response `h[k]`.

### Problem Solving Patterns
---------------------------

1.  **Convolution Sum**: When analyzing a discrete-time system, the first step is to find the convolution sum of the input and impulse response sequences.
2.  **Linearity**: The system exhibits linearity if it satisfies the following property:

`a*x[n] + b*y[n] = (ax[n] + by[n])`

where `a` and `b` are constants.

3.  **Time-Invariance**: A time-invariant system preserves its behavior over time, meaning that a delay in the input sequence does not affect the output:

`y[n-k] = y[n]`

### Examples with Solutions
---------------------------

**Example 1**

Find the output of a discrete-time system when the input is `x[n] = δ[n-2]`, where `δ[n-2]` is the unit impulse at `n=2`. Given that the impulse response of the system is `h[k] = u[k+1]`, find the output sequence `y[n]`.

**Solution**

Using the convolution sum equation, we have:

```latex
y[n] = \sum_{k=-\infty}^{\infty} h[k]x[n-k]
```

Substituting `h[k] = u[k+1]` and `x[n-k] = δ[n-2-k]`, we get:

```latex
y[n] = \sum_{k=-\infty}^{\infty} u[k+1]\delta[n-2-k]
```

Since the delta function is only non-zero at `n=2+k`, we can simplify this expression to:

```latex
y[n] = u[n-3]
```

**Example 2**

A discrete-time system has an impulse response of `h[k] = (1/2)^(k+1)`. Find the output sequence when the input is `x[n] = cos(πn/4)`.

**Solution**

Using the convolution sum equation, we have:

```latex
y[n] = \sum_{k=-\infty}^{\infty} h[k]x[n-k]
```

Substituting `h[k] = (1/2)^(k+1)` and `x[n-k] = cos(π(n-k)/4)`, we get:

```latex
y[n] = \sum_{k=-\infty}^{\infty} (1/2)^{k+1}\cos(\pi(n-k)/4)
```

This expression can be simplified using trigonometric identities and properties of the cosine function.

### Common Pitfalls
-------------------

*   **Incorrect Convolution Sum**: Students often make mistakes when applying the convolution sum equation, such as forgetting to include or exclude terms.
*   **Overlooking Linearity/Time-Invariance**: Failing to recognize these properties can lead to incorrect solutions and misunderstanding of system behavior.

### Quick Summary
---------------

| Key Concept | Brief Description |
| --- | --- |
| Convolution Sum | Represents the relationship between input and output sequences in discrete-time systems. |
| Linearity | Property where a system preserves its behavior under scaling and shifting operations. |
| Time-Invariance | Property where a system's behavior remains unchanged over time, regardless of delays in the input sequence. |

Note: The content of this theory note is based on the provided source questions and may require expansion or addition to cover all relevant topics.