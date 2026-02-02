# Numerical Ability: General Aptitude
## Introduction
Numerical Ability (NA) section of GATE CS exam tests the candidate's problem-solving skills and ability to apply mathematical concepts to solve real-world problems. This note focuses on one of the previous year questions related to Production Engineering, specifically Orthogonal Cutting Operation.

## Core Concepts
In an orthogonal cutting operation, a single-point cutting tool is used to remove material from a workpiece. The cutting force and friction force are acting on the chip, which causes deformation and shear stress in the material. The rake angle of the cutting tool affects the shear plane and hence the cutting forces.

### Shear Force and Friction
The shear force $F_s$ can be calculated using the following formula:

$$ F_s = \frac{F_c}{\sin(\phi)} $$

where $F_c$ is the cutting force, $\phi$ is the friction angle, which is related to the rake angle $\alpha$ by:

$$ \tan(\phi) = \cot(\alpha) $$

## Key Formulas/Theorems
- Cutting Force: $F_c = F_{\text{normal}} + F_{\text{tangential}}$
- Shear Force: $F_s = \frac{F_c}{\sin(\phi)}$

## Problem Solving Patterns
1. Identify the type of cutting tool used (single-point or multi-point).
2. Calculate the friction angle $\phi$ from the given rake angle $\alpha$.
3. Determine the cutting force $F_c$ and its components.
4. Apply the formula for shear force using the calculated values.

## Examples with Solutions

### Example 1: Given
- Rake angle, $\alpha = 12^{\circ}$
- Cutting Force, $F_c = 1000 N$
- Friction Force, $F_f = 600 N$
- Chip Thickness, $t_c = 1.5 mm$
- Uncut Chip Thickness, $t_{\text{uncut}} = 0.75 mm$

### Solution
First, calculate the friction angle:

$$ \tan(\phi) = \cot(12^{\circ}) $$

Using a calculator or trigonometric table, we find $\tan(\phi)$ and then solve for $\phi$.

Next, calculate the shear force using the formula:

$$ F_s = \frac{F_c}{\sin(\phi)} $$

Substitute the given values and round off to two decimal places as instructed.

## Common Pitfalls
- Students often confuse the cutting force with friction force or vice versa.
- Failure to correctly calculate the friction angle from the rake angle can lead to incorrect shear forces.

## Quick Summary

*   Understand the concept of orthogonal cutting operation and its key parameters (rake angle, cutting force, friction force).
*   Calculate the friction angle using the rake angle.
*   Apply the formula for shear force using the calculated values.
*   Be cautious with the units and rounding off instructions.

This comprehensive note should equip you to tackle similar questions in the future.