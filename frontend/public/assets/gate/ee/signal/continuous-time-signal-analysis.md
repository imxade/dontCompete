**Continuous Time Signal Analysis**
=====================================

**Introduction**
---------------

In this note, we will delve into the analysis of continuous time signals using Fourier transform techniques. The focus will be on understanding key concepts, formulas, and problem-solving patterns to tackle questions from previous years.

**Core Concepts**
-----------------

### 1. Even Functions

An even function satisfies:

$$
f(t) = f(-t)
$$

for all $t$. This implies that the function is symmetric about the y-axis.

### 2. Fourier Transform

The Fourier transform of a continuous-time signal $f(t)$ is defined as:

$$
F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-j\omega t}dt
$$

where $\omega$ is the angular frequency.

### 3. Differentiation in the Frequency Domain

For an even function, differentiation in the time domain corresponds to a multiplication by $-j\omega$ in the frequency domain:

$$
\frac{df(t)}{dt} \Leftrightarrow -j\omega F(\omega)
$$

**Key Formulas/Theorems**
-------------------------

### 1. Fourier Transform of an Even Function

The Fourier transform of an even function is a real-valued function:

$$
F(\omega) = F(-\omega)^*
$$

where $^*$ denotes complex conjugation.

### 2. Differentiation Theorem

For an even function, differentiation in the time domain corresponds to multiplication by $-j\omega$ in the frequency domain:

$$
\frac{df(t)}{dt} \Leftrightarrow -j\omega F(\omega)
$$

**Problem Solving Patterns**
---------------------------

### 1. Identifying Even Functions

To determine if a function is even, check if it satisfies $f(t) = f(-t)$ for all $t$.

### 2. Applying the Differentiation Theorem

Use the differentiation theorem to find the Fourier transform of a derivative:

$$
\frac{df(t)}{dt} \Leftrightarrow -j\omega F(\omega)
$$

**Examples with Solutions**
---------------------------

### Example 1: Finding the Fourier Transform of an Even Function

Given $f(t) = e^{-at}$, find its Fourier transform.

```mermaid
graph LR
A[Even function] --> B[Integrate]
B[Integrate] --> C[$F(\omega)$]
C[$F(\omega)$] --> D[jω/$(a^2 + ω^2)$]
```

Solution:

$$
\begin{aligned}
F(\omega) &= \int_{-\infty}^{\infty} e^{-at}e^{-j\omega t}dt \\
&= \frac{-j\omega}{a^2 + \omega^2}
\end{aligned}
$$

### Example 2: Applying the Differentiation Theorem

Given $f(t) = e^{-at}$, find its derivative and Fourier transform.

```mermaid
graph LR
A[Even function] --> B[Differentiate]
B[Differentiate] --> C[jω/$(a^2 + ω^2)$]
```

Solution:

$$
\begin{aligned}
\frac{df(t)}{dt} &= -ae^{-at} \\
F(\omega) &= \int_{-\infty}^{\infty} -ae^{-at}e^{-j\omega t}dt \\
&= (-j\omega)\left(\frac{-j\omega}{a^2 + \omega^2}\right)
\end{aligned}
$$

**Common Pitfalls**
------------------

### 1. Misidentifying Even Functions

Be careful when checking if a function is even; always verify that $f(t) = f(-t)$ for all $t$.

### 2. Applying the Differentiation Theorem Incorrectly

Make sure to use the correct formula for differentiation in the frequency domain:

$$
\frac{df(t)}{dt} \Leftrightarrow -j\omega F(\omega)
$$

**Quick Summary**
-----------------

* Even functions satisfy $f(t) = f(-t)$ for all $t$.
* The Fourier transform of an even function is real-valued: $F(\omega) = F(-\omega)^*$.
* Differentiation in the time domain corresponds to multiplication by $-j\omega$ in the frequency domain.

Note: This note has been created to provide a comprehensive overview of continuous time signal analysis using Fourier transform techniques. It includes core concepts, key formulas and theorems, problem-solving patterns, examples with solutions, and common pitfalls to watch out for.