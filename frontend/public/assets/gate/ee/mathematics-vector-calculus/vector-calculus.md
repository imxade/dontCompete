**Vector Calculus Theory Note**
================================

**Introduction**
---------------

Vector calculus is a branch of mathematics that deals with the application of vector operations to scalar fields and other vectors. It plays a crucial role in various fields such as physics, engineering, and computer science.

**Core Concepts**
-----------------

### Vectors and Scalars

* A **vector** is a mathematical object that has both magnitude (length) and direction.
* A **scalar** is a numerical value that represents a quantity without direction.

### Vector Operations

* Addition: Two vectors can be added by combining their components.
* Subtraction: The difference between two vectors is obtained by subtracting the corresponding components.
* Scalar Multiplication: A vector can be scaled by multiplying its components with a scalar.

### Gradient, Divergence, and Curl

* **Gradient** (∇f): Measures the rate of change of a function f in different directions. It's a vector that points in the direction of maximum increase of f.
* **Divergence** (div F): Measures the amount of "source" or "sink" of a vector field F at a point. It's a scalar value.
* **Curl** (∇×F): Measures the rotation or circulation of a vector field F around a point. It's a vector that points in the direction of maximum rotation.

### Directional Derivative

* The directional derivative of a function f at a point P in the direction of a unit vector u is denoted by ∂f/∂u and represents the rate of change of f in the direction of u.

**Key Formulas/Theorems**
-------------------------

* **Gradient Theorem**: ∇f(x, y, z) = (∂f/∂x)i + (∂f/∂y)j + (∂f/∂z)k
* **Divergence Theorem**: div F(x, y, z) = ∂F_x/∂x + ∂F_y/∂y + ∂F_z/∂z
* **Curl Theorem**: ∇×F(x, y, z) = (∂F_z/∂y - ∂F_y/∂z)i + (∂F_x/∂z - ∂F_z/∂x)j + (∂F_y/∂x - ∂F_x/∂y)k
* **Directional Derivative Formula**: ∂f/∂u = u · ∇f

**Problem Solving Patterns**
---------------------------

1. **Recognize the type of problem**: Identify whether it involves gradient, divergence, curl, or directional derivative.
2. **Apply relevant formulas and theorems**: Use the appropriate formula or theorem to solve the problem.

**Examples with Solutions**
-------------------------

### Example 1: Gradient

Find the gradient of f(x, y) = x^2y at (1, 2).

∇f(x, y) = (∂f/∂x)i + (∂f/∂y)j
= 2xyi + x^2j
= 4i + j

### Example 2: Directional Derivative

Find the directional derivative of f(x, y, z) = xyz at (1, 1, 1) in the direction of u = i + j + k.

∂f/∂u = u · ∇f
= (i + j + k) · (∂f/∂x)i + (∂f/∂y)j + (∂f/∂z)k
= i + j + k

### Example 3: Divergence

Find the divergence of F(x, y, z) = (2xyi - x^2zj + xyzk).

div F(x, y, z) = ∂F_x/∂x + ∂F_y/∂y + ∂F_z/∂z
= 2yi - 2xzj + yzk

**Common Pitfalls**
-------------------

* **Misinterpretation of vector operations**: Pay attention to the order and type of vectors involved.
* **Incorrect application of formulas and theorems**: Double-check your work and ensure you're using the right formula for the given problem.

**Quick Summary**
-----------------

* Vectors and scalars
* Vector operations (addition, subtraction, scalar multiplication)
* Gradient, divergence, and curl
* Directional derivative formula
* Key formulas and theorems