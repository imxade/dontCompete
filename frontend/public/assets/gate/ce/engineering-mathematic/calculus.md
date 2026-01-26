**Calculus Theory Note**
========================

**Introduction**
---------------

Calculus is a branch of mathematics that deals with the study of continuous change, particularly in the context of functions and limits. It consists of two main branches: Differential Calculus (study of rates of change) and Integral Calculus (study of accumulation).

**Core Concepts**
-----------------

### Limits

The limit of a function $f(x)$ as $x$ approaches $a$ is denoted by $\lim_{x \to a} f(x)$ and represents the value that the function approaches as $x$ gets arbitrarily close to $a$. If the limit exists, it can be denoted by $L = \lim_{x \to a} f(x)$.

### Continuity

A function $f(x)$ is said to be continuous at a point $a$ if the following conditions are met:

1. The function is defined at $a$, i.e., $f(a)$ exists.
2. The limit of the function as $x$ approaches $a$ exists, i.e., $\lim_{x \to a} f(x)$ exists.
3. The limit of the function as $x$ approaches $a$ is equal to the value of the function at $a$, i.e., $\lim_{x \to a} f(x) = f(a)$.

### Differentiation

The derivative of a function $f(x)$ with respect to $x$ is denoted by $f'(x)$ and represents the rate of change of the function at a given point. It can be calculated using various rules, including:

* Power Rule: If $f(x) = x^n$, then $f'(x) = nx^{n-1}$
* Product Rule: If $f(x) = u(x)v(x)$, then $f'(x) = u'(x)v(x) + u(x)v'(x)$
* Quotient Rule: If $f(x) = \frac{u(x)}{v(x)}$, then $f'(x) = \frac{u'(x)v(x) - u(x)v'(x)}{(v(x))^2}$

### Integration

The definite integral of a function $f(x)$ with respect to $x$ between two limits $a$ and $b$ is denoted by $\int_{a}^{b} f(x) dx$. It represents the area under the curve of the function between the two limits.

**Key Formulas/Theorems**
-------------------------

### Fundamental Theorem of Calculus (FTC)

The FTC states that differentiation and integration are inverse processes. Specifically, if $F(x)$ is an antiderivative of $f(x)$, then:

$$\int_{a}^{b} f(x) dx = F(b) - F(a)$$

### Mean Value Theorem (MVT)

The MVT states that a function $f(x)$ has at least one point where the instantaneous rate of change is equal to the average rate of change. Mathematically:

$$\exists c \in [a, b] : f'(c) = \frac{f(b) - f(a)}{b-a}$$

### L'Hopital's Rule

L'Hopital's rule states that if a limit is in the form $\frac{0}{0}$ or $\frac{\infty}{\infty}$, then:

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

**Problem Solving Patterns**
---------------------------

### Evaluating Limits

When evaluating limits, the following patterns are useful:

* **Direct Substitution**: If $f(x)$ is continuous at $a$, then $\lim_{x \to a} f(x) = f(a)$.
* **One-Sided Limits**: If $f(x)$ has a limit as $x$ approaches $a$ from one side, but not the other, then:
	+ $\lim_{x \to a^+} f(x) = L$
	+ $\lim_{x \to a^-} f(x) = M$
* **L'Hopital's Rule**: If a limit is in the form $\frac{0}{0}$ or $\frac{\infty}{\infty}$, then apply L'Hopital's rule.

### Solving Differential Equations

When solving differential equations using separation of variables:

1. Separate the variables by dividing both sides of the equation by $y$ and multiplying both sides by $dx$.
2. Integrate both sides separately to obtain the solution.

**Examples with Solutions**
---------------------------

### Example 1: Evaluating Limits

Find $\lim_{x \to 0} \frac{\sin x}{x}$.

Solution:

Using direct substitution, we get:

$$\lim_{x \to 0} \frac{\sin x}{x} = \frac{\sin 0}{0} = \frac{0}{0}$$

Applying L'Hopital's rule, we get:

$$\lim_{x \to 0} \frac{\cos x}{1} = 1$$

### Example 2: Solving Differential Equations

Solve the differential equation $\frac{dy}{dx} = xy$.

Solution:

Separating variables, we get:

$$\int \frac{dy}{y} = \int x dx$$

Integrating both sides separately, we get:

$$\ln |y| = \frac{x^2}{2} + C$$

### Example 3: Integrating Functions

Evaluate $\int e^{x} dx$.

Solution:

Using the power rule for integration, we get:

$$\int e^{x} dx = e^x + C$$

**Common Pitfalls**
-------------------

* **Incorrectly Applying L'Hopital's Rule**: Be careful when applying L'Hopital's rule to ensure that it is in the correct form.
* **Forgetting to Check for Continuity**: Always check if a function is continuous at a given point before evaluating its limit.

**Quick Summary**
-----------------

Calculus is a branch of mathematics that deals with the study of continuous change. Key concepts include limits, continuity, differentiation, and integration. The fundamental theorem of calculus states that differentiation and integration are inverse processes. Common pitfalls include incorrectly applying L'Hopital's rule and forgetting to check for continuity.

Note: This theory note has been created based on the provided source questions (Q1) and may not cover all possible concepts in calculus. Further study is recommended to ensure comprehensive understanding.