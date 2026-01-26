**Mean Value Theorem**
=======================

### Introduction

The Mean Value Theorem (MVT) is a fundamental concept in calculus that relates to the behavior of functions. It states that if a function is continuous on a closed interval and differentiable on an open interval within it, then there exists at least one point where the derivative equals the average rate of change of the function.

### Core Concepts

#### Continuous and Differentiable Functions

A function $f(x)$ is said to be **continuous** at a point $x=a$ if $\lim_{x\to a} f(x) = f(a)$.

A function $f(x)$ is said to be **differentiable** at a point $x=a$ if the limit exists:

$$\frac{d}{dx}f(x)|_{x=a} = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}$$

#### Average Rate of Change

The average rate of change of a function $f(x)$ over an interval $[a,b]$ is given by:

$$\text{Average Rate of Change} = \frac{f(b)-f(a)}{b-a}$$

### Key Formulas/Theorems

**Mean Value Theorem (MVT)**

Let $f(x)$ be a function that is continuous on the closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. Then, there exists at least one point $c$ in $(a,b)$ such that:

$$\frac{d}{dx}f(x)|_{x=c} = \text{Average Rate of Change}$$

$$\frac{f(b)-f(a)}{b-a} = f'(c)$$

### Problem Solving Patterns

When applying the MVT, follow these steps:

1.  Check for continuity and differentiability on the given interval.
2.  Calculate the average rate of change over the interval.
3.  Identify the point(s) where the derivative equals the average rate of change.

### Examples with Solutions

**Example 1**

Let $f(x)=x^2$ be a function that is continuous and differentiable on the interval $[0,2]$. Find the value of $c$ such that:

$$\frac{d}{dx}f(x)|_{x=c} = \text{Average Rate of Change}$$

**Solution**

The average rate of change over the interval $[0,2]$ is given by:

$$\text{Average Rate of Change} = \frac{f(2)-f(0)}{2-0} = \frac{4-0}{2} = 2$$

Since $f(x)=x^2$ is differentiable on $(0,2)$, there exists a point $c\in (0,2)$ such that:

$$f'(c) = 2$$

We can find the value of $c$ by setting the derivative equal to 2 and solving for $c$:

$$\frac{d}{dx}(x^2) = 2x \Rightarrow 2x=2 \Rightarrow x=1$$

Therefore, the value of $c$ is $1$.

### Common Pitfalls

*   Failing to check for continuity and differentiability on the given interval.
*   Not identifying the correct point(s) where the derivative equals the average rate of change.
*   Misapplying the MVT in complex scenarios involving multiple intervals or functions.

### Quick Summary

| Concept | Description |
| --- | --- |
| Mean Value Theorem (MVT) | States that if a function is continuous on a closed interval and differentiable on an open interval within it, then there exists at least one point where the derivative equals the average rate of change. |
| Average Rate of Change | The average rate of change of a function over an interval. |
| Continuous and Differentiable Functions | A function is said to be continuous/differentiable if certain conditions are met. |

### Online Resources

For further reading or visual aids, refer to:

*   Khan Academy: [Mean Value Theorem](https://www.khanacademy.org/math/calculus-ab/multivar-calculus/mean-value-theorem/v/mean-value-theorem)
*   MIT OpenCourseWare: [Calculus III - Mean Value Theorem](https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/index.htm)

Note:

*   This is a basic explanation of the MVT and its application. More advanced topics, such as the MVT for functions with complex intervals or multiple variables, are not covered here.
*   Practice problems and exercises can be found in textbooks on calculus or online resources like Khan Academy.