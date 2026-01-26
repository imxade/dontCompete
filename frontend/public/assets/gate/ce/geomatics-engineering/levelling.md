# Levelling
================

## Introduction
---------------

Levelling is a technique used in geomatics engineering to determine the height of points on the ground surface with respect to a reference point. It involves measuring the difference in height between two points using a levelling instrument, such as a theodolite or a total station.

## Core Concepts
-----------------

### Levelling Instruments

Levelling instruments are used to measure the angle and distance between two points on the ground surface. The most common types of levelling instruments are:

*   Theodolites: Used for precise measurements of horizontal angles and distances.
*   Total Stations: Used for simultaneous measurement of horizontal and vertical angles and distances.

### Levelling Methodologies

There are two primary methodologies used in levelling:

*   **Differential Levelling**: Measures the difference in height between two points using a series of intermediate benchmarks (BMs).
*   **Absolute Levelling**: Measures the absolute height of a point with respect to a known reference point, such as an Ordnance Datum.

### Principles of Levelling

The principles of levelling are based on the following laws:

*   **Law of Sines**: Relates the angles and sides of triangles.
*   **Law of Cosines**: Relates the angles and sides of triangles.

## Key Formulas/Theorems
-------------------------

### Differential Levelling Formula

The formula for differential levelling is given by:

$$\Delta h = \frac{1}{2} (H_1 + H_2) - R_L$$

where $\Delta h$ is the difference in height, $H_1$ and $H_2$ are the staff readings at points 1 and 2, and $R_L$ is the reduced level of point 2.

### Absolute Levelling Formula

The formula for absolute levelling is given by:

$$h = H + R_D - \Delta h$$

where $h$ is the absolute height of point P, $H$ is the staff reading at point P, $R_D$ is the Ordnance Datum, and $\Delta h$ is the difference in height between point P and the reference point.

## Problem Solving Patterns
---------------------------

### Differential Levelling

When solving differential levelling problems, follow these steps:

1.  Identify the reduced levels of each benchmark (BM).
2.  Use the formula for differential levelling to calculate the difference in height between two points.
3.  Round off the final answer to the required number of decimal places.

### Absolute Levelling

When solving absolute levelling problems, follow these steps:

1.  Identify the staff reading at point P and the Ordnance Datum.
2.  Use the formula for absolute levelling to calculate the absolute height of point P.
3.  Round off the final answer to the required number of decimal places.

## Examples with Solutions
---------------------------

### Example 1: Differential Levelling

A differential levelling is carried out from point P (BM: +200.000 m) to point R. The readings taken are given in the table below.

| Points | Staff Readings (m) | Remarks |
| --- | --- | --- |
| P | (+)2.050 | Back Sight |
|  | (-) | BM: 200.000 m |
| Q | 1.050 | Fore Sight |
|  | 0.950 | Q is a change point |
| R | (-)1.655 | |

Calculate the reduced level of point R (rounded off to 3 decimal places).

Solution:

*   Reduced Level of P = +200.000 m
*   Staff reading at Q = 1.050 m
*   Staff reading at R = -1.655 m
*   Δh = (H_Q + H_R) / 2 - RL_P
= (1.050 + (-1.655)) / 2 - 200.000
= -0.6525 m
*   Reduced Level of R = RL_P + Δh
= 200.000 - 0.6525
= 199.3475

### Example 2: Absolute Levelling

An absolute levelling is carried out at point P with a staff reading of (+)3.250 m and an Ordnance Datum of 100.000 m. Calculate the absolute height of point P (rounded off to 4 decimal places).

Solution:

*   Staff reading at P = +3.250 m
*   Ordnance Datum = 100.000 m
*   Δh = 0 (since it's an absolute levelling)
*   Absolute Height of P = H_P - Δh + RD
= 3.250 - 0 + 100.000
= 103.250

## Common Pitfalls
------------------

*   Failing to identify the correct type of levelling (differential or absolute).
*   Incorrectly applying the formula for differential or absolute levelling.
*   Failing to round off the final answer to the required number of decimal places.

## Quick Summary
---------------

### Key Concepts

*   Levelling instruments (theodolites and total stations)
*   Levelling methodologies (differential and absolute levelling)
*   Principles of levelling (Law of Sines and Law of Cosines)

### Formulas/Theorems

*   Differential levelling formula: Δh = (H_1 + H_2) / 2 - RL
*   Absolute levelling formula: h = H + RD - Δh

### Problem Solving Patterns

*   Follow the steps for differential or absolute levelling depending on the type of problem.
*   Round off the final answer to the required number of decimal places.