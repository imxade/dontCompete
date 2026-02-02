**Calculus Theory Note**
========================

### Introduction

Calculus is a branch of mathematics that deals with the study of continuous change, particularly in the context of functions and limits. It has two main branches: Differential Calculus (DC) and Integral Calculus (IC). This theory note will cover the core concepts, formulas, and problem-solving patterns required to tackle questions like Q1 from the GATE CS exam.

### Core Concepts

#### Limits

The limit of a function $f(x)$ as $x$ approaches $a$ is denoted by $\lim_{x \to a} f(x)$. It represents the behavior of the function near the point $a$.

**Definition:** Given a function $f: \mathbb{R} \to \mathbb{R}$ and a real number $a$, we say that:

$$\lim_{x \to a} f(x) = L \iff \forall \epsilon > 0, \exists \delta > 0 \text{ such that } 0 < |x-a| < \delta \implies |f(x)-L| < \epsilon$$

#### Derivatives

The derivative of a function $f(x)$ at point $a$ is denoted by $f'(a)$. It represents the rate of change of the function near the point $a$.

**Definition:** Given a function $f: \mathbb{R} \to \mathbb{R}$ and a real number $a$, we say that:

$$f'(a) = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h}$$

#### Integrals

The definite integral of a function $f(x)$ from $a$ to $b$ is denoted by $\int_{a}^{b} f(x) dx$. It represents the area under the curve of the function between the limits $a$ and $b$.

**Definition:** Given a function $f: \mathbb{R} \to \mathbb{R}$ and real numbers $a, b$, we say that:

$$\int_{a}^{b} f(x) dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x$$

where $\Delta x = (b-a)/n$ and $x_i^*$ is a point in the $i$-th subinterval.

### Key Formulas/Theorems

* **Derivative Rules**:
	+ Linearity: $f'(ax+b) = af'(ax)$
	+ Chain Rule: $(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$
	+ Product Rule: $(fg)'(x) = f'(x)g(x) + f(x)g'(x)$
	+ Quotient Rule: $\left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x)-f(x)g'(x)}{(g(x))^2}$
* **Integral Formulas**:
	+ Power Rule: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$
	+ Exponential Rule: $\int e^x dx = e^x + C$

### Problem Solving Patterns

When solving problems involving calculus, follow these steps:

1. Identify the type of problem (differential or integral).
2. Determine the specific formula or theorem required.
3. Apply the formula or theorem to derive a solution.
4. Simplify and check your answer.

### Examples with Solutions

**Example 1:**

Find the derivative of $f(x) = x^2 \sin x$ using the product rule.

```latex
\frac{d}{dx} (x^2 \sin x) &= \frac{d}{dx} (x^2) \cdot \sin x + x^2 \cdot \frac{d}{dx} (\sin x) \\
&= 2x \sin x + x^2 \cos x
```

**Example 2:**

Evaluate the definite integral $\int_0^1 x^3 dx$ using the power rule.

```latex
\int_0^1 x^3 dx &= \left[ \frac{x^{4}}{4} \right]_0^1 \\
&= \frac{1}{4} - 0 = \frac{1}{4}
```

### Common Pitfalls

* Failing to apply the correct formula or theorem.
* Ignoring units and dimensions.
* Not simplifying expressions correctly.

### Quick Summary

| Concept | Key Points |
| --- | --- |
| Limits | Definition, notation ($\lim_{x \to a} f(x)$) |
| Derivatives | Definition, derivative rules (linearity, chain rule, product rule) |
| Integrals | Definition, integral formulas (power rule, exponential rule) |

**Note:** This theory note provides a comprehensive overview of calculus concepts and formulas required to tackle questions like Q1 from the GATE CS exam. However, it is essential to practice solving problems and exercises to reinforce understanding and build problem-solving skills.