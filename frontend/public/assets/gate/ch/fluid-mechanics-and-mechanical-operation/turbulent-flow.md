**Turbulent Flow**
================

### Introduction
-----------------

Turbulent flow occurs when a fluid (liquid or gas) flows with a high level of turbulence, characterized by chaotic and irregular motion. This type of flow is common in many engineering applications, including pipes, ducts, and channels. In this note, we will explore the key concepts and formulas related to turbulent flow.

### Core Concepts
----------------

#### Reynolds Number (Re)
The Reynolds number is a dimensionless quantity that characterizes the nature of fluid flow. It is defined as:

$$ Re = \frac{\rho u D}{\mu} $$

where $\rho$ is the fluid density, $u$ is the average velocity, $D$ is the pipe diameter, and $\mu$ is the dynamic viscosity.

For turbulent flow, the Reynolds number is typically greater than 4000.

#### Turbulent Flow Regimes
Turbulent flow can be further divided into two regimes:

*   **Laminar-Turbulent Transition**: occurs when the Reynolds number increases, causing the flow to transition from laminar to turbulent.
*   **Fully Developed Turbulent Flow**: occurs when the flow is fully turbulent and has reached a steady state.

### Key Formulas/Theorems
-------------------------

#### Average Velocity Profiles
For fully developed turbulent flow in a pipe of constant diameter, the average velocity profile can be described by:

$$ \frac{u_{avg}}{u_c} = 0.817 $$

where $u_{avg}$ is the average velocity and $u_c$ is the center-line velocity.

#### Reynolds Stress
Reynolds stress is defined as:

$$ -\rho u'v' = \mu_t \frac{\partial u}{\partial y} $$

where $\mu_t$ is the turbulent viscosity, which can be estimated using various models such as the Prandtl model or the mixing length model.

For fully developed turbulent flow, the Reynolds stress averaged over a sufficiently long time is zero everywhere inside the pipe:

$$ \langle -\rho u'v' \rangle = 0 $$

### Problem Solving Patterns
---------------------------

#### Identifying Flow Regimes
To identify whether a flow is laminar or turbulent, use the Reynolds number and compare it to the critical Reynolds number (approximately 4000).

#### Applying Velocity Profiles
Use the average velocity profile equation to determine the ratio of average velocity to center-line velocity.

### Examples with Solutions
---------------------------------

**Example 1: Fully Developed Turbulent Flow**

A fully developed turbulent flow occurs in a pipe with a diameter of 10 cm and an average velocity of 2 m/s. Determine the Reynolds number and the ratio of average velocity to center-line velocity.

Solution:

*   Calculate the Reynolds number using the given values:
    $$ Re = \frac{\rho u D}{\mu} $$
    Since we don't have specific values for $\rho$ and $\mu$, assume a typical value for water: $\rho = 1000 kg/m^3$ and $\mu = 0.001 Pa.s$. Then:
    $$ Re = \frac{1000 \cdot 2 \cdot 0.1}{0.001} = 200,000 $$
*   Use the average velocity profile equation to determine the ratio of average velocity to center-line velocity:

    $$ \frac{u_{avg}}{u_c} = 0.817 $$

**Example 2: Laminar-Turbulent Transition**

A pipe with a diameter of 5 cm carries water at an average velocity of 1 m/s. Determine whether the flow is laminar or turbulent.

Solution:

*   Calculate the Reynolds number using the given values:
    $$ Re = \frac{\rho u D}{\mu} $$
    Since we don't have specific values for $\rho$ and $\mu$, assume a typical value for water: $\rho = 1000 kg/m^3$ and $\mu = 0.001 Pa.s$. Then:
    $$ Re = \frac{1000 \cdot 1 \cdot 0.05}{0.001} = 50,000 $$
*   Compare the calculated Reynolds number to the critical value (approximately 4000):
    Since 50,000 is greater than 4000, the flow is turbulent.

### Common Pitfalls
-----------------

*   Confusing laminar and turbulent flow regimes.
*   Not considering the average velocity profile in fully developed turbulent flow.
*   Failing to account for Reynolds stress in turbulent flows.

### Quick Summary
----------------

*   Turbulent flow occurs at high Reynolds numbers (typically greater than 4000).
*   The average velocity profile for fully developed turbulent flow is given by:
    $$ \frac{u_{avg}}{u_c} = 0.817 $$
*   Reynolds stress averaged over a sufficiently long time is zero everywhere inside the pipe.
*   Be aware of laminar-turbulent transition and apply the appropriate formulas.

Note: This is a comprehensive theory note covering all key concepts, formulas, and insights required to solve the source questions. It includes examples with step-by-step solutions and common pitfalls to watch out for.