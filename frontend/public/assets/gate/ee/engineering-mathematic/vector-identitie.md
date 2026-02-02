**Vector Identities**
=====================

### Introduction

Vector identities are fundamental concepts in Engineering Mathematics that describe how vectors behave under various operations such as dot product, cross product, and differentiation. These identities are crucial for solving problems involving vector calculus, particularly when dealing with gradient, divergence, and curl.

### Core Concepts

#### Vector Operations

*   **Dot Product**: The dot product of two vectors $\mathbf{a}$ and $\mathbf{b}$ is denoted by $\mathbf{a} \cdot \mathbf{b}$ and is given by:
    $$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos \theta$$
*   **Cross Product**: The cross product of two vectors $\mathbf{a}$ and $\mathbf{b}$ is denoted by $\mathbf{a} \times \mathbf{b}$ and is given by:
    $$\mathbf{a} \times \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \sin \theta \mathbf{n}$$
*   **Gradient**: The gradient of a scalar function $f(x, y, z)$ is denoted by $\nabla f$ and is given by:
    $$\nabla f = \frac{\partial f}{\partial x} \mathbf{i} + \frac{\partial f}{\partial y} \mathbf{j} + \frac{\partial f}{\partial z} \mathbf{k}$$

#### Vector Identities

*   **Gradient of a Dot Product**:
    $$\nabla (\mathbf{a} \cdot \mathbf{b}) = (\mathbf{a} \cdot \nabla) \mathbf{b} + (\mathbf{b} \cdot \nabla) \mathbf{a}$$
*   **Gradient of a Cross Product**:
    $$\nabla (\mathbf{a} \times \mathbf{b}) = (\mathbf{b} \cdot \nabla) \mathbf{a} - (\mathbf{a} \cdot \nabla) \mathbf{b}$$
*   **Divergence of a Cross Product**:
    $$\nabla \cdot (\mathbf{a} \times \mathbf{b}) = \mathbf{b} \cdot \nabla \times \mathbf{a} - \mathbf{a} \cdot \nabla \times \mathbf{b}$$

### Key Formulas/Theorems

*   **Divergence Theorem**:
    $$\iiint_V (\nabla \cdot \mathbf{F}) dV = \iint_S \mathbf{F} \cdot d\mathbf{A}$$
*   **Stokes' Theorem**:
    $$\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{A} = \oint_C \mathbf{F} \cdot d\mathbf{l}$$

### Problem Solving Patterns

When dealing with vector identities, it's essential to identify the type of operation involved and apply the corresponding identity. Here are some common patterns:

*   **Chain Rule**: When differentiating a composition of functions, use the chain rule to find the derivative.
*   **Product Rule**: When differentiating a product of functions, use the product rule to find the derivative.
*   **Quotient Rule**: When differentiating a quotient of functions, use the quotient rule to find the derivative.

### Examples with Solutions

**Example 1**

Find the gradient of the function $f(x, y) = x^2 + 3xy$.

Solution:

$$\nabla f = \frac{\partial f}{\partial x} \mathbf{i} + \frac{\partial f}{\partial y} \mathbf{j}$$
$$= (2x + 3y) \mathbf{i} + 3x \mathbf{j}$$

**Example 2**

Find the divergence of the vector field $\mathbf{F} = (x^2y, z^2x, yz^2)$.

Solution:

$$\nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$$
$$= (2xy, 2xz, 2yz)$$

### Common Pitfalls

*   **Confusing gradient and divergence**: Make sure to use the correct identity for each operation.
*   **Forgetting about boundary terms**: When applying vector identities, don't forget about any boundary terms that may arise.

### Quick Summary

| Concept | Formula/Identity |
| --- | --- |
| Gradient of a Dot Product | $\nabla (\mathbf{a} \cdot \mathbf{b}) = (\mathbf{a} \cdot \nabla) \mathbf{b} + (\mathbf{b} \cdot \nabla) \mathbf{a}$ |
| Gradient of a Cross Product | $\nabla (\mathbf{a} \times \mathbf{b}) = (\mathbf{b} \cdot \nabla) \mathbf{a} - (\mathbf{a} \cdot \nabla) \mathbf{b}$ |
| Divergence of a Cross Product | $\nabla \cdot (\mathbf{a} \times \mathbf{b}) = \mathbf{b} \cdot \nabla \times \mathbf{a} - \mathbf{a} \cdot \nabla \times \mathbf{b}$ |
| Divergence Theorem | $\iiint_V (\nabla \cdot \mathbf{F}) dV = \iint_S \mathbf{F} \cdot d\mathbf{A}$ |
| Stokes' Theorem | $\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{A} = \oint_C \mathbf{F} \cdot d\mathbf{l}$ |

This comprehensive note covers all the theoretical concepts, formulas, and insights required to solve vector identity problems. By mastering these concepts, students will be well-prepared for future exams and challenges in Engineering Mathematics.