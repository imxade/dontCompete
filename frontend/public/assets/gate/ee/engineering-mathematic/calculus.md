**Calculus Theory Note**
=======================

**Introduction**
---------------

Calculus is a branch of mathematics that deals with the study of continuous change, particularly in the context of functions and limits. It has extensive applications in various fields, including physics, engineering, economics, and computer science.

**Core Concepts**
-----------------

### Limits

The limit of a function f(x) as x approaches a certain value a is denoted as lim x→a f(x). It represents the behavior of the function as x gets arbitrarily close to a.

*   The limit exists if the function approaches a unique value as x approaches a.
*   The limit does not exist if the function oscillates or becomes infinite as x approaches a.

### Derivatives

The derivative of a function f(x) is denoted as f'(x) and represents the rate of change of the function with respect to x. It is defined as:

f'(x) = lim h→0 [f(x + h) - f(x)]/h

*   Geometrically, the derivative represents the slope of the tangent line to the graph of the function at a given point.
*   Physically, the derivative represents the rate of change of a quantity with respect to time or another variable.

### Integrals

The definite integral of a function f(x) from x=a to x=b is denoted as ∫[a,b] f(x) dx and represents the area under the curve of the function between the limits of integration. It is defined as:

∫[a,b] f(x) dx = F(b) - F(a)

where F(x) is the antiderivative of f(x).

*   Geometrically, the definite integral represents the area between the graph of the function and the x-axis.
*   Physically, the definite integral represents the total accumulation of a quantity over a given interval.

**Key Formulas/Theorems**
-------------------------

### Power Rule

If f(x) = x^n, then f'(x) = nx^(n-1)

### Product Rule

If f(x) = u(x)v(x), then f'(x) = u'(x)v(x) + u(x)v'(x)

### Quotient Rule

If f(x) = u(x)/v(x), then f'(x) = (u'(x)v(x) - u(x)v'(x)) / v^2(x)

### Fundamental Theorem of Calculus

∫[a,b] f(x) dx = F(b) - F(a)

where F(x) is the antiderivative of f(x).

**Problem Solving Patterns**
---------------------------

*   Identify the type of problem: limit, derivative, or integral.
*   Read and understand the problem carefully.
*   Sketch a graph to visualize the situation (if applicable).
*   Apply relevant formulas and theorems to solve the problem.

**Examples with Solutions**
-------------------------

### Example 1: Limit

Find the limit of f(x) = (2x^2 - 3x + 1)/(x^2 - 4) as x approaches 2.

Solution:

lim x→2 (2x^2 - 3x + 1)/(x^2 - 4)
= lim x→2 [(2x^2 - 3x + 1) / (x-2)(x+2)] / [1/(x-2)]
= lim x→2 (2x^2 - 3x + 1)/((x-2)(x+2))
= (4 - 6 + 1)/(4 - 4)
= -1/0

The limit does not exist because the function becomes infinite as x approaches 2.

### Example 2: Derivative

Find the derivative of f(x) = x^3 - 2x^2 + x.

Solution:

f'(x) = d/dx (x^3 - 2x^2 + x)
= d/dx (x^3) - d/dx (2x^2) + d/dx (x)
= 3x^2 - 4x + 1

### Example 3: Integral

Find the definite integral of f(x) = x^2 from x=0 to x=2.

Solution:

∫[0,2] x^2 dx
= F(2) - F(0)
where F(x) is the antiderivative of f(x).
= (x^3 / 3) | [0,2]
= (8/3) - 0
= 8/3

**Common Pitfalls**
-------------------

*   Be careful with sign errors when applying formulas and theorems.
*   Make sure to read and understand the problem carefully before starting to solve it.
*   Double-check your work for accuracy.

**Quick Summary**
-----------------

Calculus is a branch of mathematics that deals with the study of continuous change. It has extensive applications in various fields, including physics, engineering, economics, and computer science. The core concepts include limits, derivatives, and integrals. Key formulas and theorems include the power rule, product rule, quotient rule, and fundamental theorem of calculus.

This note covers all the theoretical concepts required to solve the source questions, which include finding limits, derivatives, and integrals, as well as applying relevant formulas and theorems. The examples with solutions demonstrate how to apply these concepts to real-world problems.