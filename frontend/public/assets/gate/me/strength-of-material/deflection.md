**Theory Note: Deflection**
==========================

**Introduction**
---------------

Deflection in the context of Strength of Materials refers to the amount by which a beam or structural element deviates from its original straight-line path under an applied load. Understanding deflection is crucial for designing safe and efficient structures.

**Core Concepts**
-----------------

### What causes Deflection?

*   External loads (e.g., weight, moment)
*   Material properties:
    *   Flexural rigidity ($EI$)
    *   Young's modulus
*   Beam geometry:
    *   Length ($L$)
    *   Cross-sectional area

**Key Formulas/Theorems**
------------------------

### Moment-Area Theorem

The moment-area theorem relates the deflection of a beam to the area under its bending moment diagram.

$$\frac{M}{EI} = \frac{1}{R} + \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{M}{EI}\right)$$

where $R$ is the radius of curvature, and $\mathrm{d}/\mathrm{d}x$ denotes differentiation with respect to the beam's length.

### Bending Moment Diagrams

Bending moment diagrams (BMDs) represent the distribution of bending moments along a beam. A BMD can be constructed by:

1.  Calculating the internal forces at each point
2.  Integrating these forces over the beam's length

**Problem Solving Patterns**
---------------------------

### Strategy for Source Question Q1 (ID: me\_2021-M\_6)

To solve this question, apply the moment-area theorem and the formula for deflection due to an end moment:

$$\delta = \frac{M L^2}{24 EI}$$

Compare the given options with the derived expression.

**Examples with Solutions**
---------------------------

### Example 1: Deflection of a Simply Supported Beam

A simply supported beam has a length $L$, a flexural rigidity $EI$, and an end load $P$. Find the deflection at mid-span.

Assuming small deflections, use the following formula:

$$\delta = \frac{PL^3}{48 EI}$$

**Common Pitfalls**
-------------------

### Missing units or dimensions in calculations

Ensure that all quantities have consistent units and are correctly dimensioned when applying formulas.

### Incorrect application of boundary conditions

Verify that boundary conditions (e.g., fixed, simply supported) are properly accounted for in the solution.

### **Quick Summary**
---------------

*   Deflection is a measure of beam deviation under load.
*   Flexural rigidity ($EI$), length ($L$), and material properties influence deflection.
*   Moment-area theorem relates deflection to bending moment diagrams.
*   Bending moment diagrams are constructed by integrating internal forces over the beam's length.

**Sources:**

GATE 2021 (Forenoon Session) Mechanical Engineering PAGE 11

Note: The above theory note is written in Markdown format and includes LaTeX equations, Mermaid diagrams (not used here), and a concise structure to facilitate easy revision and comprehension of the topic.