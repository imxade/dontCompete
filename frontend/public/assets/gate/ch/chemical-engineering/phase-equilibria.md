**Phase Equilibria**
====================

**Introduction**
---------------

Phase equilibria refer to the equilibrium between different phases of a system, such as liquid-liquid, vapor-liquid, or solid-liquid. In this topic, we will focus on binary liquid mixtures and the activity coefficient model.

**Core Concepts**
-----------------

### Activity Coefficient Model

The activity coefficient model is used to describe the behavior of a binary liquid mixture. It relates the activity (or fugacity) of each component in the mixture to its mole fraction. The excess Gibbs free energy, G^E, is expressed as:

$$G^E = RT \sum_i x_i \int_0^{x_i} \ln \gamma_i d x_i$$

where R is the gas constant, T is the temperature, and $x_i$ is the mole fraction of component i.

### Excess Gibbs Free Energy Model

The excess Gibbs free energy model is a specific implementation of the activity coefficient model. It assumes that the excess free energy can be represented by a two-parameter equation:

$$G^E = x_1 \phi_{11} x_2^{2} + x_2 \phi_{22} x_1^{2} + \epsilon x_1 x_2$$

where $\phi_{ii}$ and $\epsilon$ are parameters that depend on the specific system.

**Key Formulas/Theorems**
-------------------------

### Activity Coefficient Model

The activity coefficient, γ_i, is related to the mole fraction by:

$$\ln \gamma_i = \frac{\partial G^E}{\partial n_i}$$

where $n_i$ is the number of moles of component i.

**Problem Solving Patterns**
---------------------------

### Plotting Activity Coefficients

When plotting In γ vs. x, we can use the following observations:

* The curve will be concave up for ideal mixtures.
* For non-ideal mixtures, the curve may exhibit positive or negative deviations from ideality.

**Examples with Solutions**
-------------------------

### Example 1: Plotting Activity Coefficients

Suppose we are given a binary liquid mixture of components A and B. We want to plot In γ_A vs. x_A at a temperature of 298 K.

Given:

* Excess Gibbs free energy model parameters: ϕ_AA = 0.5, ϕ_BB = 1.2, ε = -0.3
* Initial guess for mole fraction x_A = 0.5

Solution:
```latex
\begin{align*}
\ln \gamma_A &amp;= \frac{\partial G^E}{\partial n_A} \\
&amp;= \phi_{AA} x_B^2 + \epsilon x_B \\
\end{align*}
```
Using the given parameters and initial guess, we can evaluate the derivative at x_A = 0.5 to obtain:

$$\ln \gamma_A \approx -0.3 \cdot 0.5 = -0.15$$

Plotting In γ vs. x, we can see that the curve is concave up.

**Common Pitfalls**
-------------------

* Failing to account for non-ideal behavior.
* Incorrectly assuming ideal mixtures.

**Quick Summary**
-----------------

* Activity coefficient model relates activity to mole fraction.
* Excess Gibbs free energy model parameters depend on specific system.
* Plotting activity coefficients can reveal non-ideal behavior.
* Common pitfalls include incorrect assumptions about ideality.

Note: This is a basic outline, and you may need to add or modify sections based on the specific requirements of your exam.