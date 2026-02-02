# Solution of Differential Equations: Numerical Method
## Introduction

Differential equations are fundamental in modeling various phenomena in physics, engineering, and other fields. However, solving them analytically can be challenging or impossible for certain types of equations. Numerical methods provide a way to approximate the solution of differential equations.

## Core Concepts

### Types of Differential Equations

* **Ordinary Differential Equations (ODEs)**: Involving one independent variable.
* **Partial Differential Equations (PDEs)**: Involving multiple independent variables.

### Order of Differential Equation

* The order of a differential equation is the highest derivative involved in the equation.

## Key Formulas/Theorems

$$\begin{aligned}
y'' + p(x)y' + q(x)y &= f(x) \\
\end{aligned}$$

where $p(x)$, $q(x)$, and $f(x)$ are functions of $x$.

### Euler's Method

A simple numerical method for solving ODEs. Given the initial condition $y(0) = y_0$, we can approximate the solution at $x_{n+1}$ using:

$$\begin{aligned}
y_{n+1} &= y_n + hf(x_n, y_n)
\end{aligned}$$

where $h$ is the step size.

### Improved Euler's Method

A more accurate version of Euler's method. It uses two points to estimate the slope and then averages them:

$$\begin{aligned}
y_{n+1} &= y_n + \frac{h}{2}(f(x_n, y_n) + f(x_{n+1}, y_n + hf(x_n, y_n)))
\end{aligned}$$

## Problem Solving Patterns

* Identify the type of differential equation and choose the appropriate numerical method.
* Check if the initial conditions are given.

## Examples with Solutions

### Example 1: Euler's Method

Consider the ODE:

$$\begin{aligned}
y'' + y' + y &= 0 \\
y(0) = 1, \quad y'(0) = 0
\end{aligned}$$

Using Euler's method with a step size of $h=0.1$, find an approximation for $y(0.1)$.

Solution:

We first need to estimate the slope at $x_0$ using Euler's method:

$$\begin{aligned}
f(x_0, y_0) &= f(0, 1) = -1
\end{aligned}$$

Now we can approximate the value of $y(0.1)$:

$$\begin{aligned}
y(0.1) &\approx y(0) + hf(0, y(0)) \\
&= 1 + (0.1)(-1) = 0.9
\end{aligned}$$

### Example 2: Improved Euler's Method

Consider the same ODE as above but use improved Euler's method:

Solution:

We first need to estimate the slope at $x_0$ using the improved Euler's method:

$$\begin{aligned}
f(x_0, y_0) &= f(0, 1) = -1 \\
y_{n+1} &= y_n + \frac{h}{2}(f(x_n, y_n) + f(x_{n+1}, y_n + hf(x_n, y_n)))
\end{aligned}$$

Substituting the values:

$$\begin{aligned}
y(0.1) &\approx 1 + \frac{(0.1)}{2}((-1) + (-1)) \\
&= 1 - (0.05)(-2) = 1.1
\end{aligned}$$

## Common Pitfalls

* Incorrect application of numerical methods.
* Ignoring the initial conditions.

## Quick Summary

* Understand the type of differential equation and choose the appropriate numerical method.
* Check if the initial conditions are given.
* Apply the correct formulas for Euler's and improved Euler's methods.