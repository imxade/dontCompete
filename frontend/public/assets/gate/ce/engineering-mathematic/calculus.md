**Calculus Theory Note**
========================

### Introduction

Calculus is a branch of mathematics that deals with the study of continuous change, particularly in the context of functions and limits. It has extensive applications in various fields such as physics, engineering, economics, and computer science. The two main branches of calculus are Differential Calculus and Integral Calculus.

### Core Concepts

#### Limits

The concept of a limit is central to calculus. A function f(x) has a limit L at x=a if for every ε>0, there exists a δ>0 such that |f(x)-L|<ε whenever 0<|x-a|<δ.

*   The notation lim x→a f(x)=L is used to represent the limit.
*   A function may have a limit even if it does not exist at a particular point.

#### Differentiation

Differentiation is a fundamental concept in calculus that deals with the rate of change of a function with respect to its input variable. The derivative of a function f(x) is denoted as f'(x).

*   Geometrically, the derivative represents the slope of the tangent line to the graph of the function at a given point.
*   Differentiation can be used to find the maximum and minimum values of a function.

#### Integration

Integration is another key concept in calculus that deals with finding the area under curves. The definite integral of a function f(x) from a to b is denoted as ∫[a,b] f(x) dx.

*   Geometrically, the definite integral represents the area between the graph of the function and the x-axis.
*   Integration can be used to find the volume of solids and surfaces.

### Key Formulas/Theorems

*   **Power Rule**: If f(x)=x^n, then f'(x)=nx^(n-1)
*   **Product Rule**: If f(x)=u(x)v(x), then f'(x)=u'(x)v(x)+u(x)v'(x)
*   **Quotient Rule**: If f(x)=u(x)/v(x), then f'(x)=(u'(x)v(x)-u(x)v'(x))/v^2(x)

### Problem Solving Patterns

1.  **Function Differentiation**: Use the power rule, product rule, and quotient rule to find derivatives of functions.
2.  **Limit Evaluation**: Apply the definition of a limit or use known limits such as lim x→a sin(x)/x=1 to evaluate limits.
3.  **Integration by Substitution**: Use substitution to integrate functions that are difficult to integrate directly.

### Examples with Solutions

**Example 1:** Find the derivative of f(x)=2x^2sin(x)

*   Using the product rule, we get
    f'(x)=(2x^2)'sin(x)+2x^2(sin(x))'
    =4xsin(x)+2x^2cos(x)

**Example 2:** Evaluate the limit lim x→0 sin(x)/x

*   Applying the definition of a limit, we get
    For every ε>0, there exists δ>0 such that |sin(x)/x-L|<ε whenever 0<|x-0|<δ.
    Since sin(0)=0 and cos(0)=1, we have L=1.

### Common Pitfalls

*   **Incorrect Application of Rules**: Make sure to apply the correct differentiation or integration rule for a given function.
*   **Limit Evaluation Errors**: Verify that you are applying the definition of a limit correctly when evaluating limits.

### Quick Summary

*   Limits: lim x→a f(x)=L
*   Differentiation: f'(x)=(2x^2)'sin(x)+2x^2(sin(x))'
*   Integration by Substitution: ∫[a,b] u'(x)v(x) dx=uv(b)-uv(a)

Note: The above content is just an example and might need adjustments according to your specific requirements.