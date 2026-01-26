**Vector Analysis for GATE CS Exam**
=====================================

**Introduction**
---------------

Vector analysis is a fundamental tool in engineering mathematics, particularly in fluid mechanics and physics. It provides a powerful framework for describing and analyzing complex phenomena involving vectors. In this theory note, we will cover the key concepts, formulas, and problem-solving techniques required to tackle questions on vector analysis.

**Core Concepts**
-----------------

### Vectors

A vector is a mathematical object that has both magnitude (length) and direction. It can be represented graphically as an arrow in a coordinate system.

### Vector Operations

*   **Addition**: The sum of two vectors, denoted by $\mathbf{a} + \mathbf{b}$.
*   **Scalar Multiplication**: The product of a vector and a scalar, denoted by $c\mathbf{a}$ or $\mathbf{a}c$.
*   **Dot Product** (or **Inner Product**): A way to multiply two vectors together, resulting in a scalar value.

### Gradient

The gradient of a function is a measure of the rate of change of that function with respect to its variables. It is denoted by $\nabla f(x,y)$ or $\frac{\partial f}{\partial x} \mathbf{i} + \frac{\partial f}{\partial y} \mathbf{j}$.

**Key Formulas/Theorems**
-------------------------

### Vector Identities

*   **Divergence Theorem**: $\int_V \nabla \cdot \mathbf{F} dV = \oint_S \mathbf{F} \cdot d\mathbf{A}$
*   **Gradient of a Scalar Field**: $\nabla f(x,y) = \frac{\partial f}{\partial x} \mathbf{i} + \frac{\partial f}{\partial y} \mathbf{j}$

### Curl and Divergence Operators

*   **Curl**: $\nabla \times \mathbf{F} = \left(\frac{\partial F_y}{\partial z} - \frac{\partial F_z}{\partial y}\right)\mathbf{i} + \left(\frac{\partial F_z}{\partial x} - \frac{\partial F_x}{\partial z}\right)\mathbf{j} + \left(\frac{\partial F_x}{\partial y} - \frac{\partial F_y}{\partial x}\right)\mathbf{k}$
*   **Divergence**: $\nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$

**Problem Solving Patterns**
---------------------------

### Simplifying Vector Expressions

To simplify the given expression $2(u\frac{\partial u}{\partial x} - v\frac{\partial u}{\partial y})$ for two-dimensional, incompressible flow:

```mermaid
graph LR
A[Given Expression] --> B[Simplify]
B --> C[Factor out 2]
C --> D[Simplify terms]
D --> E[Final Answer]
```

The final answer is $\boxed{u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y}}$.

**Examples with Solutions**
---------------------------

### Example 1

Simplify the expression $2(u\frac{\partial u}{\partial x} - v\frac{\partial u}{\partial y})$.

Solution:

```mermaid
graph LR
A[Given Expression] --> B[Simplify]
B --> C[Factor out 2]
C --> D[Simplify terms]
D --> E[Final Answer]
```

The final answer is $\boxed{u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y}}$.

### Example 2

Given the vector field $\mathbf{F}(x,y,z) = x^2y \mathbf{i} + z \mathbf{j}$, find its divergence.

Solution:

$\nabla \cdot \mathbf{F} = \frac{\partial (x^2y)}{\partial x} + 0 + \frac{\partial z}{\partial z}$
$= 2xy + 1$

**Common Pitfalls**
------------------

*   Students often forget to apply vector identities when simplifying expressions.
*   Incorrectly applying the divergence or curl operators can lead to incorrect results.

**Quick Summary**
-----------------

*   Vectors have magnitude and direction.
*   Vector operations include addition, scalar multiplication, and dot product.
*   Gradient is a measure of rate of change with respect to variables.
*   Key formulas include vector identities, gradient, and divergence/curl operators.