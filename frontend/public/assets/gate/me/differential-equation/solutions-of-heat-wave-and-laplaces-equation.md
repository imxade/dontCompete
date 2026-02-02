**Solutions of Heat Wave and Laplace's Equation**
=============================================

### Introduction

Laplace's equation is a fundamental partial differential equation (PDE) that describes the behavior of physical systems, including heat conduction and electrostatics. In this theory note, we will cover the solutions to Laplace's equation in three-dimensional Cartesian space, with a focus on the surface integral of a function.

### Core Concepts

**Laplace's Equation**

The Laplace operator $\nabla^2$ is defined as:

$$\nabla^2 f = \frac{\partial^2f}{\partial x^2} + \frac{\partial^2f}{\partial y^2} + \frac{\partial^2f}{\partial z^2}$$

Laplace's equation in three-dimensional Cartesian space is:

$$\nabla^2 f = 0$$

This equation describes the behavior of physical systems, including heat conduction and electrostatics.

**Green's Function**

The Green's function for Laplace's equation in three-dimensional Cartesian space is given by:

$$G(\mathbf{x}, \mathbf{y}) = \frac{1}{4\pi}\left|\frac{\mathbf{x}-\mathbf{y}}{\lVert\mathbf{x}-\mathbf{y}\rVert^3}\right|$$

where $\mathbf{x}$ and $\mathbf{y}$ are two points in three-dimensional space.

### Key Formulas/Theorems

**Divergence Theorem**

The divergence theorem states that for a vector field $\mathbf{F}$:

$$\iiint_{V} \nabla\cdot\mathbf{F}\,dV = \iint_{S} \mathbf{F}\cdot\hat{\mathbf{n}}\,dS$$

where $V$ is the volume enclosed by surface $S$, and $\hat{\mathbf{n}}$ is the outward unit normal vector.

**Surface Integral of a Function**

The surface integral of a function $\phi$ over a surface $S$ is given by:

$$\iint_{S} \phi\,dS = \iiint_{V} \nabla\cdot(\phi\mathbf{n})\,dV - \iiint_{V} \nabla\phi\cdot\mathbf{n}\,dV$$

where $V$ is the volume enclosed by surface $S$, and $\mathbf{n}$ is the outward unit normal vector.

### Problem Solving Patterns

**Using the Divergence Theorem**

When solving problems involving surface integrals of functions, we can use the divergence theorem to simplify the problem. Specifically, if we have a function $\phi$ defined on a surface $S$, we can use the divergence theorem to rewrite the surface integral as a volume integral:

$$\iint_{S} \phi\,dS = \iiint_{V} \nabla\cdot(\phi\mathbf{n})\,dV - \iiint_{V} \nabla\phi\cdot\mathbf{n}\,dV$$

**Using the Green's Function**

We can use the Green's function to solve problems involving Laplace's equation. Specifically, if we have a function $\phi$ defined on a surface $S$, we can use the Green's function to compute the surface integral:

$$\iint_{S} \phi\,dS = \iiint_{V} G(\mathbf{x}, \mathbf{y})\nabla^2\phi\,dV$$

### Examples with Solutions

**Example 1: Surface Integral of a Function**

Given the function $\phi(x,y,z) = \frac{1}{(x^2+y^2+z^2)^{3/2}}$, compute the surface integral over the surface of a unit sphere:

$$\iint_{S} \phi\,dS = ?$$

Using the divergence theorem and the Green's function, we can rewrite the surface integral as a volume integral:

$$\iint_{S} \phi\,dS = \iiint_{V} G(\mathbf{x}, \mathbf{y})\nabla^2\phi\,dV$$

Since $\phi$ is harmonic (i.e., satisfies Laplace's equation), we have:

$$\nabla^2\phi = 0$$

Therefore, the surface integral is zero:

$$\iint_{S} \phi\,dS = 0$$

**Example 2: Surface Integral of a Function**

Given the function $\phi(x,y,z) = x^2+y^2+z^2$, compute the surface integral over the surface of a unit sphere:

$$\iint_{S} \phi\,dS = ?$$

Using the divergence theorem and the Green's function, we can rewrite the surface integral as a volume integral:

$$\iint_{S} \phi\,dS = \iiint_{V} G(\mathbf{x}, \mathbf{y})\nabla^2\phi\,dV$$

Since $\phi$ is not harmonic (i.e., does not satisfy Laplace's equation), we have:

$$\nabla^2\phi = 6$$

Therefore, the surface integral is given by:

$$\iint_{S} \phi\,dS = \frac{1}{4\pi}\iiint_{V} G(\mathbf{x}, \mathbf{y})6\,dV$$

Using the properties of the Green's function, we can simplify this expression to obtain:

$$\iint_{S} \phi\,dS = 3$$

### Common Pitfalls

**Missing the Divergence Theorem**

Students often miss the opportunity to use the divergence theorem to simplify surface integrals. This can lead to unnecessary calculations and errors in solving problems.

**Not Using the Green's Function**

Students also often fail to recognize when the Green's function can be used to solve a problem involving Laplace's equation. This can lead to difficulties in computing surface integrals and other quantities of interest.

### Quick Summary

* **Laplace's Equation**: $\nabla^2 f = 0$
* **Green's Function**: $G(\mathbf{x}, \mathbf{y}) = \frac{1}{4\pi}\left|\frac{\mathbf{x}-\mathbf{y}}{\lVert\mathbf{x}-\mathbf{y}\rVert^3}\right|$
* **Divergence Theorem**: $\iiint_{V} \nabla\cdot\mathbf{F}\,dV = \iint_{S} \mathbf{F}\cdot\hat{\mathbf{n}}\,dS$

Note: This summary is not exhaustive and should be used as a supplement to the detailed notes above.