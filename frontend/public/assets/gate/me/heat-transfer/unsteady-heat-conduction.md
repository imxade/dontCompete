**Unsteady Heat Conduction**
==========================

### Introduction

Unsteady heat conduction refers to the transfer of heat between a body and its surroundings when there is a change in temperature over time. This concept is crucial in various engineering applications, including thermal design of equipment and systems.

### Core Concepts

When a body is suddenly subjected to a new temperature environment, it takes some time to reach a new steady-state temperature. The rate at which this happens depends on several factors:

1.  **Thermal Properties**: The material's specific heat capacity ($c_p$), thermal conductivity ($k$), and density ($\rho$).
2.  **Geometry**: The shape and size of the body, including its surface area ($A$) and volume ($V$).
3.  **Boundary Conditions**: The temperature of the surrounding environment and any internal or external heat sources.

### Key Formulas/Theorems

*   **Fourier's Law for Unsteady State Conduction**:

    \[
    \frac{\partial T}{\partial t} = \alpha \nabla^2T
    \]

    where $T$ is temperature, $\alpha$ is thermal diffusivity ($\alpha = k / (\rho c_p)$), and $\nabla^2$ is the Laplacian operator.

*   **Biot Number**:

    \[
    Bi = \frac{hL}{k}
    \]

    where $h$ is convective heat transfer coefficient, $L$ is characteristic length, and $k$ is thermal conductivity.

### Problem Solving Patterns

When solving unsteady heat conduction problems using Heisler charts, you need to determine the relevant dimensionless parameters:

*   **Biot Number (Bi)**: Characterizes the ratio of convective to conductive resistances.
*   **Fourier Number (Fo)**: Represents the ratio of time to a characteristic time scale.

### Examples with Solutions

**Example 1:**

A hot steel spherical ball is suddenly dipped into a low-temperature oil bath. Determine the required dimensionless parameters using Heisler charts.

*   **Step 1:** Identify relevant properties:
    *   Steel: $c_p = 500 J/kgK$, $k = 50 W/mK$, $\rho = 8000 kg/m^3$.
    *   Oil bath: Assume uniform temperature ($T_\infty$).
*   **Step 2:** Determine characteristic length and time:
    *   For a sphere, $L = R$ (radius of the ball).
    *   Characteristic time: $\tau = \frac{R^2}{\alpha}$.
*   **Step 3:** Calculate dimensionless parameters:
    *   Biot number: $Bi = \frac{hR}{k}$. Assuming a typical convective coefficient ($h$), calculate Bi.
    *   Fourier number: $Fo = \frac{\tau}{t} = \frac{R^2 / \alpha}{t}$.

**Solution:** Using Heisler charts, the required parameters are indeed **Biot Number (Bi)** and **Fourier Number (Fo)**.

### Common Pitfalls

*   Failing to consider thermal properties of the material.
*   Incorrectly determining characteristic length or time scales.
*   Misinterpreting dimensionless parameter requirements for Heisler charts.

### Quick Summary

*   Unsteady heat conduction involves changes in temperature over time.
*   Relevant parameters include thermal properties, geometry, and boundary conditions.
*   Fourier's Law describes the rate of heat transfer.
*   Dimensionless parameters (Bi and Fo) are crucial for solving problems using Heisler charts.

Note: This is a starting point. I will be happy to make any changes or additions as per your request.