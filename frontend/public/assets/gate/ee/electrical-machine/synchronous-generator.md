# Synchronous Generator
=====================================

## Introduction
---------------

A synchronous generator, also known as an alternator, is an electrical machine that converts mechanical energy into electrical energy in the form of alternating current (AC). It consists of a rotor and a stator, with the rotor being driven by a prime mover such as a steam turbine or gas turbine.

## Core Concepts
----------------

### Synchronous Reactance

Synchronous reactance ($X_s$) is the opposition to the flow of current in a synchronous generator due to its magnetic field. It is measured in ohms and is an important parameter in determining the performance of the generator.

### Armature Resistance

Armature resistance is the resistance of the stator windings, which opposes the flow of current through them. In a synchronous generator with negligible armature resistance, the voltage drop across the armature is zero.

### Terminal Voltage and Induced EMF

The terminal voltage ($V_t$) is the voltage measured at the terminals of the generator, while the induced EMF ($E$) is the voltage induced in the stator windings due to rotation of the rotor. The magnitude of per-phase terminal voltage is given by $A V$, and the magnitude of per-phase induced emf is given by $A E$.

## Key Formulas/Theorems
-------------------------

### Synchronous Impedance

The synchronous impedance ($Z_s$) is given by:

$$ Z_s = \frac{V_t}{I} = R_a + jX_s $$

where $R_a$ is the armature resistance and $X_s$ is the synchronous reactance.

### Terminal Voltage Equation

The terminal voltage equation for a synchronous generator is given by:

$$ V_t = E - IZ_s $$

## Problem Solving Patterns
---------------------------

When solving problems involving synchronous generators, follow these steps:

1.  Determine the type of load connected to the generator (leading or lagging).
2.  Calculate the power factor angle ($\phi$) using the load current and terminal voltage.
3.  Use the terminal voltage equation to relate the terminal voltage, induced EMF, and synchronous impedance.

## Examples with Solutions
---------------------------

### Example 1:

A three-phase cylindrical rotor synchronous generator has a synchronous reactance of $2 \Omega$ and negligible armature resistance. The magnitude of per-phase terminal voltage is $100 V$, and the magnitude of per-phase induced emf is $120 V$. Determine the type of load connected to the generator.

Solution:
The power factor angle can be calculated using the ratio of terminal voltage to induced EMF:

$$ \phi = \cos^{-1} \left( \frac{V_t}{E} \right) = \cos^{-1} \left( \frac{100}{120} \right) = 23.58^{\circ} $$

Since the load current lags behind the terminal voltage, the load is lagging.

### Example 2:

A three-phase cylindrical rotor synchronous generator has a synchronous reactance of $3 \Omega$ and negligible armature resistance. The magnitude of per-phase terminal voltage is $150 V$, and the magnitude of per-phase induced emf is $180 V$. Determine the type of load connected to the generator.

Solution:
The power factor angle can be calculated using the ratio of terminal voltage to induced EMF:

$$ \phi = \cos^{-1} \left( \frac{V_t}{E} \right) = \cos^{-1} \left( \frac{150}{180} \right) = 36.87^{\circ} $$

Since the load current leads ahead of the terminal voltage, the load is leading.

## Common Pitfalls
-------------------

*   Failing to consider the effect of armature resistance on the terminal voltage.
*   Not distinguishing between leading and lagging loads.
*   Ignoring the synchronous reactance when calculating the terminal voltage.

## Quick Summary
----------------

*   Synchronous generator: converts mechanical energy into electrical energy in the form of AC.
*   Synchronous reactance ($X_s$): opposition to current flow due to magnetic field.
*   Armature resistance ($R_a$): negligible in this context.
*   Terminal voltage equation: $V_t = E - IZ_s$
*   Determine load type by calculating power factor angle.