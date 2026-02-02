**Engineering Hydrology: Infiltration**
=====================================

### Introduction
-----------------

Infiltration is a crucial aspect of engineering hydrology, representing the process by which water from precipitation or surface runoff seeps into the soil. Understanding infiltration is vital for predicting stormwater runoff, designing drainage systems, and estimating groundwater recharge.

### Core Concepts
------------------

*   **Rainfall Intensity**: The rate at which rain falls over a specific area.
*   **Storm Duration**: The length of time it takes for a storm to pass over a catchment.
*   **Infiltration Capacity**: The maximum rate at which water can infiltrate the soil.

### Key Formulas/Theorems
---------------------------

The W-Index formula is used to calculate the infiltration excess:

$$P = \frac{1}{4} \times \left( I_2^2 + 20I_2 + 40 \right)$$

where $P$ is the total infiltration and $I_n$ represents the rainfall intensity at time $n$ (in mm/hour).

### Problem Solving Patterns
-----------------------------

To solve problems involving infiltration, follow these steps:

1.  **Determine Rainfall Intensity**: Identify the rainfall intensity values for each time interval.
2.  **Apply W-Index Formula**: Use the given formula to calculate the total infiltration based on the rainfall intensities.
3.  **Calculate Infiltration Excess**: Subtract the direct runoff depth from the calculated total infiltration.

### Examples with Solutions
---------------------------

**Example 1:**

Given a 12-hour storm, a direct runoff depth of 100 mm, and the following rainfall intensity values (in mm/hour):

| Time | Rainfall Intensity |
| --- | --- |
| $t_0$ | 20 |
| $t_2$ | 10 |
| $t_3$ | 5 |

Calculate the $\phi$-index of the storm.

**Solution:**

1.  Apply the W-Index formula:

$$P = \frac{1}{4} \times (I_2^2 + 20I_2 + 40)$$

Substitute $I_2 = 10$ into the equation:

$$P = \frac{1}{4} \times (100 + 200 + 40)$$

$$P = \frac{1}{4} \times 340$$

$$P = 85$$

Calculate the total infiltration excess by subtracting the direct runoff depth from $P$:

$$\text{Infiltration Excess} = P - \text{Direct Runoff Depth}$$

$$\text{Infiltration Excess} = 85 - 100$$

$$\text{Infiltration Excess} = -15$$

Since the infiltration excess cannot be negative, recalculate $P$ using the correct formula:

$$P = \frac{1}{4} \times (I_2^2 + 20I_2 + 40)$$

Substitute $I_2 = 10$ into the equation:

$$P = \frac{1}{4} \times (100 + 200 + 40)$$

Since this gives a negative value, we must have made an error in our calculation.

Looking at the formula more closely, we see that if $I_2 < 20$, then the term $(20I_2)$ will be less than $400$. Since all other terms are positive, this implies that the entire product is less than $1200$ and so $P < 300$. This means that the infiltration excess must also be negative.

However, we are given that the direct runoff depth is greater than the total infiltration. Therefore, our previous answer was incorrect, and the correct solution should have been:

$$\text{Infiltration Excess} = P - \text{Direct Runoff Depth}$$

$$\text{Infiltration Excess} = 85 + 100$$

This is impossible, since we are given that direct runoff depth is greater than total infiltration.

The correct solution must have been:

$$P = \frac{1}{4} \times (I_2^2 + 20I_2 + 40)$$

Substitute $I_3 = 5$ into the equation:

$$P = \frac{1}{4} \times (25 + 100 + 40)$$

$$P = \frac{165}{4}$$

Calculate the total infiltration excess by subtracting the direct runoff depth from $P$:

$$\text{Infiltration Excess} = P - \text{Direct Runoff Depth}$$

$$\text{Infiltration Excess} = \frac{165}{4} - 100$$

$$\text{Infiltration Excess} = \frac{65}{4}$$

The $\phi$-index is calculated as the ratio of infiltration excess to total rainfall:

$$\phi = \frac{\text{Infiltration Excess}}{\text{Total Rainfall}}$$

$$\phi = \frac{\frac{65}{4}}{100 + 85}$$

$$\phi = \frac{65}{1850}$$

### Common Pitfalls
-------------------

*   Incorrectly applying the W-Index formula.
*   Failing to consider the correct rainfall intensity values.
*   Not subtracting the direct runoff depth from the total infiltration.

### Quick Summary
------------------

*   Infiltration is the process by which water seeps into the soil.
*   The W-Index formula calculates the total infiltration based on rainfall intensities.
*   The $\phi$-index represents the ratio of infiltration excess to total rainfall.