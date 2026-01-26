**Hydrograph**
================

### Introduction
---------------

A hydrograph is a graphical representation of the flow rate (discharge) at different times during a flood event or storm runoff. It is an essential tool in engineering hydrology to analyze and predict the behavior of water flows in rivers, streams, and other water bodies.

### Core Concepts
-----------------

#### Definition of Unit Hydrograph
--------------------------------

A unit hydrograph is a graphical representation of the flow rate response of a catchment area to a unit input (e.g., 1 mm of rainfall). It is used to predict the flood hydrographs for different types and intensities of storms.

#### Types of Unit Hydrographs
-----------------------------

*   **1-hour unit hydrograph**: A unit hydrograph representing the flow rate response to a unit input over a period of 1 hour.
*   **3-hour unit hydrograph**: A unit hydrograph representing the flow rate response to a unit input over a period of 3 hours.

### Key Formulas/Theorems
-------------------------

The unit hydrograph is obtained by dividing the actual flood hydrograph by the corresponding rainfall intensity. The unit hydrograph can be used to derive the flood hydrographs for different types and intensities of storms using the following formula:

$$\text{Flood Hydrograph} = \text{Unit Hydrograph} \times \text{Rainfall Intensity}$$

### Problem Solving Patterns
---------------------------

1.  **Understanding the Unit Hydrograph**: The unit hydrograph is a graphical representation of the flow rate response to a unit input. To solve problems related to the unit hydrograph, it is essential to understand its shape and behavior.
2.  **Scaling Up or Down**: When scaling up or down the unit hydrograph to obtain the flood hydrographs for different types and intensities of storms, it is crucial to consider the effect of rainfall intensity on the flow rate response.

### Examples with Solutions
---------------------------

**Example 1**

The ordinates of a 1-hour unit hydrograph are given below:

| Time (hours) | Ordinates of 1-hour UH (m/s) |
| --- | --- |
| 0   | 3                           |
| 1   | 13                          |
| 2   | 50                          |
| 3   | 80                          |
| 4   | 95                          |
| 5   | 85                          |

Derive a 3-hour unit hydrograph using the given ordinates.

**Solution**

To derive the 3-hour unit hydrograph, we need to calculate the flow rate response over a period of 3 hours. Since the ordinates are already given for a 1-hour unit hydrograph, we can use the following approach:

*   Calculate the cumulative flow over a period of 3 hours by summing up the ordinates.
*   Divide the cumulative flow by 3 to obtain the ordinates of the 3-hour unit hydrograph.

Let's calculate the cumulative flow over a period of 3 hours:

| Time (hours) | Ordinates of 1-hour UH (m/s) | Cumulative Flow |
| --- | --- | --- |
| 0   | 3                           | 0              |
| 1   | 13                          | 16             |
| 2   | 50                          | 66             |
| 3   | 80                          | 146            |
| 4   | 95                          | 241            |
| 5   | 85                          | 326            |

Now, let's divide the cumulative flow by 3 to obtain the ordinates of the 3-hour unit hydrograph:

| Time (hours) | Ordinates of 3-hour UH (m/s) |
| --- | --- |
| 0   | 0                           |
| 1   | 5.33                         |
| 2   | 22                            |
| 3   | 48.67                        |
| 4   | 80.33                        |
| 5   | 108.67                       |

**Example 2**

The peak discharge for the derived 3-hour unit hydrograph is required.

**Solution**

To determine the peak discharge, we need to analyze the ordinates of the 3-hour unit hydrograph and identify the maximum flow rate. From the ordinates calculated in Example 1, it can be seen that the maximum flow rate occurs at time = 4 hours with a value of 80.33 m/s.

However, this is not the correct answer. Let's re-evaluate the ordinates:

| Time (hours) | Ordinates of 3-hour UH (m/s) |
| --- | --- |
| 0   | 0                           |
| 1   | 5.33                         |
| 2   | 22                            |
| 3   | 48.67                        |
| 4   | 80.33                        |
| 5   | 108.67                       |

The maximum flow rate actually occurs at time = 5 hours with a value of 108.67 m/s.

### Common Pitfalls
-------------------

*   Not understanding the concept of unit hydrograph and its applications.
*   Failing to scale up or down the unit hydrograph correctly.
*   Not analyzing the ordinates carefully to identify the maximum flow rate.

### Quick Summary
------------------

*   Hydrograph: A graphical representation of the flow rate at different times during a flood event or storm runoff.
*   Unit hydrograph: A graphical representation of the flow rate response to a unit input over a period of time (e.g., 1 hour, 3 hours).
*   Scaling up or down the unit hydrograph: To obtain the flood hydrographs for different types and intensities of storms.

Note that this summary is not exhaustive and is meant to be a quick reference. For a more detailed understanding, please refer to the theory sections above.