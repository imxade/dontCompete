# Mass Transfer
================

## Introduction
---------------

Mass transfer refers to the movement of mass from one phase to another, often involving a change of state (e.g., solid-liquid, liquid-gas). This topic is crucial in chemical engineering, particularly in processes like drying, evaporation, and separation.

## Core Concepts
-----------------

### Mass Transfer Mechanisms

There are two primary mechanisms:

1.  **Diffusion**: Random movement of molecules due to thermal energy.
2.  **Convection**: Bulk flow of a fluid carrying mass with it.

### Fick's Law of Diffusion

Describes the rate of diffusion: $J = -D \frac{dC}{dx}$

*   $J$ is the molar flux (mol/m²s)
*   $D$ is the diffusion coefficient
*   $\frac{dC}{dx}$ is the concentration gradient

### Mass Transfer Coefficients

Used to describe the rate of mass transfer in various scenarios:

*   **Diffusion coefficient** ($D$): for diffusive transport
*   **Convection coefficient** (h): for convective transport

## Key Formulas/Theorems
-------------------------

### Drying Rate Equations

For constant and falling rate regimes:

1.  $N = k_a (C_s - C_m)$ (constant rate)
2.  $\frac{dC}{dt} = \frac{k_f A \rho_p (C_i - C)}{\pi r^2}$ (falling rate)

*   $N$ is the drying rate
*   $k_a$, $k_f$ are mass transfer coefficients
*   $A$ is surface area, $\rho_p$ is particle density

### Reverse Osmosis Criterion

For equilibrium to prevail: $\pi_1 - p_1 = \pi_2 + p_2$

## Problem Solving Patterns
---------------------------

*   Identify the mass transfer mechanism (diffusion, convection)
*   Apply relevant formulas and equations
*   Consider boundary conditions and initial conditions

### Examples with Solutions

**Example 1:** Batch drying experiment

Given:

*   Initial moisture content: 0.35 kg H₂O/kg dry solid
*   Final moisture content: 0.1 kg H₂O/kg dry solid
*   Drying time: 5h
*   Constant rate regime: $N = \frac{2}{2} \, \text{kg} \, \text{H}_2\text{O}/(\text{m}^2 \text{h})$

Find the mass of dry solid per unit area.

**Solution**

1.  Calculate the total moisture removed: $0.35 - 0.1 = 0.25$ kg H₂O/kg dry solid
2.  Apply Fick's Law for constant rate regime:
    $J = \frac{dN}{dt} = k_a (C_s - C_m)$
3.  Substitute values and solve for $k_a$:
    $\frac{dN}{dt} = \frac{0.25}{5} = k_a (0 - 0.1)$
4.  Use the result to find the mass of dry solid per unit area: $\rho_p = \frac{m_d}{A}$

**Example 2:** Reverse Osmosis

Given:

*   Feed side: $p_1$, $\pi_1$
*   Permeate side: $p_2$, $\pi_2$

Find the criterion for equilibrium to prevail.

**Solution**

Apply the reverse osmosis criterion:
$\pi_1 - p_1 = \pi_2 + p_2$

## Common Pitfalls
------------------

*   Misapplication of mass transfer equations and formulas
*   Failure to consider boundary conditions and initial conditions
*   Inadequate attention to units and dimensional analysis

## Quick Summary
---------------

*   Mass transfer mechanisms: diffusion, convection
*   Fick's Law of Diffusion
*   Mass transfer coefficients (diffusion coefficient, convection coefficient)
*   Drying rate equations (constant and falling rate regimes)
*   Reverse Osmosis criterion
*   Problem solving patterns: identify mechanism, apply relevant formulas, consider boundary conditions