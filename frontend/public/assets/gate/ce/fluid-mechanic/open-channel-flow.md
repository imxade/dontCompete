**Open Channel Flow**
=====================

**Introduction**
---------------

Open channel flow refers to the movement of fluids through channels with a free surface, such as rivers, canals, or pipes. This topic deals with the principles and laws governing the behavior of fluids in open channels.

**Core Concepts**
-----------------

### 1. Manning's Formula

The most commonly used formula for calculating the discharge of fluid flow in an open channel is Manning's equation:

$$Q = \frac{1}{n}AR^{2/3}S^{1/2}$$

where:
- $Q$ is the discharge (m³/s)
- $A$ is the cross-sectional area of the channel (m²)
- $R$ is the hydraulic radius (m)
- $S$ is the bed slope of the channel (dimensionless)

Manning's roughness coefficient ($n$) is a measure of the roughness of the channel surface and is typically in the range of 0.01 to 0.05.

### 2. Critical Depth

The critical depth is the maximum depth at which the flow becomes supercritical. It can be calculated using:

$$y_c = \frac{Q^{2/3}}{C^2}$$

where:
- $y_c$ is the critical depth (m)
- $Q$ is the discharge (m³/s)
- $C$ is the Chezy's coefficient (m²/s)

### 3. Hydraulic Jump

A hydraulic jump occurs when a supercritical flow suddenly becomes subcritical, resulting in a sudden increase in depth and velocity. The minimum Froude number for a hydraulic jump to occur is:

$$Fr_{min} = \frac{1}{\sqrt{2}}$$

**Key Formulas/Theorems**
-------------------------

### 1. Discharge (Manning's Formula)

$$Q = \frac{1}{n}AR^{2/3}S^{1/2}$$

### 2. Critical Depth

$$y_c = \frac{Q^{2/3}}{C^2}$$

### 3. Hydraulic Jump

$$Fr_{min} = \frac{1}{\sqrt{2}}$$

**Problem Solving Patterns**
---------------------------

*   Calculate the discharge using Manning's formula.
*   Determine the critical depth for a given flow rate and Chezy's coefficient.
*   Identify if a hydraulic jump will occur by calculating the Froude number.

**Examples with Solutions**
---------------------------

### 1. Example 1

A rectangular channel is 4.0 m wide and carries a discharge of $Q$ = 3.2 m³/s with a depth of $y$ = 0.4 m. The channel transitions to a maximum width contraction at a downstream location, without influencing the upstream flow conditions.

Using Manning's formula, we can calculate the discharge:

$$Q = \frac{1}{n}AR^{2/3}S^{1/2}$$

Assuming $n$ = 0.01 and $S$ = 0.001 (slope of 1:1000), we get:

$$R = \frac{A}{P} = \frac{4y^2}{4 + 2y}$$

Substituting values, we get:

$$R = 1.33 m$$

Now,

$$Q = \frac{1}{0.01}(4)(1.33)^{2/3}(0.001)^{1/2} = 3.16 m^3/s$$

Since $Q_{given}$ = 3.2 m³/s, the maximum contraction width can be calculated:

$$W_{max} = \frac{4y^2}{(4 + 2y)R^{2/3}}$$

Substituting values, we get:

$$W_{max} = 3.35 m$$

### 2. Example 2

A round-bottom triangular lined canal is to be laid at a slope of 1 in 1500, to carry a discharge of $Q$ = 32.5 m³/s. The side slopes of the canal cross-section are to be kept at 1.25H : 1V.

Using Manning's formula, we can calculate the critical depth:

$$y_c = \frac{Q^{2/3}}{C^2}$$

Assuming $C$ = 150 m/s (Chezy's coefficient), we get:

$$y_c = \frac{(32.5)^{2/3}}{(150)^2} = 0.94 m$$

Now, using the side slope ratio, we can calculate the maximum depth:

$$H_{max} = y_c + \frac{V}{1.25}$$

Assuming $V$ = $\sqrt{2gH}$ (velocity), we get:

$$H_{max} = 0.94 + \frac{\sqrt{2(9.81)(0.94)}}{1.25} = 1.02 m$$

Since the flow depth is less than the maximum depth, it will be in the range of 2.39 to 2.42 m.

### 3. Example 3

A spillway has unit discharge of $q$ = 7.5 m³/s/m. The flow depth at the downstream horizontal apron is $y_d$ = 0.5 m.

Using the hydraulic jump theory, we can calculate the minimum Froude number:

$$Fr_{min} = \frac{1}{\sqrt{2}}$$

Now, using the Bernoulli's equation, we can calculate the velocity at the downstream end:

$$V_d = \sqrt{2g(y_g - y_d)}$$

Assuming $y_g$ = 4 m (tail water depth), we get:

$$V_d = \sqrt{2(9.81)(4 - 0.5)} = 8.38 m/s$$

Now, using the equation for hydraulic jump:

$$Fr_{d} = \frac{V_d}{\sqrt{g(y_g - y_d)}} > Fr_{min}$$

Substituting values, we get:

$$Fr_{d} = 4.56 > \frac{1}{\sqrt{2}} = 0.707$$

Since $Fr_{d}$ is greater than the minimum Froude number, a hydraulic jump will occur.

**Common Pitfalls**
-----------------

*   Not considering the side slopes and bed slope while calculating discharge or critical depth.
*   Assuming Chezy's coefficient as a constant value.
*   Not using Bernoulli's equation to calculate velocity at downstream end for hydraulic jump.

**Quick Summary**
----------------

| Concept | Formula |
| --- | --- |
| Manning's Formula | $Q = \frac{1}{n}AR^{2/3}S^{1/2}$ |
| Critical Depth | $y_c = \frac{Q^{2/3}}{C^2}$ |
| Hydraulic Jump | $Fr_{min} = \frac{1}{\sqrt{2}}$ |

This comprehensive theory note covers the key concepts, formulas, and problem-solving patterns required for open channel flow.