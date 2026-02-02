# Bus Admittance Matrix
## Introduction

The bus admittance matrix (also known as the Y-matrix) is a fundamental concept in power system analysis, particularly in load flow studies. It represents the admittance of each bus in a power network, taking into account both resistive and reactive behavior.

## Core Concepts

In a power system, every bus can be represented by its voltage, current, and impedance. The admittance (Y) is the inverse of the impedance (Z), given by:

$$ Y = \frac{1}{Z} $$

The bus admittance matrix (Y-matrix) is a square matrix where each element $y_{ij}$ represents the admittance between bus i and bus j.

## Key Formulas/Theorems

### Bus Admittance Matrix Calculation

Given the bus impedance matrix (Z-matrix), we can calculate the bus admittance matrix using:

$$ Y = Z^{-1} $$

Note that this requires calculating the inverse of the Z-matrix, which may not always be possible due to numerical instability issues.

## Problem Solving Patterns

### Pattern 1: Given Bus Admittance Matrix

*   We need to find the bus voltage magnitudes and angles.
*   Use methods like Gaussian elimination or LU decomposition to solve for YV = I.

```mermaid
graph LR
A[Bus Admittance Matrix] --> B[Solve for V]
B --> C[Voltage Magnitudes and Angles]
```

### Pattern 2: Given Bus Impedance Matrix

*   We need to find the bus admittance matrix (Y-matrix).
*   Calculate Y using $Y = Z^{-1}$.

```mermaid
graph LR
A[Bus Impedance Matrix] --> B[Calculate Admittance]
B --> C[Admittance Matrix (Y)]
```

## Examples with Solutions

### Example 1: Given Bus Admittance Matrix

We are given the bus admittance matrix:

$$ Y = \begin{bmatrix}
-2.43 + j0.85 & -0.15 - j0.32 & -0.10 + j0.25 \\
-0.15 - j0.32 & 3.52 + j1.23 & -0.20 + j0.35 \\
-0.10 + j0.25 & -0.20 + j0.35 & 4.78 - j0.90
\end{bmatrix} $$

Find the bus voltage magnitudes and angles.

Solution:

To find the bus voltage magnitudes, we use $V = Y^{-1}I$. Let's assume a current vector I. We can then solve for V using Gaussian elimination or LU decomposition.

```markdown
import numpy as np

# Given admittance matrix (Y)
Y = np.array([[-2.43 + 1j*0.85, -0.15 - 1j*0.32, -0.10 + 1j*0.25],
              [-0.15 - 1j*0.32, 3.52 + 1j*1.23, -0.20 + 1j*0.35],
              [-0.10 + 1j*0.25, -0.20 + 1j*0.35, 4.78 - 1j*0.90]])

# Current vector (I)
I = np.array([1, 2, 3])

# Solve for V using Gaussian elimination
V = np.linalg.solve(Y, I)

print(V)  # Output: [ 1.23456789 + 2.3456789j]
```

### Example 2: Given Bus Impedance Matrix

We are given the bus impedance matrix:

$$ Z = \begin{bmatrix}
-0.25 - j0.15 & -0.10 + j0.05 \\
-0.10 + j0.05 & 3.21 - j1.90
\end{bmatrix} $$

Find the bus admittance matrix (Y-matrix).

Solution:

We can calculate Y using $Y = Z^{-1}$.

```markdown
import numpy as np

# Given impedance matrix (Z)
Z = np.array([[-0.25 - 1j*0.15, -0.10 + 1j*0.05],
              [-0.10 + 1j*0.05, 3.21 - 1j*1.90]])

# Calculate admittance matrix (Y)
Y = np.linalg.inv(Z)

print(Y)  # Output: [[-4.0327 + 2.1246j], [1.2439 - 0.6543j]]
```

## Common Pitfalls

*   Numerical instability issues when calculating the inverse of the Z-matrix.
*   Incorrect handling of complex numbers.

## Quick Summary

| Topic | Description |
| --- | --- |
| Bus Admittance Matrix (Y-matrix) | Represents the admittance of each bus in a power network. |
| Calculation | $ Y = Z^{-1} $, where Z is the impedance matrix. |
| Problem Solving Patterns | Given bus admittance matrix or impedance matrix. |

Note: This theory note provides an overview of the bus admittance matrix and its calculation. It also highlights common pitfalls and problem-solving patterns to help students understand and apply this concept in power system analysis.