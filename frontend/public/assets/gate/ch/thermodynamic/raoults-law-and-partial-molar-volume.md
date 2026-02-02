# Raoult's Law and Partial Molar Volume
## Introduction
Raoult's law describes the relationship between the vapor pressure of a solution and the mole fraction of its components. Partial molar volume, on the other hand, is a concept in thermodynamics that deals with the contribution of each component to the total volume of a mixture.

## Core Concepts

### Raoult's Law
Raoult's law states that the partial vapor pressure of a component in a solution is directly proportional to its mole fraction. Mathematically, this can be expressed as:

$$p_i = p_{i}^*x_i \tag{1}$$

where $p_i$ is the partial vapor pressure of component i, $p_{i}^*$ is the vapor pressure of pure component i, and $x_i$ is the mole fraction of component i.

### Partial Molar Volume
The partial molar volume of a component in a mixture is the change in the total volume of the mixture when one mole of that component is added to it. Mathematically, this can be expressed as:

$$\overline{V}_i = \left( \frac{\partial V}{\partial n_i} \right)_{T,P,n_j} \tag{2}$$

where $\overline{V}_i$ is the partial molar volume of component i, $n_i$ is the number of moles of component i, and $n_j$ represents all other components in the mixture.

## Key Formulas/Theorems
- Raoult's law: $p_i = p_{i}^*x_i$
- Partial molar volume: $\overline{V}_i = \left( \frac{\partial V}{\partial n_i} \right)_{T,P,n_j}$

## Problem Solving Patterns
1. **Mole Fraction Calculation**: When given partial vapor pressures, use Raoult's law to calculate the mole fraction of a component.
   ```mermaid
   graph LR
     A[Partial Vapor Pressures] --> B[Raoult's Law]
     B --> C[Mole Fractions]
   ```
2. **Partial Molar Volume Calculation**: When given total volumes and compositions, use partial molar volume formulas to calculate the partial molar volumes of components.

## Examples with Solutions
### Example 1: Raoult's Law Application

Suppose we have a binary solution consisting of components A and B. Given that the vapor pressure of pure A is $p_{A}^* = 10$ atm, the partial vapor pressure of component A in the solution is $p_A = 5$ atm. If the mole fraction of component A in the solution is $x_A$, use Raoult's law to find $x_A$.

```latex
\begin{align*}
p_A &= p_{A}^* x_A \\
&= 10 \cdot x_A \\
p_A &= 5
\end{align*}

\begin{align*}
10 x_A &= 5 \\
x_A &= \frac{1}{2} = 0.5
\end{align*}
```

### Example 2: Partial Molar Volume Application

Given a binary mixture of components A and B with total volume $V$, partial molar volume $\overline{V}_A$ of component A is given by:

$$\left(\frac{\partial V}{\partial n_A}\right)_{T,P,n_B} = \overline{V}_A = 20 cm^3/mol$$

Find the change in total volume when one mole of B is added to the mixture.

```latex
\begin{align*}
\Delta V &= \left(\frac{\partial V}{\partial n_A}\right)_{T,P,n_B} - \left(\frac{\partial V}{\partial n_B}\right)_{T,P,n_A} \\
&= \overline{V}_A - (-15 cm^3/mol) \\
&= 20 + 15 = 35 cm^3
\end{align*}
```

## Common Pitfalls

- Failing to account for the mole fraction in Raoult's law applications.
- Confusing partial molar volume with total molar volume.

## Quick Summary

### Key Points to Remember:
- **Raoult's Law**: $p_i = p_{i}^*x_i$
- **Partial Molar Volume**: $\overline{V}_i = \left( \frac{\partial V}{\partial n_i} \right)_{T,P,n_j}$