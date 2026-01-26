**Transfer Function: G(s)**
=========================

### Introduction

The transfer function of a control system is a mathematical representation that describes the relationship between the input and output signals. It's a crucial concept in control systems, and understanding it is essential for analyzing and designing control systems.

### Core Concepts

#### Definition

The transfer function **G(s)** is defined as the ratio of the Laplace transform of the output signal **Y(s)** to the Laplace transform of the input signal **R(s)**:

$$
G(s) = \frac{Y(s)}{R(s)}
$$

#### Types of Transfer Functions

*   **Stable transfer function**: A transfer function with all poles in the left half of the s-plane.
*   **Unstable transfer function**: A transfer function with at least one pole in the right half of the s-plane.

### Key Formulas/Theorems

#### Final Value Theorem

The final value theorem states that if a signal has a finite limit as time approaches infinity, then:

$$
\lim_{s \to 0} sY(s) = \lim_{t \to \infty} y(t)
$$

### Problem Solving Patterns

1.  **Given transfer function**: Identify the type of system (stable or unstable).
2.  **Apply Laplace transform**: Find the Laplace transforms of the input and output signals.
3.  **Evaluate transfer function**: Calculate the transfer function using the given transfer function equation.
4.  **Simplify expression**: Simplify the resulting expression to determine the final value.

### Examples with Solutions

**Example:**

Given the transfer function:

$$
G(s) = \frac{2}{s + 1}
$$

Find the output signal if a unit step input is applied.

**Solution:**

*   Apply Laplace transform to the input signal:
    *   $$R(s) = \frac{1}{s}$$
*   Evaluate transfer function using given equation:
    *   $$Y(s) = G(s)R(s) = \frac{2}{s + 1}\frac{1}{s}$$
*   Simplify expression to determine the final value:

```mermaid
graph LR;
    A[Step input] --> B[Laplace transform];
    B --> C[Y(s)];
    C --> D[Evaluate transfer function];
    D --> E[Simplify expression];
```

**Final Answer:**

Using the final value theorem, we find that:

$$\lim_{s \to 0}sY(s) = \frac{2}{1} = 2$$

The output signal is a unit step function.

### Common Pitfalls

*   **Incorrect application of Laplace transform**: Verify that the input and output signals are correctly transformed.
*   **Ignoring final value theorem**: Use the final value theorem to determine the final value if applicable.

### Quick Summary

*   Transfer function: Describes relationship between input and output signals
*   Types of transfer functions: Stable, unstable
*   Final Value Theorem: Determine final value using Laplace transforms
*   Key formulas/theorems: Laplace transform, transfer function equation