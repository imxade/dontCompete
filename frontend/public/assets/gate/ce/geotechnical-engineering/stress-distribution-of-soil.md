**Stress Distribution of Soil**
==========================

### Introduction

Stress distribution in soil is a fundamental concept in geotechnical engineering, which deals with the behavior and properties of soils under various types of loading. In this note, we will focus on the Boussinesq's problem, which is a classic problem in soil mechanics that describes the stress distribution in a half-space due to a surface load.

### Core Concepts

* **Boussinesq's Problem**: A mathematical problem that describes the stress distribution in a half-space (infinite extent) due to a surface load.
* **Half-Space**: An infinite domain with zero stress at infinity.
* **Surface Load**: A force applied to the surface of the half-space.

### Key Formulas/Theorems

The expression for vertical stress $\sigma_z$ at any point $(r, z)$ within the half-space is given by:

$$\sigma_z = \frac{3P}{2\pi}\left(1 + \frac{z^3}{r^5}\right)$$

where $P$ is the surface load, $r$ is the radial distance from the point of application of the load to the point in question, and $z$ is the depth with downward direction taken as positive.

### Problem Solving Patterns

* **Maximization**: At any given $r$, there is a variation of $\sigma_z$ along $z$. To find the maximum value of $\sigma_z$ at a specific $z$, we need to differentiate the expression for $\sigma_z$ with respect to $z$ and set it equal to zero.
* **Locus of Maximum**: The locus of the maximum $\sigma_z$ can be found by setting the derivative of $\sigma_z$ with respect to $z$ equal to zero and solving for $r$.

### Examples with Solutions

**Example 1**

Find the locus of the maximum $\sigma_z$.

$$\frac{\partial \sigma_z}{\partial z} = \frac{3P}{2\pi}\left(\frac{3z^2}{r^5}\right)$$

Setting this equal to zero and solving for $r$, we get:

$$r^5 = \frac{z^3}{1/4}$$
$$r = z^{5/3}$$

This is the locus of the maximum $\sigma_z$.

**Example 2**

Given $P = 20kN/m^2$, $\gamma_{sat} = 1706kPa$, $\nu_q = 0.35$, $\gamma_w = 10kN/m^3$, and $q = 58N$. Find the vertical stress at a depth of $z = 1m$.

$$\sigma_z = \frac{3P}{2\pi}\left(1 + \frac{z^3}{r^5}\right)$$

Since we don't have the value of $r$, let's assume it to be equal to the distance from the point of application of the load. We need more information about the configuration of the problem to solve for $r$.

### Common Pitfalls

* **Incorrect Differentiation**: When finding the locus of maximum $\sigma_z$, students often forget to differentiate the expression with respect to $z$.
* **Lack of Units**: Students often neglect to include units in their calculations, leading to incorrect answers.

### Quick Summary

* Boussinesq's problem: describes stress distribution in a half-space due to surface load
* Key formulas:
	+ $\sigma_z = \frac{3P}{2\pi}\left(1 + \frac{z^3}{r^5}\right)$
	+ Locus of maximum: $r = z^{5/3}$
* Problem-solving patterns:
	+ Maximization
	+ Differentiation with respect to $z$

Note: The answer to Q1 is indeed (A).