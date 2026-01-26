**Steady State Error**
=====================

### Introduction
The steady-state error (SSE) of a control system is a measure of its ability to track a desired input signal. It represents the difference between the actual and desired outputs as time approaches infinity.

### Core Concepts

#### Steady-State Error Definition
The SSE for a unit step input can be calculated using the final-value theorem:

$$ \lim_{s \to 0} sY(s) = \lim_{s \to 0} G(s)R(s) $$

where $G(s)$ is the transfer function of the system, and $R(s)$ is the Laplace transform of the input signal.

#### Steady-State Error for Ramp Input
For a unit ramp input, the SSE can be calculated using:

$$ E_{ss} = \lim_{s \to 0} sY(s) = K_p $$

where $K_p$ is the position error constant.

### Key Formulas/Theorems

LaTeX
```latex
\begin{align*}
E_{ss} &= \frac{1 + G(0)}{G'(0)}
&\text{for unit step input}\\
E_{ss} &= K_p
&\text{for unit ramp input}
\end{align*}
```

### Problem Solving Patterns

*   Analyze the transfer function and determine its type (e.g., first-order, second-order).
*   Identify the input signal (unit step or unit ramp) to apply the correct SSE formula.
*   Calculate $G(0)$ and $G'(0)$ for the transfer function.

### Examples with Solutions

**Example 1: Unit Step Input**

Consider a system with transfer function:

$$ G(s) = \frac{3}{s+2} $$

If the input is a unit step, calculate the SSE:

```mermaid
graph LR
A[Input] --> B[Transfer Function]
B[G(s)] --> C[Final-Value Theorem]
C[E_ss] --> D[Answer]
```

Solving for $E_{ss}$ using the final-value theorem:

$$ \lim_{s \to 0} sY(s) = \lim_{s \to 0} G(s)R(s) $$

$$ E_{ss} = \frac{1 + G(0)}{G'(0)} = \frac{1}{3/2} = \frac{2}{3} $$

**Example 2: Unit Ramp Input**

Consider a system with transfer function:

$$ G(s) = \frac{4s+6}{s^2+s+1} $$

If the input is a unit ramp, calculate the SSE:

```mermaid
graph LR
A[Input] --> B[Transfer Function]
B[G(s)] --> C[K_p]
C[E_ss] --> D[Answer]
```

Calculating $K_p$ using the transfer function and SSE formula for unit ramp input:

$$ E_{ss} = K_p = G(0) = \frac{6}{1} = 6 $$

### Common Pitfalls

*   Misidentifying the type of input signal (unit step or unit ramp).
*   Failing to apply the correct SSE formula.
*   Not considering the transfer function's zeros and poles.

### Quick Summary

*   Steady-state error is a measure of a control system's ability to track desired inputs.
*   For unit step input, use the final-value theorem: $ \lim_{s \to 0} sY(s) = \lim_{s \to 0} G(s)R(s) $.
*   For unit ramp input, use: $ E_{ss} = K_p $.

Note: External images are not included in this response. If an external image is required, it would be properly formatted as per the instructions.