**Heat Conduction**
=====================

**Introduction**
---------------

Heat conduction is a fundamental mode of heat transfer that occurs due to the collisions between adjacent atoms or molecules. In this note, we will focus on the theoretical aspects of heat conduction and its applications in various fields.

**Core Concepts**
-----------------

### 1. Fourier's Law

Fourier's law describes the rate of heat conduction through a material as follows:

$$Q = -kA\frac{dT}{dx}$$

where $Q$ is the heat transfer rate, $k$ is the thermal conductivity, $A$ is the cross-sectional area, and $\frac{dT}{dx}$ is the temperature gradient.

### 2. Thermal Diffusivity

Thermal diffusivity ($\alpha$) is a measure of how easily heat can flow through a material:

$$\alpha = \frac{k}{\rho c_p}$$

where $k$ is thermal conductivity, $\rho$ is density, and $c_p$ is specific heat capacity.

### 3. One-Dimensional Heat Equation

The one-dimensional heat equation describes the temperature distribution within a material over time:

$$\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}$$

**Key Formulas/Theorems**
-------------------------

* **Fourier's Law**: $Q = -kA\frac{dT}{dx}$
* **Thermal Diffusivity**: $\alpha = \frac{k}{\rho c_p}$
* **One-Dimensional Heat Equation**: $\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}$

**Problem Solving Patterns**
---------------------------

### 1. Analyzing Initial and Boundary Conditions

When solving heat conduction problems, it's essential to identify the initial and boundary conditions.

* Identify the thermal properties of the material (thermal conductivity, density, specific heat capacity).
* Determine the geometry of the problem (one-dimensional, two-dimensional, or three-dimensional).
* Specify the initial temperature distribution and any boundary conditions (e.g., constant temperature, insulated surface).

### 2. Separation of Variables

The separation of variables method can be used to solve the one-dimensional heat equation:

$$T(x,t) = X(x)T(t)$$

Substituting this into the heat equation yields two separate equations for $X(x)$ and $T(t)$.

**Examples with Solutions**
-------------------------

### Example 1: Heat Conduction in a Solid Slab

Consider a solid slab of thickness $H$ with an initial temperature distribution:

$$T(x,0) = T_0\left(1 + \frac{x}{H}\right)$$

The top surface is maintained at constant temperature $T_1$, while the bottom surface is insulated. Find the time required for the temperature at $x=H/2$ to reach 99% of its final steady value.

**Solution:**

* Identify the thermal properties and geometry.
* Use Fourier's Law and the one-dimensional heat equation to obtain a solution.
* Evaluate the temperature distribution at $x=H/2$ and determine the required time.

**Common Pitfalls**
------------------

* Failing to specify the thermal properties of the material.
* Ignoring boundary conditions or initial temperature distributions.
* Not using appropriate units (e.g., $\alpha = \frac{k}{\rho c_p}$).

**Quick Summary**
-----------------

* Fourier's Law: $Q = -kA\frac{dT}{dx}$
* Thermal Diffusivity: $\alpha = \frac{k}{\rho c_p}$
* One-Dimensional Heat Equation: $\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}$
* Analyze initial and boundary conditions.
* Use separation of variables to solve the one-dimensional heat equation.

This theory note should provide a comprehensive understanding of heat conduction principles, formulas, and problem-solving techniques required for the GATE CS exam.