# Effective Stress and Permeability Theory Note
==============================================

## Introduction
---------------

Effective stress and permeability are crucial concepts in geotechnical engineering, particularly in understanding fluid flow through porous media. The effective stress is the stress that causes deformation of a soil or rock mass, while permeability measures the ease with which fluids can flow through it.

## Core Concepts
-----------------

### Effective Stress

The concept of effective stress was introduced by Karl Terzaghi to describe the state of stress in a saturated porous medium. It is defined as:

$$\sigma' = \sigma - u$$

where $\sigma$ is the total stress, $u$ is the pore water pressure, and $\sigma'$ is the effective stress.

The effective stress is responsible for causing deformation of the soil or rock mass under external loads. In a saturated medium, the pore water pressure can reduce the effective stress, leading to settlement or liquefaction.

### Permeability

Permeability measures the ability of fluids to flow through a porous medium. It depends on the properties of the fluid and the medium itself. The Darcy's law relates the permeability $k$ to the seepage velocity:

$$v = -\frac{k}{\mu} \nabla p$$

where $\mu$ is the dynamic viscosity of the fluid, and $\nabla p$ is the pressure gradient.

### Anisotropic vs. Isotropic Conditions

In isotropic conditions, the permeability in all directions is equal ($k_H = k_V$). In anisotropic conditions, the permeability varies with direction ($k_H \neq k_V$).

## Key Formulas/Theorems
-------------------------

### Flow Net for Anisotropic Condition

When dealing with an anisotropic medium, we need to draw a flow net that takes into account the different permeabilities in horizontal and vertical directions. To do this, we scale the embedment depth of the wall by a factor:

$$\text{Scaling Factor} = \sqrt{\frac{k_H}{k_V}}$$

### Steady-State Flow Equations

For steady-state flow through an unconfined aquifer, we can use Darcy's law to relate the discharge rate $Q$ to the hydraulic conductivity $K$, drawdowns $h_{10}$ and $h_{100}$:

$$Q = \frac{2\pi K h_{10} (h_{10} - h_{100})}{\log \left(\frac{r_1}{r_0}\right)}$$

where $r_1$ is the distance from the pumping well to the first observation well, and $r_0$ is the distance from the pumping well to the second observation well.

## Problem Solving Patterns
---------------------------

### Effective Stress

*   Identify the external loads acting on the soil or rock mass.
*   Determine the pore water pressure distribution in the medium.
*   Calculate the effective stress using the formula $\sigma' = \sigma - u$.
*   Use the effective stress to determine the settlement or deformation of the medium.

### Permeability

*   Identify the type of fluid and porous medium involved.
*   Determine the permeability using Darcy's law or other relevant formulas.
*   Consider anisotropic conditions if applicable.
*   Apply the flow net scaling factor to adjust for anisotropy.

## Examples with Solutions
---------------------------

### Example 1: Effective Stress

A vertical sheet pile wall is installed in an anisotropic soil. Given:

*   Coefficient of horizontal permeability $k_H = 10^{-4}$ m/s
*   Coefficient of vertical permeability $k_V = 5 \times 10^{-6}$ m/s
*   Embedment depth of the wall $L = 20$ m

Find the scaling factor for drawing a flow net:

$$\text{Scaling Factor} = \sqrt{\frac{k_H}{k_V}} = \sqrt{\frac{10^{-4}}{5 \times 10^{-6}}} = \sqrt{2}$$

### Example 2: Permeability

A 30 cm diameter well is drilled into an unconfined aquifer. Given:

*   Hydraulic conductivity $K = 10$ m/day
*   Drawdowns:
	+ First observation well at 10 m from the pumping well, $h_{10} = 5$ m
	+ Second observation well at 100 m from the pumping well, $h_{100} = 1$ m

Find the corresponding pumping rate:

$$Q = \frac{2\pi K h_{10} (h_{10} - h_{100})}{\log \left(\frac{r_1}{r_0}\right)} = \frac{2\pi \times 10 \times 5 \times (5-1)}{\log \left(\frac{10}{100}\right)} = 1857.64$$

## Common Pitfalls
-------------------

*   Failing to account for anisotropic conditions in permeability.
*   Not using the correct flow net scaling factor when dealing with anisotropy.
*   Incorrectly applying Darcy's law or other formulas for fluid flow.

## Quick Summary
-----------------

*   Effective stress is defined as $\sigma' = \sigma - u$.
*   Permeability depends on fluid and medium properties, described by Darcy's law.
*   Anisotropic conditions require scaling the embedment depth of walls using $\sqrt{\frac{k_H}{k_V}}$.
*   Steady-state flow through unconfined aquifers is governed by $Q = \frac{2\pi K h_{10} (h_{10} - h_{100})}{\log \left(\frac{r_1}{r_0}\right)}$.