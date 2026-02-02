**Differential Levelling**
=========================

### Introduction
-----------------

Differential levelling is a technique used to determine the difference in elevation between two points on the Earth's surface. It involves measuring the differences in height between consecutive benchmarks (BM) using a leveling instrument and staff. This method is widely used in geomatics engineering for surveying, mapping, and construction projects.

### Core Concepts
------------------

#### Principle of Levelling

The principle of levelling states that "the difference in elevation between two points is equal to the sum of the differences in elevation between consecutive benchmarks." In other words, the leveling instrument measures the distance between the staff and the BM, and this distance represents the difference in elevation.

#### Reduced Level (RL)

Reduced level is a datum used as a reference for measuring elevations. It is the elevation of a point relative to a benchmark with a known elevation. The RL is usually measured in meters above or below a specific benchmark.

### Key Formulas/Theorems
-------------------------

$$\text{Difference in elevation} = \sum_{i=1}^{n} (\text{FS}_i - \text{BS}_i)$$

where $\text{FS}$ is the fore sight reading and $\text{BS}$ is the back sight reading.

### Problem Solving Patterns
---------------------------

1.  **Identify consecutive benchmarks**: Determine which points are consecutive benchmarks.
2.  **Measure differences in elevation**: Measure the difference in elevation between each pair of consecutive benchmarks using the leveling instrument and staff.
3.  **Calculate total difference in elevation**: Calculate the total difference in elevation by summing up the differences measured at each benchmark.

### Examples with Solutions
---------------------------

**Example 1:**

Suppose we have two points, P and R, and we want to find the reduced level of point R relative to a benchmark with an RL of +200.000 m.

| Point | Staff Readings (m) |
| --- | --- |
| P    | -2.050            |
| Q    | 1.050             |
| R    | -1.655            |

To find the reduced level of point R, we need to calculate the total difference in elevation between points P and R.

$$\text{Difference in elevation} = \sum_{i=1}^{3} (\text{FS}_i - \text{BS}_i)$$

$$\text{Difference in elevation} = (-2.050 + 1.050) + (1.050 - 0.950) + (0.950 - (-1.655))$$

$$\text{Difference in elevation} = -1.000 + 1.100 + 2.605 = 3.705 \text{ m}$$

Since the reduced level of point P is +200.000 m, the reduced level of point R is:

$$\text{RL of R} = \text{RL of P} + \text{Difference in elevation}$$

$$\text{RL of R} = 200.000 + (-3.705) = 196.295 \text{ m}$$

### Common Pitfalls
-------------------

*   **Incorrectly identifying consecutive benchmarks**: Make sure to identify the correct consecutive benchmarks.
*   **Forgetting to sum up differences in elevation**: Remember to calculate the total difference in elevation by summing up the differences measured at each benchmark.

### Quick Summary
------------------

*   The principle of levelling states that the difference in elevation between two points is equal to the sum of the differences in elevation between consecutive benchmarks.
*   Reduced level (RL) is a datum used as a reference for measuring elevations.
*   To calculate the total difference in elevation, sum up the differences measured at each benchmark.

Note: This theory note is based on the source question provided and may not cover all possible topics or questions related to differential levelling.