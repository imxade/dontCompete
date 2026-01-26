**Continuous Random Variable - Theory Note**
======================================

### Introduction
---------------

In this section, we'll explore continuous random variables and their applications in communication systems. A continuous random variable takes on a range of values within a given interval or domain.

### Core Concepts
-----------------

#### Definition

A continuous random variable is a function that assigns a real value to each possible outcome of an experiment. The probability density function (PDF) of a continuous random variable describes the likelihood of observing a particular value.

**Probability Density Function**

Given a continuous random variable `X` with PDF `f(x)`, we have:

$$ P(X \in A) = \int_A f(x) dx $$

where `A` is an interval or region in the domain of `X`.

#### Uniform Distribution

In this theory note, we focus on uniform distributions, where every value within a specified range has an equal probability.

**Uniform PDF**

For a random variable `X` with a uniform distribution over `[a, b]`, its PDF is given by:

$$ f(x) = \begin{cases} 
\frac{1}{b-a} & a < x < b \\
0 & \text{otherwise}
\end{cases} $$

#### Independence of Random Variables

In this problem, `X` and `Y` are independent continuous random variables. This means that the occurrence or value of one does not affect the probability distribution of the other.

**Joint PDF**

When two random variables are independent, their joint PDF is the product of their individual PDFs:

$$ f_{XY}(x,y) = f_X(x) \cdot f_Y(y) $$

### Key Formulas/Theorems
-------------------------

#### Joint Probability for Continuous Random Variables

Given independent continuous random variables `X` and `Y`, we can compute the joint probability of an event `A` as:

$$ P(A) = \int_{x \in A} f_X(x) dx \cdot \int_{y \in B} f_Y(y) dy $$

where `B` is a region defined by the conditions in `A`.

### Problem Solving Patterns
---------------------------

#### Identifying Uniform Distributions

When dealing with uniform distributions, ensure you identify the range `[a, b]` and apply the corresponding PDF.

**Example**: The given problem involves two uniform random variables. Identify their ranges and calculate their joint probability.

### Examples with Solutions
---------------------------

**Problem 1**

Given `X ∼ U(2,3)` and `Y ∼ U(1,4)`, compute:

$$ P(Y > X \leq 2) $$

**Solution**

We first identify the range of `X` (2, 3) and its PDF. Then we calculate the joint probability for the condition `Y > X ≤ 2`.

```mermaid
graph LR;
A[X=2] --> B[X≤2] --> C[Y>2];
```

We integrate over the specified intervals using the given PDFs:

$$ P(Y > X \leq 2) = \int_2^3 f_X(x) dx \cdot \int_{x+1}^4 f_Y(y) dy $$

Substituting the uniform PDF formula and integrating, we get:

$$ P(Y > X \leq 2) = 0.5 \cdot (2-1) = 0.5 $$

### Common Pitfalls
-------------------

*   Failing to identify uniform distributions or applying incorrect formulas.
*   Misinterpreting independence or joint probability calculations.

### Quick Summary
------------------

*   **Continuous Random Variables**: Take on real values within an interval or domain.
*   **Uniform Distribution**: Every value within a specified range has equal probability.
*   **Independence of Random Variables**: Two variables are independent if their occurrence or value does not affect each other's probability distribution.
*   **Key Formulas/Theorems**:
    *   Joint PDF for two independent random variables: $f_{XY}(x,y) = f_X(x) \cdot f_Y(y)$
    *   Joint probability for continuous random variables: $P(A) = \int_{x \in A} f_X(x) dx \cdot \int_{y \in B} f_Y(y) dy$