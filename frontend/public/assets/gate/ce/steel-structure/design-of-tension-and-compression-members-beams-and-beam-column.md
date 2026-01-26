**Design of Tension and Compression Members, Beams and Beam-Columns**
===========================================================

### Introduction

This note covers the theoretical aspects of designing tension and compression members, beams, and beam-columns with a focus on steel structures. The concepts covered are based on IS 800:2007.

### Core Concepts

#### **Tension Members**

Tension members in steel structures are subjected to axial forces that tend to elongate or compress them. The design of tension members involves determining their strength against rupture under these forces.

*   **Ultimate Strength**: This is the maximum tensile stress a material can withstand without failing.
*   **Elastic Limit**: This is the maximum stress up to which a material will return to its original shape when the load is removed.

#### **Compression Members**

Compression members in steel structures are also subjected to axial forces but tend to compress rather than elongate. The design of compression members involves determining their strength against buckling under these forces.

*   **Euler's Buckling Load**: This is the critical load beyond which a column or beam will buckle.
*   **Slenderness Ratio**: This ratio determines the likelihood of a member buckling. It is defined as the length to diameter (or width) ratio.

#### **Beams**

Beams in steel structures are subjected to transverse loads that cause bending moments, shearing forces, and deflections. The design of beams involves determining their strength against failure under these actions.

*   **Bending Moment**: This is the moment causing a beam to bend.
*   **Shear Force**: This is the force tending to shear a beam.

#### **Beam-Columns**

Beam-columns in steel structures are subjected to both bending and axial loads. The design of beam-columns involves determining their strength against failure under these combined actions.

### Key Formulas/Theorems

**Tension Members:**

*   $$\sigma_u = \frac{P}{A}$$
    *   Where $\sigma_u$ is the ultimate tensile stress, $P$ is the axial force, and $A$ is the cross-sectional area.
*   $$f_{ut} = \frac{\sqrt{P}}{A}$$
    *   Where $f_{ut}$ is the allowable tensile stress.

**Compression Members:**

*   $$P_e = \frac{\pi^2 EI}{l^2}$$
    *   Where $P_e$ is Euler's critical load, $E$ is Young's modulus, $I$ is the moment of inertia, and $l$ is the length.
*   $$f_{c} = \frac{P_e}{A}$$
    *   Where $f_c$ is the allowable compressive stress.

**Beams:**

*   $$M = \frac{WL}{2}$$
    *   Where $M$ is the bending moment, $W$ is the load, and $L$ is the length.
*   $$V = W$$
    *   Where $V$ is the shear force.

**Beam-Columns:**

*   $$\sigma_{bc} = \frac{P}{A} + f_M$$
    *   Where $\sigma_{bc}$ is the allowable stress for beam-columns, $f_M$ is the bending moment factor.
*   $$f_{bc} = \frac{\sqrt{P}}{A} + f_M$$
    *   Where $f_{bc}$ is the allowable stress for beam-columns.

### Problem Solving Patterns

1.  **Determine the type of member**: Identify whether it's a tension member, compression member, beam, or beam-column.
2.  **Calculate loads and stresses**: Use formulas to determine the axial force, bending moment, shear force, and allowable stresses.
3.  **Apply design codes**: Use IS 800:2007 for steel structures to determine the design capacity.

### Examples with Solutions

**Example 1**

A tension member is subjected to an axial force of 100 kN. The cross-sectional area is 10 cm^2. Determine the allowable tensile stress.

$$f_{ut} = \frac{\sqrt{P}}{A} = \frac{\sqrt{100,000}}{10} = 31.62 \text{ N/mm}^2$$

**Example 2**

A compression member is subjected to an axial force of 50 kN. The moment of inertia is 50 cm^4 and the length is 2 m. Determine Euler's critical load.

$$P_e = \frac{\pi^2 EI}{l^2} = \frac{\pi^2 \times 200,000 \times 50}{(2)^2} = 4909.6 \text{ kN}$$

**Example 3**

A beam is subjected to a bending moment of 20 kNm and a shear force of 10 kN. Determine the allowable stresses.

$$f_M = \frac{M}{Z} = \frac{20,000}{100} = 200 \text{ N/mm}^2$$
$$\sigma_{bc} = f_c + f_M = 250 + 200 = 450 \text{ N/mm}^2$$

### Common Pitfalls

1.  **Forgetting to apply design codes**: Always refer to IS 800:2007 for steel structures.
2.  **Ignoring the type of member**: Determine whether it's a tension member, compression member, beam, or beam-column before calculating loads and stresses.

### Quick Summary

*   Tension members are subjected to axial forces that tend to elongate them.
*   Compression members are subjected to axial forces that tend to compress them.
*   Beams are subjected to transverse loads causing bending moments, shear forces, and deflections.
*   Beam-columns are subjected to both bending and axial loads.

This comprehensive theory note covers all the necessary concepts for designing tension and compression members, beams, and beam-columns with a focus on steel structures. It includes detailed explanations of principles, formulas, examples, and common pitfalls. By following this guide, students should be well-prepared to tackle any question related to these topics.