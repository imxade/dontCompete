**Reaction Kinetics**
=====================

**Introduction**
---------------

Reaction kinetics is a branch of chemical engineering that deals with the study of rates and mechanisms of chemical reactions. It is essential to understand reaction kinetics as it helps in designing and optimizing chemical reactors, which are critical components in various industries such as petroleum refining, chemical processing, and pharmaceutical manufacturing.

**Core Concepts**
-----------------

### Reaction Rate

The rate of a chemical reaction is defined as the change in concentration of reactants or products per unit time. It can be expressed mathematically as:

$$\text{Reaction rate} = \frac{\Delta C}{\Delta t}$$

where $\Delta C$ is the change in concentration and $\Delta t$ is the change in time.

### Order of Reaction

The order of a reaction refers to the dependence of the reaction rate on the concentration of reactants. It can be expressed mathematically as:

$$\text{Rate} = k [A]^n [B]^m \cdots$$

where $k$ is the rate constant, $[A]$ and $[B]$ are the concentrations of reactants A and B, respectively, and $n$ and $m$ are the orders of reaction.

### Rate Constant

The rate constant ($k$) is a measure of the frequency at which reactant molecules collide and result in a chemical reaction. It depends on the temperature, pressure, and catalysts present in the system.

**Key Formulas/Theorems**
-------------------------

*   Reaction rate equation:

$$\text{Rate} = k [A]^n [B]^m \cdots$$

*   Integrated rate laws for first-order reactions:

$$\ln \frac{[A]}{[A]_0} = - kt$$

*   Integrated rate laws for second-order reactions:

$$\frac{1}{[A]} = \frac{1}{[A]_0} + kt$$

**Problem Solving Patterns**
---------------------------

### Segregated Model

The segregated model is a mathematical approach used to describe the behavior of non-ideal reactors. It assumes that the reactants are perfectly mixed, but there is a distribution of residence times within the reactor.

### Residence Time Distribution (RTD)

The RTD curve represents the probability distribution of residence times in the reactor. It can be obtained experimentally using tracer experiments or calculated theoretically using models such as the plug flow model and the backmix model.

**Examples with Solutions**
---------------------------

Q1: An irreversible liquid-phase second-order reaction $A \rightleftharpoons B$ has a rate constant $k = 0.2 \, \text{L} \, \text{mol}^{-1} \, \text{min}^{-1}$ at a concentration of pure $A$ equal to $1.5 \, \text{mol} \, \text{L}^{-1}$. The segregated model mimics the non-ideality of this reactor. If the residence time distribution (RTD) curve for this reactor is given as:

|  | RTD Curve |
| --- | --- |
| Rectangle i | $0 < t < 5$ min |
| Rectangle ii | $5 < t < 10$ min |
| Rectangle iii | $10 < t < 15$ min |

Calculate the percentage conversion of $A$ at the exit of the reactor.

Solution:

1.  Area under RTD curve = $\int_0^{\infty} E(t) \, dt$
2.  Given that the areas of rectangles (i), (ii), and (iii) are equal, we can write:

$$\text{Area of Rectangle i} = \frac{5}{15} \times 1 = \frac{1}{3}$$

$$\text{Area of Rectangle ii} = \frac{5}{15} \times \frac{2}{3} = \frac{2}{9}$$

$$\text{Area of Rectangle iii} = \frac{5}{15} \times \frac{4}{9} = \frac{4}{27}$$
3.  Total area under RTD curve:

$$E(t) = \frac{\delta (t-5)}{2} + \frac{\delta (t-10)}{3} + \frac{\delta (t-15)}{4}$$

where $\delta$ is the Dirac delta function.
4.  We can calculate the area under RTD curve by integrating over time:

$$\int_0^{\infty} E(t) \, dt = \left[ t \right]_5^{10} + \frac{1}{3} \left[ t \right]_{10}^{15}$$

$$= 5 + \frac{5}{9} = \frac{50}{9}$$
5.  Percentage conversion of $A$ at the exit of the reactor is given by:

$$\text{Percentage Conversion} = X C _{\text{out}} = 1 - \frac{k C_A^2 t_{\text{out}}}{[A]_0^2}$$

where $k$, $C_A$, and $t_{\text{out}}$ are the rate constant, concentration of $A$, and residence time at the exit of the reactor, respectively.
6.  Given that:

$$k = 0.2 \, \text{L} \, \text{mol}^{-1} \, \text{min}^{-1}$$

$$C_A = 1.5 \, \text{mol} \, \text{L}^{-1}$$

$$t_{\text{out}} = 15 \, \text{min}$$

we can calculate the percentage conversion of $A$ at the exit of the reactor:

$$X C _{\text{out}} = 1 - \frac{0.2 \times (1.5)^2 \times 15}{(1.5)^2} = 1 - \frac{0.45}{1.5} = 0.7$$

Therefore, the percentage conversion of $A$ at the exit of the reactor is $\boxed{71\%}$.

**Common Pitfalls**
------------------

*   Students often miss the fact that the areas under the RTD curve are equal.
*   They may also confuse the residence time distribution (RTD) with the reaction rate equation.

**Quick Summary**
-----------------

*   Reaction kinetics deals with the study of rates and mechanisms of chemical reactions.
*   The segregated model is a mathematical approach used to describe the behavior of non-ideal reactors.
*   Residence time distribution (RTD) curve represents the probability distribution of residence times in the reactor.
*   Percentage conversion of $A$ at the exit of the reactor can be calculated using the rate constant, concentration of $A$, and residence time.