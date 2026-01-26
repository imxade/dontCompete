**Electrostatics and Vector Field Integration**
======================================================

**Introduction**
---------------

Electrostatics is a branch of physics that deals with the study of electric charges at rest. It forms the basis for understanding electromagnetic fields, which are crucial in the design and analysis of electrical systems. In this note, we will cover the fundamental concepts of electrostatics and vector field integration, focusing on the principles required to solve problems like GATE 2023 Question 62.

**Core Concepts**
----------------

### Electrostatic Field

The electrostatic field $\mathbf{E}$ is a vector field that describes the electric force per unit charge at a given point in space. It is defined as the negative gradient of the electric potential $V$:

$$\mathbf{E} = -\nabla V$$

### Gauss's Law

Gauss's law states that the total electric flux through a closed surface is proportional to the charge enclosed within the surface:

$$\oint \mathbf{E} \cdot d\mathbf{A} = \frac{q_{enc}}{\epsilon_0}$$

where $\epsilon_0$ is the electric constant (permittivity of free space).

### Vector Field Integration

The line integral of a vector field $\mathbf{F}$ along a curve $C$ is defined as:

$$\int_C \mathbf{F} \cdot d\mathbf{l} = \oint \mathbf{F} \cdot d\mathbf{s}$$

where $d\mathbf{l}$ and $d\mathbf{s}$ are the differential displacement vectors along the curve.

**Key Formulas/Theorems**
-------------------------

*   Electrostatic field: $\mathbf{E} = -\nabla V$
*   Gauss's law: $\oint \mathbf{E} \cdot d\mathbf{A} = \frac{q_{enc}}{\epsilon_0}$
*   Line integral of a vector field: $\int_C \mathbf{F} \cdot d\mathbf{l} = \oint \mathbf{F} \cdot d\mathbf{s}$

**Problem Solving Patterns**
---------------------------

To solve problems involving electrostatics and vector field integration, follow these steps:

1.  Identify the type of problem: electrostatic field, electric flux, or line integral.
2.  Determine the relevant formulas and laws to apply.
3.  Set up the necessary mathematical expressions and equations.
4.  Solve for the unknown quantities.

**Examples with Solutions**
---------------------------

### Example 1:

GATE 2023 Question 62

Given the closed curve described by $r = \sqrt{x^2 + y^2}$, where $\theta$ is the angle between the positive x-axis and the line connecting the origin to the point $(x,y)$.

Find the magnitude of the line integral of the vector field $\mathbf{F} = yi - xj$ around the closed curve.

**Solution:**

*   First, parameterize the curve $r = \sqrt{x^2 + y^2}$ as:

$$x = r \cos \theta,$$

$$y = r \sin \theta.$$

*   The vector field $\mathbf{F} = yi - xj$ can be expressed in terms of $r$ and $\theta$:

$\mathbf{F}(r, \theta) = y\hat{i} - x\hat{j}$

$\mathbf{F}(r, \theta) = r \sin \theta \hat{i} - r \cos \theta \hat{j}$

*   Now, we evaluate the line integral $\int_C \mathbf{F} \cdot d\mathbf{l}$ around the closed curve:

$$\int_C \mathbf{F} \cdot d\mathbf{l} = \oint_{0 \leq r \leq 1} (r \sin \theta \hat{i} - r \cos \theta \hat{j}) \cdot dr(\cos \theta \hat{i} + \sin \theta \hat{j})$$

$$= \int_0^{2\pi} (r^2 \sin^2 \theta - r^2 \cos^2 \theta) d\theta$$

*   Evaluating the integral, we get:

$$\oint_{C} \mathbf{F} \cdot d\mathbf{l} = \left[\frac{-r^2}{3}\right]_0^{1} = -\frac{1}{3}$$

Therefore, the magnitude of the line integral is $\boxed{\sqrt{\frac{8}{9}}}$.

### Common Pitfalls
-------------------

*   Misapplication of Gauss's law to problems involving line integrals.
*   Failure to parameterize the curve correctly in vector field integration problems.

**Quick Summary**
-----------------

*   Electrostatic field: $\mathbf{E} = -\nabla V$
*   Gauss's law: $\oint \mathbf{E} \cdot d\mathbf{A} = \frac{q_{enc}}{\epsilon_0}$
*   Line integral of a vector field: $\int_C \mathbf{F} \cdot d\mathbf{l} = \oint \mathbf{F} \cdot d\mathbf{s}$