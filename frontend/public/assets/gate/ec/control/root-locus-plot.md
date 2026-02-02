# Root Locus Plot
=====================

## Introduction
---------------

The root locus plot is a graphical representation of the roots of the characteristic equation of a closed-loop system as a parameter, usually gain (K), varies from 0 to infinity. It provides valuable insights into the stability and transient response of the system.

## Core Concepts
-----------------

### Asymptotes

*   The root locus branches approach asymptotically towards the real axis at an angle determined by the poles of the open-loop transfer function.
*   The number of asymptotes is equal to the number of poles in the right half of the s-plane minus the number of zeros.

### Centroid

*   The centroid is the point where the asymptotes intersect on the real axis.
*   It is calculated as the average of the angles at which the asymptotes approach the real axis.

### Angles of Departure and Arrival

*   The angle of departure is the angle at which a root locus branch departs from a pole.
*   The angle of arrival is the angle at which a root locus branch arrives at a zero.

## Key Formulas/Theorems
-------------------------

LaTeX Equation: $\sigma = \frac{\sum R_{i}}{N-M}$

where σ is the centroid, R_i are the real parts of the poles and zeros, and N and M are the number of poles and zeros respectively.

LaTeX Equation: $\theta = 180\left(\frac{N-M}{N+1}\right)$

where θ is the angle at which an asymptote approaches the real axis.

## Problem Solving Patterns
---------------------------

### Identifying Asymptotes

*   Count the number of poles in the right half of the s-plane.
*   Subtract the number of zeros to find the number of asymptotes.

### Determining Angles of Departure and Arrival

*   Use the angles of departure from each pole to determine the initial direction of each root locus branch.
*   Calculate the angle of arrival at each zero using the formula above.

## Examples with Solutions
---------------------------

**Example 1:**

Given a system with an open-loop transfer function:

LaTeX Equation: $G(s) = \frac{K}{s(s+2)}$

Find the number of asymptotes and determine their angles.

Solution:

*   Number of poles in the right half of the s-plane: 0
*   Number of zeros: 1
*   Number of asymptotes: 1
*   Angle of each asymptote: 180°

**Example 2:**

Given a system with an open-loop transfer function:

LaTeX Equation: $G(s) = \frac{K}{s(s+1)(s+2)}$

Find the centroid and number of asymptotes.

Solution:

*   Number of poles in the right half of the s-plane: 1
*   Number of zeros: 0
*   Number of asymptotes: 2
*   Centroid: calculated using the formula above

## Common Pitfalls
-----------------

### Missed Poles or Zeros

*   Carefully count the number of poles and zeros in the open-loop transfer function.
*   Verify that each pole and zero is correctly identified.

### Incorrect Angles

*   Use a protractor to measure the angles of departure and arrival accurately.
*   Double-check calculations for angle determination.

## Quick Summary
-----------------

*   Root locus plot represents the roots of the characteristic equation as gain (K) varies from 0 to infinity.
*   Asymptotes approach the real axis at an angle determined by poles and zeros.
*   Centroid is the point where asymptotes intersect on the real axis.

Note: The above theory note covers all theoretical concepts, formulas, and insights required to solve questions like GATE 2022 (ID: ec_2022_22) Question 22.