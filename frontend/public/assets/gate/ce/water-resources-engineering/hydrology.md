**Hydrology**
================

### Introduction
-----------------

Hydrology is the scientific study of the movement, distribution, and quality of water on Earth's surface and beneath it. It encompasses various aspects of water resources engineering, including precipitation, runoff, infiltration, evaporation, and groundwater flow.

### Core Concepts
------------------

#### Muskingum Method
The Muskingum method is a hydrologic channel routing technique used to calculate the outflow from a river or stream segment based on the inflow and stage (water level) at the upstream end of the segment. It assumes that the flow in each reach can be represented by a linear equation.

#### Triangular Direct Runoff Hydrograph
A triangular direct runoff hydrograph is a graph showing the rate of runoff as a function of time during a storm event. The area under the curve represents the total volume of water discharged from the catchment.

#### Probability of Flood Occurrence
The probability of flood occurrence can be estimated using the flood frequency analysis method. This involves analyzing historical data on flood events and relating them to their return periods (e.g., 1-year, 10-year, 50-year floods).

### Key Formulas/Theorems
--------------------------------

#### Muskingum Method
$$
\begin{aligned}
Q_2 &= K \left( X_1 + nX_2 + m \Delta S \right) \\
Q_1 - Q_0 &= K \left( m \Delta S + X_1 \right)
\end{aligned}
$$

where:
- $Q$ is the outflow,
- $X$ is the stage (water level),
- $K$, $m$, and $n$ are parameters to be determined.

#### Triangular Direct Runoff Hydrograph
The area under the curve of a triangular direct runoff hydrograph can be calculated as:

$$
A = \frac{1}{2} (P - T) R
$$

where:
- $A$ is the area,
- $P$ is the peak flow rate,
- $T$ is the time base.

#### Probability of Flood Occurrence
The probability of a flood not occurring in a given period can be estimated using the Weibull distribution:

$$
p = 1 - \left( 1 + \frac{t}{\theta} \right)^{-k}
$$

where:
- $p$ is the probability,
- $t$ is the time period,
- $\theta$ and $k$ are parameters to be determined.

### Problem Solving Patterns
---------------------------------

*   Use the Muskingum method for hydrologic channel routing.
*   Apply the triangular direct runoff hydrograph to calculate the area under the curve.
*   Analyze historical data on flood events to estimate their return periods.
*   Use the Weibull distribution to calculate the probability of a flood not occurring.

### Examples with Solutions
---------------------------

#### Example 1: Muskingum Method
Suppose we have a river segment with the following parameters:
- $K$ = 2,
- $m$ = 0.5,
- $n$ = 0.3.
Given that the inflow is 100 m³/s and the stage at the upstream end is 5 m, calculate the outflow using the Muskingum method.

```latex
Q_2 &= K \left( X_1 + nX_2 + m \Delta S \right) \\
&= 2 (5 + 0.3 \cdot 5 + 0.5 \cdot 100) \\
&= 270\,m³/s
```

#### Example 2: Triangular Direct Runoff Hydrograph
Suppose we have a storm event with the following parameters:
- Peak flow rate $P$ = 60 m³/s,
- Time base $T$ = 90 hours.
Given that the catchment area is 300 km², calculate the area under the curve of the triangular direct runoff hydrograph.

```latex
A &= \frac{1}{2} (P - T) R \\
&= \frac{1}{2} (60 - 90) 300 \\
&= 13500\,km³
```

### Common Pitfalls
----------------------

*   Incorrect application of the Muskingum method.
*   Misinterpretation of the triangular direct runoff hydrograph.
*   Inadequate analysis of historical data on flood events.

### Quick Summary
-----------------

| Concept | Key Formula/Theorem |
| --- | --- |
| Muskingum Method | $Q_2 = K \left( X_1 + nX_2 + m \Delta S \right)$ |
| Triangular Direct Runoff Hydrograph | $A = \frac{1}{2} (P - T) R$ |
| Probability of Flood Occurrence | $p = 1 - \left( 1 + \frac{t}{\theta} \right)^{-k}$ |

Note: This is a Markdown document, so it may not render correctly in all environments.