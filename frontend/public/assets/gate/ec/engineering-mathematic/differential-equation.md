**Differential Equations**
==========================

### Introduction

A differential equation (DE) is an equation that involves an unknown function and its derivatives. DEs are used to model a wide range of phenomena, from population growth and chemical reactions to electrical circuits and mechanical systems.

### Core Concepts

#### Ordinary Differential Equations (ODEs)

*   An ODE is a DE that contains only one independent variable and its derivatives.
*   The general form of an ODE is:

$$F(x,y,y',y'',...)=0$$

where $x$ is the independent variable, $y$ is the unknown function, and $y'$, $y''$, etc. are its derivatives.

#### Types of ODEs

*   **Linear ODEs**: These have a linear dependence on the unknown function and its derivatives.

    $$P(x)y'+Q(x)y=R(x)$$
*   **Nonlinear ODEs**: These do not satisfy the above form.

    Example: $y''+yy'=0$

#### Solution Methods for ODEs

*   **Separation of Variables**: Separate the variables and integrate.
*   **Substitution Method**: Substitute a function or a combination of functions to simplify the DE.
*   **Integration Factor**: Multiply the DE by an integrating factor, which is usually a function of $x$.

### Key Formulas/Theorems

#### Integrating Factor

The integrating factor for a linear ODE in the form:

$$y'+P(x)y=Q(x)$$

is given by:

$$\mu(x)=e^{\int P(x)dx}$$

The general solution is then given by:

$$y=\frac{1}{\mu(x)}\left[\int Q(x)\mu(x)dx+C\right]$$

#### Separation of Variables

For a DE in the form:

$$\frac{dy}{dx}=f(x,y)g(y)$$

separate the variables to get:

$$\frac{dg(y)}{f(x,y)}=dx$$

Integrate both sides and solve for $y$.

### Problem Solving Patterns

#### Q1 (ec_2021_32)

The given DE is:

$$2y+\frac{dy}{dx}=x+y$$

To find the integrating factor, we need to identify the coefficients of $y$ and $\frac{dy}{dx}$.

*   Coefficient of $y$: 2
*   Coefficient of $\frac{dy}{dx}$: 1

The integrating factor is given by:

$$\mu(x)=e^{\int \left(\frac{-1}{2}\right) dx}=e^{-\frac{x}{2}}$$

Multiply the DE by the integrating factor to get:

$$e^{-\frac{x}{2}}\left(2y+\frac{dy}{dx}\right)=e^{-\frac{x}{2}}x+e^{-\frac{x}{2}}y$$

The left-hand side is now a total derivative, so we can integrate both sides with respect to $x$:

$$\int \mu(x) d(y)=\int (x+y)e^{-\frac{x}{2}} dx$$

Simplifying the right-hand side and solving for $y$, we get:

$$y=x+Ce^{x/2}$$

Hence, the correct option is (B): $1/\sqrt{3}(e^{\frac{x}{2}}-C)$.

### Examples with Solutions

#### Example 1: Nonlinear ODE

Solve the DE:

$$y''-4yy'=0$$

*   Let $z=y'$.
*   The given DE becomes a first-order linear DE in $z$ and $x$: $z'-4yz=0$
*   Multiply by an integrating factor, $\mu(x)=e^{-\int 4dx}=e^{-4x}$:
    \begin{align*}
    e^{-4x}z'&=-4ye^{4x}\\
    \Rightarrow\quad z'&=-4ye^{5x}
    \end{align*}

Integrate both sides to solve for $z$:

$$z=\int -4ye^{5x} dx$$

Simplifying and solving for $y$, we get:

$$y=(C+\frac{x^2}{5})e^{-\frac{2x^2}{5}}$$

#### Example 2: Separation of Variables

Solve the DE:

$$\frac{dy}{dx}=x^2+3y$$

*   Separate the variables to get:
    \begin{align*}
    \int \frac{1}{(3+x^2)} dy&=\int (x^2+3) dx\\
    \Rightarrow\quad \frac{1}{6}\ln|3+x^2|&=x^3+3x+C
    \end{align*}

Solving for $y$, we get:

$$y=Ce^{6(x^3+3x)}+x^2$$

### Common Pitfalls

*   Students often forget to identify the correct integrating factor, leading to incorrect solutions.
*   Another common error is not separating the variables correctly in nonlinear DEs.

### Quick Summary

*   Differential equations are crucial in modeling real-world phenomena.
*   ODEs have various solution methods like separation of variables and integration factors.
*   Identify coefficients to find the correct integrating factor and simplify the DE accordingly.