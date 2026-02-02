# Vector Calculus
=====================================

## Introduction
---------------

Vector calculus is a branch of mathematics that deals with the study of vectors and their properties, particularly in the context of functions of several variables. It combines concepts from vector algebra, differential equations, and multivariable calculus to provide powerful tools for modeling and solving problems in physics, engineering, and other fields.

## Core Concepts
-----------------

### 1. Vector Fields

A **vector field** is a function that assigns a vector to each point in space. It can be thought of as an operator that takes a point as input and produces a vector as output.

### 2. Scalar Fields

A **scalar field** is a function that assigns a scalar (a real number) to each point in space.

### 3. Gradient

The **gradient** of a scalar field `φ(x, y, z)` is a vector field that points in the direction of maximum increase of the scalar field at each point.

`∇φ = (∂φ/∂x)i + (∂φ/∂y)j + (∂φ/∂z)k`

### 4. Divergence

The **divergence** of a vector field `F(x, y, z)` is a scalar that represents the amount of "source" or "sink" at each point.

`∇ ⋅ F = ∂(Fx)/∂x + ∂(Fy)/∂y + ∂(Fz)/∂z`

### 5. Curl

The **curl** of a vector field `F(x, y, z)` is a vector that represents the amount of "rotation" at each point.

`∇ × F = (∂Fz/∂y - ∂Fy/∂z)i + (∂Fx/∂z - ∂Fz/∂x)j + (∂Fy/∂x - ∂Fx/∂y)k`

### 6. Stokes' Theorem

**Stokes' theorem** relates the curl of a vector field to the line integral around a closed curve.

`∫(∇ × F) ⋅ dL = ∮F ⋅ dr`

## Key Formulas/Theorems
-------------------------

* Gradient: `∇φ = (∂φ/∂x)i + (∂φ/∂y)j + (∂φ/∂z)k`
* Divergence: `∇ ⋅ F = ∂(Fx)/∂x + ∂(Fy)/∂y + ∂(Fz)/∂z`
* Curl: `∇ × F = (∂Fz/∂y - ∂Fy/∂z)i + (∂Fx/∂z - ∂Fz/∂x)j + (∂Fy/∂x - ∂Fx/∂y)k`
* Stokes' theorem: `∫(∇ × F) ⋅ dL = ∮F ⋅ dr`

## Problem Solving Patterns
---------------------------

### 1. Vector Calculus Identities

When working with vector calculus, it's essential to remember the following identities:

`∇(φψ) = φ∇ψ + ψ∇φ`
`∇ ⋅ (φF) = φ∇ ⋅ F + F ⋅ ∇φ`
`∇ × (φF) = φ∇ × F + (∇φ) × F`

### 2. Gradient and Divergence

* Use the gradient to find the direction of maximum increase of a scalar field.
* Use the divergence to find the amount of source or sink at each point.

## Examples with Solutions
---------------------------

### Example 1: Find the divergence of a vector field `F(x, y, z) = (x^2y + z)i + (xy^2 - xz)j + (yz^2 + xy)k`

```latex
∇ ⋅ F = ∂(Fx)/∂x + ∂(Fy)/∂y + ∂(Fz)/∂z
= 2xy + y^2 - z
```

### Example 2: Evaluate the line integral `∫(∇ × F) ⋅ dL` around a closed curve for the vector field `F(x, y, z) = (y^2i - x^2j + k)`

```latex
∮F ⋅ dr = ∮(y^2i - x^2j + k) ⋅ (dxi + dyj + dzk)
= ∫(y^2dx - x^2dy + dz)
```

## Common Pitfalls
------------------

* When evaluating line integrals, remember to use Stokes' theorem.
* Be careful when applying vector calculus identities.

## Quick Summary
---------------

* Vector fields and scalar fields are essential concepts in vector calculus.
* Gradient, divergence, and curl are fundamental operators that describe the properties of vector fields.
* Stokes' theorem relates the curl of a vector field to the line integral around a closed curve.

I hope this comprehensive theory note helps you prepare for the GATE CS exam!