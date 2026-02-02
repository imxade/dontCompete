**Thermal Properties of Pure Substance**
=====================================

**Introduction**
---------------

The thermal properties of a pure substance are a crucial aspect of thermodynamics, which studies the relationships between heat, work, and energy. In this section, we will delve into the concepts related to enthalpy, partial molar enthalpy, and infinite dilution.

**Core Concepts**
-----------------

### Enthalpy (H)

Enthalpy is a measure of the total energy of a system, including internal energy (U) and the product of pressure (P) and volume (V). It is defined as:

$$H = U + PV$$

### Partial Molar Enthalpy (Ḣx)

Partial molar enthalpy represents the change in enthalpy when one mole of a component is added to a solution, while keeping the amount of other components constant. For a binary liquid system with components 1 and 2:

$$H_x = \left( \frac{\partial H}{\partial n_x} \right)_{T,P,n_{i \neq x}}$$

### Infinite Dilution (χ)

At infinite dilution, the concentration of one component approaches zero. The partial molar enthalpy at infinite dilution is denoted as Ḣx∞.

**Key Formulas/Theorems**
-------------------------

LaTeX formulas will be used to represent mathematical expressions:

* Enthalpy: $H = U + PV$
* Partial Molar Enthalpy: $\frac{\partial H}{\partial n_x} = \left( \frac{\partial (U + PV)}{\partial n_x} \right)_{T,P,n_{i \neq x}}$
* Infinite Dilution: $\lim_{x \to 0} \frac{\partial H}{\partial n_x}$

**Problem Solving Patterns**
---------------------------

When solving problems related to thermal properties of pure substances, follow these steps:

1.  Identify the type of problem (e.g., calculating partial molar enthalpy).
2.  Use the relevant formula or theorem from the core concepts section.
3.  Apply boundary conditions and limits as necessary.

**Examples with Solutions**
---------------------------

### Example 1: Calculating Partial Molar Enthalpy

Given a binary liquid system:

$$H = \frac{40}{x_1} + \frac{60}{x_2}$$

Find the partial molar enthalpy of species 1 at infinite dilution.

```markdown
## Step 1: Identify the formula for partial molar enthalpy.
$\left( \frac{\partial H}{\partial n_x} \right)_{T,P,n_{i \neq x}} = \left( \frac{\partial (U + PV)}{\partial n_x} \right)_{T,P,n_{i \neq x}}$

## Step 2: Apply the formula to the given system.
$\left( \frac{\partial H}{\partial n_1} \right)_{T,P,n_{i \neq 1}} = \frac{40}{x_1^2}$

## Step 3: Evaluate at infinite dilution.
$\lim_{x_1 \to 0} \left( \frac{\partial H}{\partial n_1} \right)_{T,P,n_{i \neq 1}} = 42$
```

The final answer is $\boxed{42}$.

### Example 2: Thermodynamics Question (Q1)

Given the enthalpy expression:

$$H = \frac{40}{x_1^2} + \frac{60}{x_2^2}$$

Find the partial molar enthalpy of species 1 at infinite dilution.

```markdown
## Step 1: Identify the formula for partial molar enthalpy.
$\left( \frac{\partial H}{\partial n_x} \right)_{T,P,n_{i \neq x}} = \left( \frac{\partial (U + PV)}{\partial n_x} \right)_{T,P,n_{i \neq x}}$

## Step 2: Apply the formula to the given system.
$\left( \frac{\partial H}{\partial n_1} \right)_{T,P,n_{i \neq 1}} = \frac{40}{x_1^2}$

## Step 3: Evaluate at infinite dilution.
$\lim_{x_1 \to 0} \left( \frac{\partial H}{\partial n_1} \right)_{T,P,n_{i \neq 1}} = 42$
```

The final answer is $\boxed{42}$.

**Common Pitfalls**
-------------------

*   Failing to apply the correct formula or theorem.
*   Misinterpreting boundary conditions and limits.
*   Overlooking the distinction between partial molar enthalpy and infinite dilution.

**Quick Summary**
-----------------

*   Enthalpy (H) = U + PV
*   Partial Molar Enthalpy (Ḣx) = ∂H/∂nx at constant T, P, and ni ≠ x
*   Infinite Dilution (χ): Ḣx∞ = lim(x→0) ∂H/∂nx

This comprehensive theory note covers all the necessary concepts and formulas to tackle questions related to thermal properties of pure substances. It is essential to understand these principles to excel in thermodynamics problems, especially those involving enthalpy, partial molar enthalpy, and infinite dilution.