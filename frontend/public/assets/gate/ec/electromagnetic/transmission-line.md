**Transmission Lines**
=====================

### Introduction

A transmission line is a conducting wire or cable used to transmit electrical energy over long distances with minimum loss of power. It consists of two conductors, typically wires or cables, separated by an insulating material.

### Core Concepts

#### Waves on Transmission Lines

When an alternating current (AC) flows through a transmission line, it generates electromagnetic waves that propagate along the conductor. The characteristics of these waves depend on the frequency and impedance of the line.

#### Propagation Constant ($\beta$)

The propagation constant is given by $\beta = \frac{\omega}{v} = \frac{2\pi f}{v}$, where $f$ is the frequency, $\omega$ is the angular frequency, and $v$ is the velocity of propagation.

#### Characteristic Impedance ($Z_0$)

The characteristic impedance of a transmission line is given by $Z_0 = \sqrt{\frac{L}{C}}$, where $L$ is the inductance per unit length and $C$ is the capacitance per unit length.

### Key Formulas/Theorems

*   The input impedance of a lossless transmission line is given by: $Z_{in} = Z_0 \frac{Z_L + jZ_0 \tan(\beta l)}{Z_0 + jZ_L \tan(\beta l)}$
*   The reflection coefficient at the load end is given by: $\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}$
*   The standing wave ratio (SWR) is given by: $s = \frac{1 + |\rho|}{1 - |\rho|}$, where $\rho$ is the reflection coefficient.

### Problem Solving Patterns

#### Q1 Analysis

The S-parameters of a two-port network are given as:

$$\begin{bmatrix}S_{11} & S_{12} \\ S_{21} & S_{22}\end{bmatrix} = \begin{bmatrix}0.8 + j0.2 & 0.4 - j0.1 \\ 0.3 + j0.5 & 0.9 - j0.8\end{bmatrix}$$

Two lossless transmission line sections of electrical lengths $\theta_1 = \beta l_1$ and $\theta_2 = \beta l_2$ are added to the input and output ports for measurement purposes, respectively.

The S-parameters of the resultant two-port network are given as:

$$\begin{bmatrix}S'_{11} & S'_{12} \\ S'_{21} & S'_{22}\end{bmatrix} = \frac{\begin{bmatrix}1 + S_{11} e^{-j\theta_1} & S_{12} e^{-j\theta_1} \\ S_{21} e^{j\theta_2} & 1 + S_{22} e^{-j\theta_2}\end{bmatrix}}{\begin{bmatrix}1 - S_{11} e^{-j\theta_1} & -S_{12} e^{-j\theta_1} \\ -S_{21} e^{j\theta_2} & 1 - S_{22} e^{-j\theta_2}\end{bmatrix}}$$

The problem asks to calculate the S-parameters of the resultant two-port network.

#### Q2 Analysis

A transmission line of length $\frac{3}{4}\lambda$ and having a characteristic impedance of $50 \Omega$ is terminated with a load of $400 \Omega$. The impedance seen at the input end of the transmission line is required to be calculated.

### Examples with Solutions

**Example 1**

Calculate the S-parameters of a two-port network with the following S-parameters:

$$\begin{bmatrix}S_{11} & S_{12} \\ S_{21} & S_{22}\end{bmatrix} = \begin{bmatrix}0.8 + j0.2 & 0.4 - j0.1 \\ 0.3 + j0.5 & 0.9 - j0.8\end{bmatrix}$$

Two lossless transmission line sections of electrical lengths $\theta_1 = \beta l_1$ and $\theta_2 = \beta l_2$ are added to the input and output ports for measurement purposes, respectively.

The S-parameters of the resultant two-port network are given by:

$$\begin{bmatrix}S'_{11} & S'_{12} \\ S'_{21} & S'_{22}\end{bmatrix} = \frac{\begin{bmatrix}1 + S_{11} e^{-j\theta_1} & S_{12} e^{-j\theta_1} \\ S_{21} e^{j\theta_2} & 1 + S_{22} e^{-j\theta_2}\end{bmatrix}}{\begin{bmatrix}1 - S_{11} e^{-j\theta_1} & -S_{12} e^{-j\theta_1} \\ -S_{21} e^{j\theta_2} & 1 - S_{22} e^{-j\theta_2}\end{bmatrix}}$$

**Example 2**

A transmission line of length $\frac{3}{4}\lambda$ and having a characteristic impedance of $50 \Omega$ is terminated with a load of $400 \Omega$. The impedance seen at the input end of the transmission line is required to be calculated.

### Quick Summary

*   S-parameters of a two-port network are given by:
    $$\begin{bmatrix}S_{11} & S_{12} \\ S_{21} & S_{22}\end{bmatrix}$$
*   Two lossless transmission line sections are added to the input and output ports for measurement purposes.
*   The S-parameters of the resultant two-port network are given by:
    $$\begin{bmatrix}S'_{11} & S'_{12} \\ S'_{21} & S'_{22}\end{bmatrix} = \frac{\begin{bmatrix}1 + S_{11} e^{-j\theta_1} & S_{12} e^{-j\theta_1} \\ S_{21} e^{j\theta_2} & 1 + S_{22} e^{-j\theta_2}\end{bmatrix}}{\begin{bmatrix}1 - S_{11} e^{-j\theta_1} & -S_{12} e^{-j\theta_1} \\ -S_{21} e^{j\theta_2} & 1 - S_{22} e^{-j\theta_2}\end{bmatrix}}$$

### Common Pitfalls

*   Students often forget to take into account the two lossless transmission line sections added to the input and output ports.
*   They may also forget to use the correct formula for calculating the S-parameters of the resultant two-port network.