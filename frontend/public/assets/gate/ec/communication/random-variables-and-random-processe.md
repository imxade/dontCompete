**Random Variables and Random Processes**
======================================

**Introduction**
---------------

Random variables and random processes are fundamental concepts in communication systems, modeling real-world phenomena with uncertainty. This note covers key definitions, formulas, and problem-solving patterns for GATE CS exam.

**Core Concepts**
-----------------

### Definition of Random Variables

*   A **random variable** is a function that maps an outcome from a sample space to a numerical value.
*   It can be **discrete**, taking on distinct values with probability mass function (PMF) or **continuous**, taking on any value within a range with probability density function (PDF).

### Definition of Random Processes

*   A **random process** is a collection of random variables, where each variable represents the value of the process at a specific time instance.
*   It can be **stationary**, having constant statistical properties over time, or **non-stationary**, with varying properties.

### Types of Random Variables and Processes

*   **Gaussian Process**: A continuous-time stochastic process with Gaussian distribution for any finite set of samples.
*   **White Gaussian Noise (WGN)**: A random process with zero mean, constant power spectral density (PSD), and uncorrelated samples.

**Key Formulas/Theorems**
-------------------------

### Power Spectral Density (PSD)

*   The PSD of a WGN is $S_X(\omega) = N_0/2$, where $N_0$ is the noise power.
*   For a stationary process, $S_X(\omega)$ is the Fourier transform of its autocorrelation function.

### Autocorrelation Function

*   The autocorrelation function $R_X(t, s)$ of a random process $X(t)$ is defined as $E[X(t) \cdot X(s)]$.
*   For wide-sense stationary (WSS) processes, the autocorrelation function depends only on the time difference $(t - s)$.

### Cross-Correlation Function

*   The cross-correlation function $R_{XY}(t, s)$ of two random processes $X(t)$ and $Y(s)$ is defined as $E[X(t) \cdot Y(s)]$.
*   For WSS processes, the cross-correlation function depends only on the time difference $(t - s)$.

**Problem Solving Patterns**
---------------------------

### Pattern 1: Power Spectral Density of a System Output

Given an LTI system with impulse response $h(t)$ and input $X(t)$, find the PSD of the output $Y(t) = X(t) \ast h(t)$.

*   Use the convolution property to express the output in the time domain.
*   Apply the Fourier transform to obtain the output in the frequency domain.
*   Compute the PSD using the power spectral density of the input and the squared magnitude of the system's transfer function.

### Pattern 2: Probability Density Function Transformation

Given a random variable $X$ with PDF $f_X(x)$, find the PDF of the transformed variable $Y = g(X)$.

*   Use the chain rule to express the joint PDF of $(X, Y)$.
*   Apply the transformation $y = g(x)$ to obtain the new PDF.
*   Simplify the expression using properties of the original PDF and the transformation function.

**Examples with Solutions**
---------------------------

### Example 1: Power Spectral Density of a System Output

Consider an LTI system with impulse response $h(t) = e^{-t}u(t)$ and input $X(t) = WGN(0, N_0/2)$.

*   Compute the PSD of the output using the convolution property.
*   Simplify the expression to obtain the final answer.

### Example 2: Probability Density Function Transformation

Consider a random variable $X$ with PDF $f_X(x) = e^{-x}u(x)$ and transformation $Y = X^2$.

*   Apply the chain rule to express the joint PDF of $(X, Y)$.
*   Simplify the expression to obtain the final answer.

**Common Pitfalls**
-----------------

*   Confusing PSD with autocorrelation function or vice versa.
*   Failing to apply the convolution property for system outputs.
*   Not using the chain rule for probability density function transformations.

**Quick Summary**
----------------

*   Random variables and random processes are fundamental in communication systems.
*   Key concepts include power spectral density, autocorrelation functions, and cross-correlation functions.
*   Problem-solving patterns involve applying convolution properties, transformation rules, and simplifying expressions.

[Visuals]

This note covers the core concepts, key formulas/theorems, problem-solving patterns, examples with solutions, common pitfalls, and a quick summary. It is designed to help students prepare for the GATE CS exam on random variables and random processes.