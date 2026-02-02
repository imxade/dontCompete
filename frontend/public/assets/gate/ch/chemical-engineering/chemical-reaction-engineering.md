# Chemical Reaction Engineering
======================================================

## Introduction
Chemical reaction engineering deals with the development of a chemical process to achieve the desired product yield, selectivity, and efficiency. It involves understanding the kinetics of chemical reactions, reactor design, and process optimization.

## Core Concepts
--------------------------------------------------------

### Stoichiometry
Stoichiometry is the study of the quantitative relationships between reactants and products in a chemical reaction. It is essential for designing reactors and predicting product yields.

#### Law of Conservation of Mass
The law states that matter cannot be created or destroyed, only transformed from one form to another. This implies that the total mass of reactants equals the total mass of products.

#### Stoichiometric Coefficients
Stoichiometric coefficients are numerical values assigned to each species in a chemical equation. They represent the ratio of moles of a particular species consumed or produced during a reaction.

### Kinetics
Kinetics is the study of the rates at which chemical reactions occur. It helps predict the conversion of reactants, product formation, and selectivity.

#### Reaction Rate Equation
The rate of a chemical reaction is given by:

$$r = k \cdot C_A^m \cdot C_B^n \cdots$$

where:
- $r$ is the reaction rate,
- $k$ is the reaction constant,
- $C_A$, $C_B$, ... are concentrations of reactants A, B, ...,
- $m$, $n$, ... are orders of reaction with respect to each reactant.

### Reactor Design
Reactor design involves selecting a reactor type and size based on factors like efficiency, cost, safety, and environmental impact.

#### Types of Reactors
1. **Batch Reactor**: A batch reactor is used for small-scale production where the reactants are added at once, and the reaction is allowed to proceed until completion.
2. **Continuous Stirred Tank Reactor (CSTR)**: A CSTR is used for large-scale production where the reactants are continuously fed into the reactor, and the products are continuously removed.

## Key Formulas/Theorems
--------------------------------------------------------

### Stoichiometric Coefficient Formula
The stoichiometric coefficient of a species can be calculated using the following formula:

$$\text{Stoichiometric coefficient} = \frac{\text{Moles of species}}{\text{Moles of limiting reactant}}$$

where:
- Moles of species are moles of the particular species present in the reaction,
- Moles of limiting reactant are moles of the limiting reactant.

### Reaction Rate Equation Formula
The rate of a chemical reaction is given by:

$$r = k \cdot C_A^m \cdot C_B^n \cdots$$

where:
- $r$ is the reaction rate,
- $k$ is the reaction constant,
- $C_A$, $C_B$, ... are concentrations of reactants A, B, ...,
- $m$, $n$, ... are orders of reaction with respect to each reactant.

## Problem Solving Patterns
--------------------------------------------------------

### Case 1: Stoichiometry Problems
To solve stoichiometry problems, follow these steps:

1. Write the balanced chemical equation.
2. Identify the limiting reactant (or reagent).
3. Calculate the moles of the product formed using the stoichiometric coefficient.

### Example

Problem: In the reaction $A \rightarrow B$, 100 g of A is converted into B. If the molar mass of A is 20 g/mol, calculate the number of moles of B formed.

Solution:

Step 1: Write the balanced chemical equation.
$A \rightarrow B$

Step 2: Identify the limiting reactant (or reagent).
In this case, it's A.

Step 3: Calculate the moles of the product formed using the stoichiometric coefficient.
The reaction is a simple conversion, so there are no coefficients. Therefore:

Number of moles of A = mass of A / molar mass of A
= 100 g / (20 g/mol) = 5 mol

Since one mole of A gives one mole of B, number of moles of B formed = 5 mol.

### Case 2: Kinetics Problems
To solve kinetics problems, follow these steps:

1. Write the reaction rate equation.
2. Identify the order of reaction with respect to each reactant.
3. Calculate the reaction rate using the given values for concentrations and time.

## Examples with Solutions
--------------------------------------------------------

### Example 1

Problem: The reaction $A \rightarrow B$ is first-order with respect to A. If the initial concentration of A is $C_A^0 = 1 M$, calculate the concentration of B at time t, given that:

$$\frac{dC_B}{dt} = k (C_A - C_B)$$

Solution:

Step 1: Write the reaction rate equation.
$\frac{dC_B}{dt} = k (C_A - C_B)$

Step 2: Identify the order of reaction with respect to each reactant.
The reaction is first-order with respect to A.

Step 3: Calculate the concentration of B at time t, using the given initial conditions and the fact that $dC_B/dt$ is constant:

$$\frac{dC_B}{dt} = k (C_A^0 - C_B)$$
Integrating both sides gives:
$$C_B(t) = C_A^0 + (1/k)(C_A^0 - C_B(0))$$

Given that $t=5$ min, we can solve for $C_B(5)$ using this equation.

### Example 2

Problem: The reaction $A \rightarrow B$ is zero-order with respect to A. If the initial concentration of A is $C_A^0 = 1 M$, calculate the time taken for $50\%$ conversion, given that:

$$r = k C_A$$

Solution:

Step 1: Write the reaction rate equation.
$r = k C_A$

Step 2: Identify the order of reaction with respect to each reactant.
The reaction is zero-order with respect to A.

Step 3: Calculate the time taken for $50\%$ conversion using the following formula:
$$t = \frac{C_B}{k}$$

Given that $C_A^0=1 M$, we can solve for t by substituting values into this equation.

## Common Pitfalls
--------------------------------------------------------

*   Failing to consider limiting reactants.
*   Incorrectly calculating stoichiometric coefficients.
*   Forgetting to account for changes in concentration with time.

## Quick Summary
-----------------

*   Stoichiometry deals with the quantitative relationships between reactants and products.
*   Kinetics is concerned with the rates at which chemical reactions occur.
*   Reactor design involves selecting a reactor type and size based on efficiency, cost, safety, and environmental impact.