**Contour Integration**
=======================

**Introduction**
---------------

Contour integration is a fundamental technique in complex analysis that allows us to evaluate definite integrals by integrating over a closed curve in the complex plane. This method has far-reaching applications in various branches of mathematics and physics.

**Core Concepts**
-----------------

### Complex Line Integrals

A complex line integral is defined as:

$$\int_{C} f(z) dz$$

where $f(z)$ is a complex function, and $C$ is a simple closed path in the complex plane. The integral can be evaluated by parameterizing the curve $C$ and integrating with respect to the parameter.

### Cauchy-Goursat Theorem

The Cauchy-Goursat theorem states that if a function $f(z)$ is analytic within and on a simple closed path $C$, then the line integral of $f(z)$ over $C$ is zero:

$$\int_{C} f(z) dz = 0$$

### Laurent Series Expansion

A function $f(z)$ can be expanded in a Laurent series around an isolated singularity at $z=a$ as:

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-a)^n$$

where the coefficients $a_n$ are determined by the residues of the function at the singularity.

### Residue Theorem

The residue theorem states that if a function $f(z)$ has a simple pole at $z=a$, then the line integral of $f(z)$ over a closed curve surrounding the pole is given by:

$$\int_{C} f(z) dz = 2 \pi i \text{Res}(f, a)$$

where $\text{Res}(f, a)$ is the residue of $f$ at $z=a$.

**Key Formulas/Theorems**
-------------------------

*   Cauchy-Goursat theorem: $\int_{C} f(z) dz = 0$
*   Laurent series expansion: $f(z) = \sum_{n=-\infty}^{\infty} a_n (z-a)^n$
*   Residue theorem: $\int_{C} f(z) dz = 2 \pi i \text{Res}(f, a)$

**Problem Solving Patterns**
---------------------------

### Identifying Singularities

When evaluating contour integrals, it is crucial to identify the singularities of the function within and on the closed path. The type of singularity (pole, essential, etc.) determines the approach used to evaluate the integral.

### Applying Residue Theorem

If a function has simple poles within and on the closed path, apply the residue theorem to evaluate the line integral.

### Using Laurent Series Expansion

For functions with essential singularities or non-simple poles, expand the function in a Laurent series around the singularity and integrate term by term.

**Examples with Solutions**
---------------------------

*   Evaluate $\int_{C} \frac{1}{z^2+1} dz$, where $C$ is a circle centered at the origin of radius 2.
    *   Identify the singularities: The function has simple poles at $z=\pm i$ within and on the closed path.
    *   Apply the residue theorem:

$$\int_{C} \frac{1}{z^2+1} dz = 2 \pi i \left(\text{Res}\left(\frac{1}{z^2+1}, i\right) + \text{Res}\left(\frac{1}{z^2+1}, -i\right)\right)$$

    *   Evaluate the residues:

$$\text{Res}\left(\frac{1}{z^2+1}, i\right) = \lim_{z \to i} (z-i) \frac{1}{(z+i)(z-i)} = \frac{1}{2i}$$

$$\text{Res}\left(\frac{1}{z^2+1}, -i\right) = \lim_{z \to -i} (z+i) \frac{1}{(z+i)(z-i)} = \frac{-1}{2i}$$

    *   Substitute the residues into the residue theorem:

$$\int_{C} \frac{1}{z^2+1} dz = 2 \pi i \left(\frac{1}{2i} - \frac{1}{2i}\right) = 0$$
*   Evaluate $\int_{C} e^z dz$, where $C$ is a circle centered at the origin of radius 2.
    *   Expand the function in a Laurent series around the origin:

$$e^z = \sum_{n=0}^{\infty} \frac{z^n}{n!}$$

    *   Integrate term by term:

$$\int_{C} e^z dz = \int_{C} \left(\sum_{n=0}^{\infty} \frac{z^n}{n!}\right) dz$$

$$= \sum_{n=0}^{\infty} \frac{1}{n!} \int_{C} z^n dz$$

    *   Evaluate the integral:

$$\int_{C} z^n dz = 2 \pi i r^n \text{ if } n>0$$

$$\int_{C} z^n dz = 2 \pi i r^{-n-1} \text{ if } n<0$$

    *   Substitute the integral into the series:

$$\int_{C} e^z dz = \sum_{n=0}^{\infty} \frac{1}{n!} (2 \pi i r^n)$$

$$+ \sum_{n=-\infty}^{-1} \frac{1}{n!} (2 \pi i r^{-n-1})$$

    *   Simplify the series:

$$\int_{C} e^z dz = 2 \pi i \left(1 + \frac{r}{1!} + \frac{r^2}{2!} + \dotsb\right)$$

$$+ 2 \pi i \left(\frac{-1}{-2} + \frac{-r^{-3}}{(-3)!} + \frac{-r^{-5}}{(-5)!} + \dotsb\right)$$

    *   Simplify further:

$$\int_{C} e^z dz = 2 \pi i (1 - r^{-2})$$

**Common Pitfalls**
------------------

*   Failing to identify singularities within and on the closed path.
*   Misapplying the residue theorem or Laurent series expansion.
*   Not considering essential singularities or non-simple poles.

**Quick Summary**
-----------------

### Key Concepts:

*   Complex line integrals
*   Cauchy-Goursat theorem
*   Laurent series expansion
*   Residue theorem

### Problem Solving Patterns:

*   Identifying singularities within and on the closed path
*   Applying the residue theorem or Laurent series expansion
*   Integrating term by term for essential singularities or non-simple poles