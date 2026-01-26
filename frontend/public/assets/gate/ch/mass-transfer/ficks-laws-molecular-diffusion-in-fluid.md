**Fick's Laws of Molecular Diffusion in Fluids**
=====================================================

**Introduction**
---------------

Fick's laws describe how molecules diffuse through a fluid under certain conditions. These laws are crucial for understanding mass transfer phenomena, which is essential for various engineering applications, including chemical processing and separation.

**Core Concepts**
-----------------

Molecular diffusion occurs due to the random motion of molecules in a fluid. The rate of diffusion depends on several factors:

*   **Concentration gradient**: The difference in concentration between two regions.
*   **Diffusion coefficient (D)**: A measure of how easily molecules can diffuse through a medium.
*   **Steady-state assumption**: In many cases, the system reaches equilibrium where the flux is constant.

Fick's laws are formulated based on these concepts:

### Fick's First Law

The first law describes the rate of diffusion under steady-state conditions:

**Flux = -D \* dC/dx**

where:

*   **Flux (J)**: The mass transfer rate per unit area.
*   **dC/dx**: The concentration gradient.
*   **D**: Diffusion coefficient.

LaTeX rendering:
$$ J=-D\frac{dC}{dx} $$

### Fick's Second Law

The second law accounts for non-steady-state conditions:

**∂C/∂t = D \* ∂²C/∂x²**

This equation describes how the concentration changes with time.

LaTeX rendering:
$$ \frac{\partial C}{\partial t} = D\frac{\partial^2 C}{\partial x^2} $$

**Key Formulas/Theorems**
-------------------------

### Partial Pressure and Concentration Relationship

For ideal gases, we can use the following relationship:

**p = RT \* C**

where:

*   **p**: Partial pressure.
*   **R**: Universal gas constant.
*   **T**: Temperature in Kelvin.
*   **C**: Molar concentration.

LaTeX rendering:
$$ p=RT\cdot C $$

### Flux and Concentration Relationship

For Fick's first law, the flux can be rewritten as:

**J = -D \* (p2/p1)**

where:

*   **J**: Flux.
*   **D**: Diffusion coefficient.
*   **p1** and **p2**: Partial pressures at opposite sides of a film.

LaTeX rendering:
$$ J=-D\frac{p_2}{p_1} $$

**Problem Solving Patterns**
---------------------------

When solving mass transfer problems, follow these steps:

1.  Identify the type of problem (steady-state or non-steady-state).
2.  Determine the relevant laws and formulas.
3.  Apply boundary conditions and solve for unknown variables.

### Example: Steady-State Flux

Suppose we want to find the steady-state flux of SO₂ through a film with given properties:

*   **D**: Diffusion coefficient = 1 × 10⁻⁵ m² s⁻¹.
*   **p1** and **p2**: Partial pressures at opposite sides of the film are 0.15 bar and 0.05 bar, respectively.

Using Fick's first law, we can find the flux:

**J = -D \* (p2/p1)**
= -(1 × 10⁻⁵ m² s⁻¹) \* (0.05/0.15)
≈ 3.33 × 10⁻⁶ mol m⁻² s⁻¹

**Examples with Solutions**
---------------------------

### Example 1: Wet Air Drying

Consider the wet air drying problem described in source question Q1:

Wet air containing 10 mole percent water vapor is dried by passing it through a column of CaCl₂ pellets. The pellets remove 50% of water from the wet air entering the column.

Let's analyze this problem using Fick's laws:

*   **Initial concentration**: 10 mol % water vapor.
*   **Final concentration**: Unknown, but we can find it by applying the mass balance equation:
    **m_f = m_i - (m_i \* r)**
    where:
        *   **m_f**: Final amount of water vapor.
        *   **m_i**: Initial amount of water vapor.
        *   **r**: Removal efficiency (50% in this case).
        
    Solving for **m_f**, we get:
    
    ```python
    m_f = 0.5 * m_i
    ```

*   We can now find the final concentration:

```python
final_concentration = m_f / total_mol
```

where **total_mol** is the total number of moles in the air.

Plugging in values, we get:

```python
m_i = 10 mol (water vapor)
total_mol = 100 mol (air)

m_f = 0.5 * m_i = 5 mol (water vapor)

final_concentration = m_f / total_mol ≈ 0.05
```

Therefore, the final concentration of water vapor is approximately 5%.

**Common Pitfalls**
------------------

*   **Incorrect application of Fick's laws**: Make sure to use the correct formula for steady-state or non-steady-state conditions.
*   **Miscalculation of concentrations**: Double-check your units and calculations when finding concentrations.

**Quick Summary**
-----------------

*   **Fick's laws** describe molecular diffusion under steady-state and non-steady-state conditions.
*   **Key formulas** include the flux-concentration relationship and partial pressure-concentration relationship.
*   **Problem-solving patterns** involve identifying problem types, applying relevant laws and formulas, and solving for unknown variables.

By following this comprehensive theory note, you'll be well-prepared to tackle mass transfer problems involving Fick's laws of molecular diffusion.