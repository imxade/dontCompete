**Continuous Compounding**
==========================

### Introduction

Continuous compounding is a fundamental concept in finance and mathematics that deals with calculating interest rates and growth rates when interest is compounded continuously. In this note, we will cover the theoretical concepts, formulas, and problem-solving strategies required to tackle questions related to continuous compounding.

### Core Concepts

**What is Continuous Compounding?**

Continuous compounding refers to the process of calculating interest on an initial principal amount (P) for a specified time period (t), where the frequency of compounding is infinite. This means that the interest is compounded at every instant, rather than at fixed intervals such as monthly or annually.

**Key Principles**

1.  The formula for continuous compounding is given by:

    $$A = Pe^{rt}$$

    Where:
    *   A is the amount after time t
    *   P is the principal amount
    *   r is the annual interest rate (in decimal form)
    *   t is the time period (in years)

2.  The effective interest rate (eff_i) under continuous compounding can be calculated using the formula:

    $$\text{eff}_i = \lim_{m\to\infty} \left(1 + \frac{i}{m}\right)^m$$

    Where:
    *   eff_i is the effective interest rate
    *   i is the nominal interest rate (as a decimal)

### Key Formulas/Theorems

*   **Continuous Compounding Formula**: $A = Pe^{rt}$
*   **Effective Interest Rate Formula**: $\text{eff}_i = \lim_{m\to\infty} \left(1 + \frac{i}{m}\right)^m$

```latex
\begin{equation}
\label{eq:continuous-compounding}
A = Pe^{rt}
\end{equation}

\begin{equation}
\label{eq:eff-interest-rate}
\text{eff}_i = \lim_{m\to\infty} \left(1 + \frac{i}{m}\right)^m
\end{equation}
```

### Problem Solving Patterns

**Pattern 1:** Calculating Amount after Time Period

*   Given: Principal (P), interest rate (r), time period (t)
*   Required: Calculate the amount after time t using the continuous compounding formula ($A = Pe^{rt}$)

```mermaid
graph LR
    A[Given] -->|Principal, Rate, Time|> B[Calculate]
    B -->|Continuous Compounding Formula|> C[Amount]
```

**Pattern 2:** Calculating Effective Interest Rate

*   Given: Nominal interest rate (i)
*   Required: Calculate the effective interest rate using the formula ($\text{eff}_i = \lim_{m\to\infty} \left(1 + \frac{i}{m}\right)^m$)

```mermaid
graph LR
    A[Given] -->|Nominal Interest Rate|> B[Calculate]
    B -->|Effective Interest Rate Formula|> C[Eff. Interest Rate]
```

### Examples with Solutions

**Example 1:**

A principal amount of $\$$10,000$ is invested at an annual interest rate of 5% for a time period of 2 years. Calculate the amount after 2 years.

Solution:

*   Given: P = $10,000$, r = 0.05, t = 2
*   Using the continuous compounding formula:
    \begin{align*}
    A &= Pe^{rt} \\
    & = \$10,000 e^{0.05 \times 2} \\
    & = \$10,000 e^{0.1} \\
    & ≈ \$10,551.16
    \end{align*}

**Example 2:**

A nominal interest rate of 6% is compounded continuously. Calculate the effective interest rate.

Solution:

*   Given: i = 0.06
*   Using the formula for effective interest rate:
    \begin{align*}
    \text{eff}_i &= \lim_{m\to\infty} \left(1 + \frac{i}{m}\right)^m \\
    & = \lim_{m\to\infty} \left(1 + \frac{0.06}{m}\right)^m \\
    & = e^{0.06}
    \end{align*}

### Common Pitfalls

*   Forgetting to convert the interest rate from percentage to decimal form
*   Misapplying the continuous compounding formula for effective interest rate calculation
*   Ignoring the limit in the effective interest rate formula

### Quick Summary

*   Continuous compounding formula: $A = Pe^{rt}$
*   Effective interest rate formula: $\text{eff}_i = \lim_{m\to\infty} \left(1 + \frac{i}{m}\right)^m$
*   Patterns:
    *   Calculating amount after time period using the continuous compounding formula
    *   Calculating effective interest rate using the formula for effective interest rate

This comprehensive note covers all the theoretical concepts and formulas required to solve questions related to continuous compounding. By following this guide, students can develop a deep understanding of continuous compounding and effectively tackle problems on the topic.