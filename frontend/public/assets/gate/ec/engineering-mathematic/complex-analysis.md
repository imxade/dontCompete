**Complex Analysis for GATE CS Exam**
=====================================

**Introduction**
---------------

Complex analysis is a branch of mathematics that deals with functions of complex numbers. It has numerous applications in engineering, physics, and computer science. In this note, we will cover the essential concepts, formulas, and techniques required to tackle complex analysis problems in the GATE CS exam.

**Core Concepts**
-----------------

* **Complex Numbers**: A complex number is a number that can be expressed in the form $a + bj$, where $a$ and $b$ are real numbers and $j = \sqrt{-1}$.
* **Poles and Zeros**: The poles of a function are the values of $s$ that make the function undefined, while the zeros are the values of $s$ that make the function zero. In the context of rational functions, poles occur at the roots of the denominator, while zeros occur at the roots of the numerator.
* **Residues**: The residue of a function at a pole is a measure of how "sharp" the pole is.

**Key Formulas/Theorems**
-------------------------

### Laurent Series Expansion

The Laurent series expansion of a function $f(s)$ around a point $s_0$ is given by:

$$f(s) = \sum_{n=-\infty}^{\infty} c_n (s-s_0)^n$$

where the coefficients $c_n$ are determined by the residues.

### Residue Theorem

The residue theorem states that if a function $f(s)$ has a pole at $s=s_0$, then:

$$\oint_{C} f(s) ds = 2 \pi i \cdot (\text{Res}(f, s_0))$$

where $\oint_C$ is the contour integral around a closed curve $C$ enclosing the pole.

### Argument Principle

The argument principle states that if a function $f(s)$ has a simple pole at $s=s_0$, then:

$$\Delta \arg f(s) = 2 \pi (\text{Number of zeros} - \text{Number of poles})$$

where $\Delta \arg$ is the change in the argument of $f(s)$ as $s$ traverses a closed curve.

**Problem Solving Patterns**
---------------------------

1. **Identify Poles and Zeros**: Start by identifying the poles and zeros of the function.
2. **Use Laurent Series Expansion**: Expand the function around each pole to determine its residue.
3. **Apply Residue Theorem**: Use the residue theorem to evaluate contour integrals.

**Examples with Solutions**
-------------------------

### Example 1: Evaluate $\oint_{C} \frac{z}{(z-1)(z-2)} dz$ where $C$ is a circle centered at 0 and radius 3.

Solution:

* Identify poles: The function has two poles, $s=1$ and $s=2$.
* Use Laurent series expansion:
$$\frac{z}{(z-1)(z-2)} = \frac{-1}{z-1} + \frac{1}{z-2}$$
* Apply residue theorem:
$$\oint_C f(s) ds = 2 \pi i \cdot (\text{Res}(f, s=1)) + 2 \pi i \cdot (\text{Res}(f, s=2))$$

### Example 2: Evaluate $\Delta \arg (z^2+1)$ as $z$ traverses a circle centered at 0 and radius 3.

Solution:

* Identify poles: The function has two simple poles, $s=j$ and $s=-j$.
* Apply argument principle:
$$\Delta \arg f(s) = 2 \pi (\text{Number of zeros} - \text{Number of poles}) = 4 \pi$$

**Common Pitfalls**
------------------

1. **Incorrect Identification of Poles**: Make sure to identify all the poles and zeros correctly.
2. **Failure to Apply Laurent Series Expansion**: Use the Laurent series expansion to simplify the function around each pole.

**Quick Summary**
-----------------

* Complex numbers: $a + bj$
* Poles and zeros: $\frac{1}{s-p}$, $\frac{s-p_0}{(s-p_1)(s-p_2)...}$
* Residues: Laurent series expansion
* Residue theorem: $\oint_C f(s) ds = 2 \pi i \cdot (\text{Res}(f, s_0))$
* Argument principle: $\Delta \arg f(s) = 2 \pi (\text{Number of zeros} - \text{Number of poles})$