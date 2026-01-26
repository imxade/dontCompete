**Polynomials and Roots**
=========================

### Introduction

Polynomials are expressions consisting of variables and coefficients combined using addition, subtraction, and multiplication. They play a vital role in algebraic equations, particularly in finding roots. In this note, we will delve into the world of polynomials, focusing on their properties, key formulas, problem-solving patterns, and examples.

### Core Concepts

*   **Polynomial**: An expression consisting of variables and coefficients combined using addition, subtraction, and multiplication.
*   **Degree of a Polynomial**: The highest power of the variable in the polynomial.
*   **Roots of a Polynomial**: Values that make the polynomial equal to zero.

### Key Formulas/Theorems

**1.** $P(z) = (z - r_1)(z - r_2)...(z - r_n)$ where $r_i$ are the roots of the polynomial.

**2.** If a polynomial has real coefficients, complex roots come in conjugate pairs.

**3.** The sum of the roots of a polynomial with leading coefficient 1 is equal to the negation of the coefficient of the second-highest degree term.

### Problem Solving Patterns

*   **Factorization**: Use known roots or patterns to factorize polynomials.
*   **Rational Root Theorem**: Identify possible rational roots using the theorem.
*   **Descartes' Rule of Signs**: Determine the maximum number of positive and negative real roots.

### Examples with Solutions

**Q1 (ID: ee_2021_12)**

Let $P(z) = 3z^2 - 4 + jz + jz^j + z^3$. Which one of the following is true?

(A) Conjugate $\{ P(\bar{z}) \} = P(z)$ for all $z$

(B) The sum of the roots of $P(z) = 0$ is a real number

(C) The complex roots of the equation $P(z) = 0$ come in conjugate pairs.

(D) All the roots cannot be real

Solution: 
Since $jz^j=z$, we have 
$$
\begin{aligned}
P(z)&=3z^2-4+jz+z^3\\&=(z^3+3z^2)+(-4+jz)
\end{aligned}
$$ 
The polynomial has complex coefficients, so the complex roots come in conjugate pairs. Therefore, (C) is incorrect.

Now consider $P(\bar{z})$, and note that $\overline{jz} = -j\bar{z}$ and $(jz^j)^{\wedge}=(j\bar{z}^{-j})$. Thus,
$$
\begin{aligned}
P(\bar{z})&=\left(\overline{z}\right)^3+3\left(\overline{z}\right)^2-4-j\overline{z}\\
&=\left[\overline{\left(z^3+3z^2\right)}\right]-4-\overline{jz}\\
&=\overline{(z^3+3z^2)} - 4 + j \bar{z}
\end{aligned}
$$ 
We can now compare $P(\bar{z})$ to $\overline{P(z)}$. Since the coefficients of both polynomials are real, we have
$$
\begin{aligned}
\overline{P(z)}&=\overline{(z^3+3z^2)+(-4+jz)}\\&=P(\bar{z})
\end{aligned}
$$ 
Thus (A) is correct.

We can also find the sum of roots directly. Let $\alpha_1,\ldots,\alpha_n$ denote the roots of $P(z)=0$, and let $\beta_i=\overline{\alpha_i}$ be their complex conjugates.
Since the polynomial has leading coefficient 3, we have 
$$
\begin{aligned}
z^3+3z^2&=z^3+(j-4) + \sum_{i=1}^{n}(z-\alpha_i)(z-\beta_i)
\end{aligned}
$$
where the last term represents the product of all pairs $(z-\alpha_i)$ and $(z-\beta_i)$, for $i=1,\ldots,n$.
Now we can expand both sides of this equation to get:
$$
\begin{aligned}
P(z)&=\left[\sum_{i=1}^{n}\left((z-\alpha_i)(z-\bar{\alpha}_i)\right)+j-4\right]\\
&=\left[\sum_{i=1}^{n}\left(\left(z-\alpha_i\right)^2+\left|\alpha_i\right|^2\right)+j-4\right].
\end{aligned}
$$

We can then group the terms with $z$ on one side:
$$
\begin{aligned}
P(z)&=\sum_{i=1}^{n}\left[\left(z-\alpha_i\right)^2+\left|\alpha_i\right|^2\right]+j-4\\&=(\sum_{i=1}^{n}(z-\alpha_i)^2)+j-4.
\end{aligned}
$$ 
Finally, we set $P(z)=0$ to obtain
$$
\begin{aligned}
0&=\left(\sum_{i=1}^n(z-\alpha_i)^2\right)+j-4\\
\Rightarrow \quad j-4&=-\sum_{i=1}^{n}(z-\alpha_i)^2.
\end{aligned}
$$

For any value of $z$, the sum $(z-\alpha_1)^2+\cdots+(z-\alpha_n)^2$ is real (because all its terms are real).
Thus, we conclude that the sum of roots is not a real number. Therefore, (B) is incorrect.
Finally, consider the possible values for the roots: if they were all real, then $\{P(z)\}$ would be real-valued and hence $(D)$ cannot happen.

### Common Pitfalls

*   Failure to recognize complex coefficients and their implications on root behavior.
*   Misapplication of Descartes' Rule of Signs or Rational Root Theorem without careful consideration of polynomial properties.
*   Incorrect handling of conjugate pairs in polynomial factorization.

### Quick Summary

*   **Key Formulas/Theorems**:
    *   $P(z) = (z - r_1)(z - r_2)...(z - r_n)$
    *   Complex roots come in conjugate pairs for polynomials with real coefficients.
    *   The sum of the roots is equal to the negation of the coefficient of the second-highest degree term.
*   **Problem Solving Patterns**:
    *   Factorization and rational root theorem application.
    *   Descartes' Rule of Signs for determining maximum real roots.

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve questions related to polynomials and roots.