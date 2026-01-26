# Applied Mechanics and Design: Theory Notes

## Introduction
Applied mechanics and design are crucial components of engineering, focusing on the analysis and optimization of mechanical systems. This note covers key concepts related to moments of inertia, strength of materials, beam buckling, and forced vibrations.

## Core Concepts

### Moments of Inertia
The moment of inertia is a measure of an object's resistance to changes in its rotational motion. It depends on the distribution of mass relative to the axis of rotation.

**Properties of Linearly Tapered Section**
Given:
- Height `h(x) = h0 - (h0/h1)x`
where `h0` and `h1` are the initial and final heights, respectively, and `x` is the distance from the origin.
 
The area moment of inertia about the y-axis is given by:

$I_y = \int_{A} x^2 dA$

For a linearly tapered section:
```math
I_y = \frac{h_1}{3}(h_0^3 - h_1^3)
```
**Example Solution**

| Question | Solution |
| --- | --- |
| Q1: Find the area moment of inertia about the y-axis of a linearly tapered section | `3024` |

### Strength of Materials
The strength of materials deals with the properties and behaviors of materials under various types of loads. Key concepts include stress, strain, Young's modulus, and Poisson's ratio.

**Elastic Strain Energy**
Given:
- Length `L = 5 m`
- Cross-sectional area `A = πr^2`
- Density ρ = 2700 kg/m³
- Young's modulus E = 70 GPa

The elastic strain energy stored in a bar under uniaxial tension is given by:

`U = (1/2) \* F^2 / E \* A`

where `F` is the force applied to the bar.

**Example Solution**

| Question | Solution |
| --- | --- |
| Q2: Find the elastic strain energy stored in a cylindrical bar | `57.225 J` |

### Beam Buckling
Beam buckling occurs when an unsupported beam or column fails due to excessive compressive stress. The critical load at which buckling occurs can be calculated using Euler's formula.

**Euler's Formula**
Given:
- `EI`: flexural rigidity of the beam
- `L`: length of the beam
- `P`: critical load

The critical load for a simply supported column is given by:

`P = (π^2 \* EI) / L^2`

**Example Solution**

| Question | Solution |
| --- | --- |
| Q3: Find the value of β that maximizes W to avoid buckling of the beam AB | `0.0924` |

### Forced Vibrations
Forced vibrations occur when a system is subjected to an external periodic force.

**Amplitude of Forced Steady State Response**
Given:
- `x(t)`: displacement of the system at time `t`
- `ωn`: undamped natural frequency of the system
- `ζ`: damping ratio
- `ωr`: forcing frequency

The amplitude of the forced steady state response is given by:

`A = (1 / √(1 + (2ζ\*ωr/ωn)^2))`

**Example Solution**

| Question | Solution |
| --- | --- |
| Q4: Find the peak amplitude of the forced steady state response | `0.0924` |

## Problem Solving Patterns

- **Analytical Methods**: Use mathematical models to derive solutions.
- **Graphical Methods**: Plot curves or diagrams to visualize relationships between variables.

## Examples with Solutions

### Moments of Inertia
| Example | Solution |
| --- | --- |
| Find the area moment of inertia about the y-axis of a linearly tapered section | `3024` |

### Strength of Materials
| Example | Solution |
| --- | --- |
| Find the elastic strain energy stored in a cylindrical bar under uniaxial tension | `57.225 J` |

### Beam Buckling
| Example | Solution |
| --- | --- |
| Find the value of β that maximizes W to avoid buckling of the beam AB | `0.0924` |

### Forced Vibrations
| Example | Solution |
| --- | --- |
| Find the peak amplitude of the forced steady state response | `0.0924` |

## Common Pitfalls

- **Incorrect Units**: Ensure units are consistent throughout calculations.
- **Overlooked Assumptions**: Verify assumptions made in mathematical models.

## Quick Summary
* Moments of Inertia: Area moment of inertia about y-axis for linearly tapered section is `I_y = (h_1/3)(h_0^3 - h_1^3)`.
* Strength of Materials: Elastic strain energy stored in bar under uniaxial tension is `U = (1/2) \* F^2 / E \* A`.
* Beam Buckling: Critical load for simply supported column is given by Euler's formula.
* Forced Vibrations: Amplitude of forced steady state response is `A = (1 / √(1 + (2ζ\*ωr/ωn)^2))`.

---

This comprehensive note covers key concepts in Applied Mechanics and Design, including moments of inertia, strength of materials, beam buckling, and forced vibrations. Each topic includes an example solution to illustrate how to apply the formula or concept. The quick summary provides a concise overview of the main ideas.