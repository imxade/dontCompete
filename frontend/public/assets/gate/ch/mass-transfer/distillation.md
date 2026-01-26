**Distillation**
================

**Introduction**
---------------

Distillation is a mass transfer process used to separate mixtures of liquids based on differences in their boiling points. It involves heating a mixture to produce vapor, which is then condensed and collected as a pure component.

**Core Concepts**
-----------------

*   **Relative Volatility**: The ratio of the partial pressure of a component to its mole fraction in the liquid phase.
*   **Batch Distillation**: A type of distillation where a fixed quantity of feed mixture is charged into a still, and the distillate is collected as it vaporizes.

**Key Formulas/Theorems**
------------------------

### Rayleigh Equation

The Rayleigh equation relates the composition of the remaining liquid to the composition of the distillate:

$$\frac{x_F}{x_W} = \alpha \left( 1 - \frac{F}{W} \right)$$

where $x_F$ is the mole fraction of component A in the feed, $x_W$ is the mole fraction of component A in the still, $\alpha$ is the relative volatility, $F$ is the amount of distillate collected, and $W$ is the initial amount of liquid.

### Solution of Rayleigh Equation

To solve for the composition of the remaining liquid ($x_W$), we can rearrange the Rayleigh equation:

$$\frac{x_F}{x_W} = \alpha \left( 1 - \frac{F}{W} \right)$$

$$\frac{x_W}{x_F} = \frac{1}{\alpha} + \frac{F}{\alpha W}$$

Taking the natural logarithm of both sides:

$$\ln \left( \frac{x_W}{x_F} \right) = \ln \left( \frac{1}{\alpha} \right) + \ln \left( 1 + \frac{F}{\alpha W} \right)$$

Simplifying and solving for $x_W$:

$$x_W = x_F e^{\ln \left( \frac{1}{\alpha} \right) + \ln \left( 1 + \frac{F}{\alpha W} \right)}$$

### Relative Volatility

The relative volatility is given by:

$$\alpha = \frac{P_A}{x_A}$$

where $P_A$ is the partial pressure of component A and $x_A$ is its mole fraction in the liquid phase.

**Problem Solving Patterns**
---------------------------

*   Apply the Rayleigh equation to solve for the composition of the remaining liquid.
*   Use the relative volatility to determine the separation efficiency.
*   Analyze the effect of variables such as temperature, pressure, and feed composition on the distillation process.

**Examples with Solutions**
-------------------------

### Example 1

A batch still is used to separate a binary mixture of components A and B. The initial charge is 1 kmol, and the initial and final amounts of component A are 0.1 kmol and 0.01 kmol, respectively. The relative volatility is 4.5.

*   Calculate the mole fraction of component B remaining in the vessel.
*   Solution:
    *   Apply the Rayleigh equation to solve for the composition of the remaining liquid:

$$\frac{x_F}{x_W} = \alpha \left( 1 - \frac{F}{W} \right)$$

    *   Substitute values and simplify:

$$\frac{0.1}{x_W} = 4.5 \left( 1 - \frac{0.01}{1} \right)$$

$$x_W = \frac{0.1}{4.5 \times 0.99}$$

    *   Calculate the mole fraction of component B remaining in the vessel:

$$y_B = 1 - x_A = 1 - \frac{0.01}{1} = 0.99$$

### Example 2

A batch still is used to separate a binary mixture of components A and B. The initial charge is 2 kmol, and the relative volatility is 3.

*   Calculate the amount of distillate collected (F) if the mole fraction of component A in the still is 0.2.
*   Solution:
    *   Apply the Rayleigh equation to solve for the composition of the remaining liquid:

$$\frac{x_F}{x_W} = \alpha \left( 1 - \frac{F}{W} \right)$$

    *   Substitute values and simplify:

$$\frac{0.2}{x_W} = 3 \left( 1 - \frac{F}{2} \right)$$

    *   Calculate the amount of distillate collected (F):

$$F = \frac{\frac{0.2}{x_W} + 2}{3}$$

**Common Pitfalls**
------------------

*   Incorrect application of the Rayleigh equation.
*   Failure to consider the effect of relative volatility on separation efficiency.

**Quick Summary**
-----------------

*   Distillation is a mass transfer process used to separate mixtures of liquids based on differences in their boiling points.
*   The Rayleigh equation relates the composition of the remaining liquid to the composition of the distillate.
*   Relative volatility is an important parameter in determining separation efficiency.

Note: This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve the given source questions.