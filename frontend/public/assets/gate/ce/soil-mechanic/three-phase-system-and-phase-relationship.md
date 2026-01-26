**Three-Phase System and Phase Relationship**
=============================================

### Introduction

In geotechnical engineering, a three-phase system refers to a system comprising of soil, water, and air. Understanding the relationship between these phases is crucial for designing and analyzing various geotechnical structures such as dams, tunnels, and foundations.

### Core Concepts

*   **Hydrostatic Pressure**: The pressure exerted by a fluid (water) at equilibrium due to its weight.
*   **Coefficient of Friction**: A dimensionless quantity representing the ratio of the force required to initiate motion between two surfaces to the normal force acting on those surfaces.
*   **Uplift Pressure**: The upward pressure exerted by water on a submerged structure, such as a dam.

### Key Formulas/Theorems

*   **Hydrostatic Pressure Formula**:
    \[ p = \rho g h \]
    where $p$ is the hydrostatic pressure, $\rho$ is the fluid density, $g$ is the acceleration due to gravity, and $h$ is the height of the fluid column.
*   **Coefficient of Friction Formula**: Not directly applicable in this context. However, it's essential for understanding the relationship between the dam and foundation soil.

### Problem Solving Patterns

1.  **Assess the System**: Identify the phases involved (soil, water, air) and their boundaries.
2.  **Determine the Type of Pressure**: Identify whether the problem involves hydrostatic pressure, uplift pressure, or frictional forces.
3.  **Apply Relevant Formulas**: Use the appropriate formulas to calculate pressures, stresses, or forces acting on the structure.

### Examples with Solutions

**Example 1: Hydrostatic Pressure Calculation**

A dam holds 10 m of static water as shown in the figure (not drawn to scale). Calculate the hydrostatic pressure at a depth of 5 m below the water surface.

```mermaid
graph LR
    A[Water Surface] --> B[Depth = 5 m]
    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style B fill:#ff0,stroke:#333,stroke-width:2px;
```

\[ p = \rho g h = (1000\; \text{kg/m}^3) (9.81\; \text{m/s}^2) (5\; \text{m}) = 49050\; \text{Pa} \]

**Example 2: Uplift Pressure Calculation**

A concrete dam holds 10 m of static water as shown in the figure (not drawn to scale). The uplift pressure is assumed to vary linearly from full hydrostatic head at the heel, to zero at the toe of the dam. Calculate the minimum base width required for a NO-sliding condition.

```mermaid
graph LR
    A[Heel] --> B[Toe]
    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style B fill:#ff0,stroke:#333,stroke-width:2px;
```

\[ p = \rho g h \]

For a NO-sliding condition:

\[ p \leq \mu N \]
where $\mu$ is the coefficient of friction between the dam and foundation soil, and $N$ is the normal force acting on the base.

The uplift pressure varies linearly from full hydrostatic head at the heel to zero at the toe. Therefore, the minimum base width required can be calculated as:

\[ B = \frac{\rho g h}{\mu N} \]

Substituting the given values:

\[ B = \frac{(1000\; \text{kg/m}^3) (9.81\; \text{m/s}^2) (10\; \text{m})}{(0.45) (3.24 \times 10^3\; \text{kN/m}^2)} = 15.873\; \text{m} \]

### Common Pitfalls

*   Failing to identify the type of pressure involved in a problem.
*   Incorrectly applying formulas or making calculation errors.

### Quick Summary

*   Three-phase system: soil, water, and air
*   Hydrostatic pressure formula: $p = \rho g h$
*   Coefficient of friction:
*   Uplift pressure varies linearly from full hydrostatic head to zero.
*   Minimum base width required for a NO-sliding condition can be calculated using the uplift pressure and coefficient of friction.

Note: This note is created based on the provided source questions. Additional examples and explanations may be necessary to ensure comprehensive coverage.