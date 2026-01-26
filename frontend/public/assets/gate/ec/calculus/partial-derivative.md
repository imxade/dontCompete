**Partial Derivative**
=======================

### Introduction

In multivariable calculus, partial derivatives are used to study how functions of multiple variables change when one or more of those variables are changed. This concept is crucial in many fields such as physics, engineering, and economics.

### Core Concepts

A partial derivative of a function $f(x,y,z)$ with respect to the variable $x$ is denoted by $\frac{\partial f}{\partial x}$ and represents the rate of change of the function with respect to $x$, keeping $y$ and $z$ constant. Similarly, we can define partial derivatives with respect to $y$ and $z$.

The formula for a partial derivative is:

$$
\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h,y,z) - f(x,y,z)}{h}
$$

where $h$ is an infinitesimally small change in the variable $x$.

### Key Formulas/Theorems

**Partial Derivative Rules**

1. **Linearity**: The partial derivative of a sum or difference of functions is the sum or difference of their individual partial derivatives.
2. **Product Rule**: If $f(x,y,z) = u(x,y,z)v(x,y,z)$, then:
$$
\frac{\partial f}{\partial x} = \frac{\partial u}{\partial x}v + u\frac{\partial v}{\partial x}
$$

**Chain Rule**

If $f(x,y,z) = g(h(x,y,z))$, then:

$$
\frac{\partial f}{\partial x} = \frac{\partial g}{\partial h}\cdot\frac{\partial h}{\partial x}
$$

### Problem Solving Patterns

1. **Identify the function**: Clearly define the function for which you need to find the partial derivative.
2. **Determine the variable with respect to which you are taking the derivative**: Identify the variable that needs to be changed.
3. **Apply the relevant partial derivative rule**: Use linearity, product rule, or chain rule as needed.

### Examples with Solutions

**Example 1**

Find $\frac{\partial f}{\partial x}$ of $f(x,y,z) = e^{xy} \sin(z)$.

Solution:
Using the product rule:

$$
\frac{\partial f}{\partial x} = (e^{xy})'(y)\sin(z) + e^{xy}(z)'
= y e^{xy}\sin(z)
$$

**Example 2**

Find $\frac{\partial f}{\partial z}$ of $f(x,y,z) = \cos(xy)$.

Solution:
Using the chain rule:

$$
\frac{\partial f}{\partial z} = (-\sin(xy))(x)'
= -xy \sin(xy)
$$

### Common Pitfalls

* Failing to identify the correct variable with respect to which you are taking the derivative.
* Misapplying partial derivative rules (e.g., using product rule when linearity is applicable).
* Not checking for chain rule applicability.

### Quick Summary

* Partial derivatives are used to study how functions of multiple variables change.
* Key formulas and theorems include linearity, product rule, and chain rule.
* Problem-solving patterns involve identifying the function, variable with respect to which you are taking the derivative, and applying relevant partial derivative rules.