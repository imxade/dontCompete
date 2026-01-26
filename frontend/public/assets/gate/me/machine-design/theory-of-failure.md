# Theory of Failure
======================

## Introduction
---------------

The theory of failure deals with understanding how machines and structures fail under various loads, stresses, and strains. It's essential for engineers to design safe and reliable systems. This note covers the fundamental concepts related to the theory of failure.

## Core Concepts
-----------------

### Von-Mises Stress

Von-Mises stress is a measure of the three-dimensional stress state at a point in a material. It is proportional to the square root of the distortional strain energy per unit volume. Mathematically, it can be represented as:

$$\sigma_{VM} = \sqrt{\frac{1}{2}\left[\left(\sigma_1-\sigma_2\right)^2 + \left(\sigma_2-\sigma_3\right)^2 + \left(\sigma_3-\sigma_1\right)^2\right]}$$

where $\sigma_1$, $\sigma_2$, and $\sigma_3$ are the principal stresses.

### Strain Energy

Strain energy is a measure of the energy stored in a material due to deformation. It can be categorized into two types:

*   **Distortional strain energy**: This type of energy is responsible for the distortion or bending of the material.
*   **Dilatational strain energy**: This type of energy is responsible for the expansion or contraction of the material.

## Key Formulas/Theorems
-------------------------

### Strain Energy Per Unit Volume

The strain energy per unit volume can be represented as:

$$U = \frac{1}{2}\left[\sigma_{11}^2 + \sigma_{22}^2 + \sigma_{33}^2 + 2\sigma_{12}^2 + 2\sigma_{23}^2 + 2\sigma_{31}^2\right]$$

### Von-Mises Stress in Terms of Strain Energy

Von-Mises stress is proportional to the square root of the distortional strain energy per unit volume:

$$\sigma_{VM} = \sqrt{\frac{1}{2}\left[\left(\sigma_1-\sigma_2\right)^2 + \left(\sigma_2-\sigma_3\right)^2 + \left(\sigma_3-\sigma_1\right)^2\right]}$$

## Problem Solving Patterns
---------------------------

### Identifying Principal Stresses

To determine the principal stresses, we need to diagonalize the stress tensor. This involves finding the eigenvalues and eigenvectors of the stress tensor.

### Calculating Strain Energy

To calculate the strain energy per unit volume, we need to know the stress components at each point in the material. We can then use the formula for strain energy per unit volume.

## Examples with Solutions
---------------------------

### Example 1: Von-Mises Stress Calculation

Given:

*   Principal stresses: $\sigma_1 = 100$ MPa, $\sigma_2 = -50$ MPa, and $\sigma_3 = 0$

We need to calculate the Von-Mises stress.

Solution:
$$\sigma_{VM} = \sqrt{\frac{1}{2}\left[\left(\sigma_1-\sigma_2\right)^2 + \left(\sigma_2-\sigma_3\right)^2 + \left(\sigma_3-\sigma_1\right)^2\right]}$$
$$= \sqrt{\frac{1}{2}\left[\left(100-(-50)\right)^2 + \left((-50)-0\right)^2 + \left(0-100\right)^2\right]}$$
$$= \sqrt{\frac{1}{2}\left[150^2+50^2+100^2\right]}$$
$$= \sqrt{\frac{1}{2}\left[22500+2500+10000\right]}$$
$$= \sqrt{\frac{1}{2}\left[42500\right]}$$
$$= 204.14$$ MPa

### Example 2: Strain Energy Calculation

Given:

*   Stress components: $\sigma_{11} = 100$ MPa, $\sigma_{22} = -50$ MPa, and $\sigma_{33} = 0$
*   Poisson's ratio: $\nu = 0.3$

We need to calculate the strain energy per unit volume.

Solution:
$$U = \frac{1}{2}\left[\sigma_{11}^2 + \sigma_{22}^2 + \sigma_{33}^2 + 2\sigma_{12}^2 + 2\sigma_{23}^2 + 2\sigma_{31}^2\right]$$
$$= \frac{1}{2}\left[100^2+(-50)^2+0^2+2(\nu)\sigma_{11}\sigma_{22}+2(\nu)\sigma_{22}\sigma_{33}+2(\nu)\sigma_{33}\sigma_{11}\right]$$
$$= \frac{1}{2}\left[10000+2500+0+2(0.3)(100)(-50)+2(0.3)(-50)0+2(0.3)0(100)\right]$$
$$= \frac{1}{2}\left[12500-3000\right]$$
$$= 4700$$ MPa

## Common Pitfalls
------------------

*   Confusing the types of strain energy (distortional vs dilatational).
*   Incorrectly calculating the principal stresses.
*   Forgetting to consider the Poisson's ratio in calculations.

## Quick Summary
---------------

*   Von-Mises stress is proportional to the square root of the distortional strain energy per unit volume.
*   Strain energy can be categorized into two types: distortional and dilatational.
*   To calculate the Von-Mises stress, we need to know the principal stresses.
*   To calculate the strain energy per unit volume, we need to know the stress components.

This comprehensive note covers all theoretical concepts related to the theory of failure. By following this guide, you should be able to solve problems and understand the underlying principles.