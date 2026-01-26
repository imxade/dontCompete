**Vector Spaces and Basis**
==========================

**Introduction**
---------------

A vector space is a set of vectors that can be added together and scaled (multiplied by numbers) to form new vectors within the same set. The concept of basis is crucial in understanding the structure of these spaces.

**Core Concepts**
----------------

### Definition 1: Vector Space

A **vector space**$V$ over a field $\mathbb{F}$ (usually $\mathbb{R}$ or $\mathbb{C}$) is a set of vectors that satisfies the following properties:

*   Closure under addition: For any $u, v \in V$, their sum $u + v$ is also in $V$.
*   Commutativity of addition: $u + v = v + u$ for all $u, v \in V$.
*   Associativity of addition: $(u + v) + w = u + (v + w)$ for all $u, v, w \in V$.
*   Existence of additive identity: There exists a vector $0_V \in V$ such that for any $u \in V$, $u + 0_V = u$.
*   Existence of additive inverse: For each $u \in V$, there exists a vector $-u \in V$ such that $u + (-u) = 0_V$.
*   Closure under scalar multiplication: For any $u \in V$ and $\alpha \in \mathbb{F}$, the product $\alpha u$ is also in $V$.
*   Distributivity of scalar multiplication over vector addition: For all $u, v \in V$ and $\alpha \in \mathbb{F}$, $\alpha(u + v) = \alpha u + \alpha v$.
*   Distributivity of scalar multiplication over scalar addition: For all $u \in V$ and $\alpha, \beta \in \mathbb{F}$, $(\alpha + \beta)u = \alpha u + \beta u$.
*   Scalar identity: There exists an element $1_\mathbb{F} \in \mathbb{F}$ such that for any $u \in V$, $1_\mathbb{F}u = u$.

### Definition 2: Basis

A **basis** of a vector space $V$ is a set of linearly independent vectors $\{v_1, v_2, ..., v_n\}$ such that every vector in $V$ can be expressed uniquely as a linear combination of these basis vectors.

### Theorem 1: Span and Basis

If $\{v_1, v_2, ..., v_n\}$ is a set of vectors in a vector space $V$, then the following are equivalent:

*   These vectors span $V$.
*   These vectors form a basis for $V$.

### Theorem 2: Dimension

The **dimension** of a vector space $V$, denoted by $\dim(V)$, is the number of vectors in any basis for $V$. If no such finite set exists, then $V$ has infinite dimension.

```mermaid
graph LR
    V[Vector Space] -->|spanned by {v_1,v_2,...,v_n}| B[Basis]
```

**Key Formulas/Theorems**
-------------------------

*   **Dimension formula**: If $\{v_1, v_2, ..., v_m\}$ and $\{w_1, w_2, ..., w_n\}$ are bases for a vector space $V$, then $m = n$ and any basis for $V$ has the same number of vectors.
*   **Linear independence test**: A set of vectors is linearly independent if and only if none of them can be expressed as a linear combination of the others.

**Problem Solving Patterns**
---------------------------

1.  **Checking Linear Independence**: To determine if a set of vectors is linearly independent, check if any vector in the set can be expressed as a linear combination of the others.
2.  **Finding Span and Basis**: Given a set of vectors, try to express every vector in the space as a linear combination of these vectors. If it's possible to do so uniquely, then the original set is a basis for the space.

**Examples with Solutions**
---------------------------

### Example 1

Suppose we have three vectors $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$, and $\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ in $\mathbb{R}^2$. Determine if they span $\mathbb{R}^2$.

```markdown
Let $v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, v_3 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.

To check if they span $\mathbb{R}^2$, we need to find out if any vector in $\mathbb{R}^2$ can be written as a linear combination of these vectors.

Suppose $v = \begin{pmatrix} x \\ y \end{pmatrix}$. Then, there exist scalars $\alpha_1, \alpha_2, \alpha_3$ such that:

$v = \alpha_1 v_1 + \alpha_2 v_2 + \alpha_3 v_3$

or

$\begin{pmatrix} x \\ y \end{pmatrix} = \alpha_1 \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \alpha_2 \begin{pmatrix} 0 \\ 1 \end{pmatrix} + \alpha_3 \begin{pmatrix} 2 \\ 1 \end{pmatrix}$

Simplifying, we get:

$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \alpha_1 + 2\alpha_3 \\ \alpha_2 + \alpha_3 \end{pmatrix}$

So,

$x = \alpha_1 + 2\alpha_3$
$y = \alpha_2 + \alpha_3$

Since we have two equations and three variables, it is possible to choose values for $\alpha_1$, $\alpha_2$, and $\alpha_3$ such that the above equation holds.

Therefore, these vectors do span $\mathbb{R}^2$.
```

### Example 2

Determine which of the following statements about a set of six vectors in $\mathbb{R}^4$ is FALSE?

1. Any four of these vectors form a basis for $\mathbb{R}^4$.
2. It is not necessary that these vectors span $\mathbb{R}^4$.
3. If $v_1, v_2, v_3, v_4, v_5, v_6$ spans $\mathbb{R}^4$, then it forms a basis of $\mathbb{R}^4$.
4. These vectors are not linearly independent.

Solution:

Any four of the six vectors will span but cannot be a basis for $\mathbb{R}^4$. Hence, statement (A) is FALSE.

```markdown
### Common Pitfalls

*   Forgetting to check if a set of vectors is closed under addition and scalar multiplication.
*   Failing to recognize that a set of linearly independent vectors can still span the entire space.
*   Misunderstanding the concept of dimension: it's not just about how many vectors are in a basis but also about the fact that any two bases for a vector space have the same number of vectors.

### Quick Summary

*   A vector space is a set of vectors closed under addition and scalar multiplication.
*   A basis of a vector space is a set of linearly independent vectors spanning the entire space.
*   The dimension of a vector space is the number of vectors in any basis for that space.
*   Spanning and being a basis are equivalent concepts.