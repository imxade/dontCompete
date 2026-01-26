**Numerical Methods: Least Square Approximation**
==============================================

**Introduction**
---------------

Least square approximation is a method used to find the best fit line that minimizes the sum of the squared errors between observed data points and the predicted values. This technique is essential in various fields, including mathematics, statistics, and engineering.

**Core Concepts**
-----------------

* **Best Fit Line**: A straight line that minimizes the sum of the squared errors between observed data points and the predicted values.
* **Least Square Error (LSE)**: The average squared difference between observed data points and the predicted values.
* **Regression Analysis**: A statistical method to establish a relationship between variables using linear or non-linear models.

**Key Formulas/Theorems**
-------------------------

The best fit line in the least square sense is given by:

$$y = ax + b$$

where $a$ is the slope of the line and $b$ is the y-intercept. The equations for minimizing the LSE are:

$$\sum_{i=1}^n (x_i \hat{y}_i) - n \bar{x} \bar{\hat{y}} = 0$$

$$\sum_{i=1}^n x_i^2 - n \bar{x}^2 = 0$$

where $\hat{y}_i$ is the predicted value of $y$ for data point $i$, and $\bar{x}$ and $\bar{\hat{y}}$ are the means of $x$ and $\hat{y}$, respectively.

**Problem Solving Patterns**
---------------------------

1. **Given Data Points**: Use the given data points to calculate the sums required in the LSE equations.
2. **Setup Equations**: Substitute the calculated values into the LSE equations.
3. **Solve for a and b**: Solve the resulting system of linear equations for $a$ and $b$.

**Examples with Solutions**
---------------------------

### Example 1

Given data points: $(x_1, y_1) = (0, 2), (x_2, y_2) = (1, 3)$

| $x_i$ | $y_i$ |
| --- | --- |
| $0$   | $2$  |
| $1$   | $3$  |

Calculate the sums required in the LSE equations:

$$\sum_{i=1}^n x_i \hat{y}_i = 0 \cdot 2 + 1 \cdot 3 = 3$$

$$\sum_{i=1}^n y_i = 2 + 3 = 5$$

$$\bar{x} = (0 + 1)/2 = 0.5$$

$$\hat{y}_1 = a(0) + b = b$$

$$\hat{y}_2 = a(1) + b = a + b$$

Substitute these values into the LSE equations:

$$3 - n \bar{x} (a + b) = 0$$

$$5 - n (\bar{x})^2 = 0$$

Solve for $a$ and $b$:

```mermaid
graph LR;
A[(3 - 2(0.5)(a+b))]-->B[(=0)];
C[(5-(0.5)^2)]-->D[(=0)];
```

### Example 2 (Source Question: ee_2023_35)

Given data points: $(-1, 0.8), (0, 2.2)$ and $(1, 2.8)$. Find the value of the slope of the best fit straight line in the least square sense.

| $x_i$ | $y_i$ |
| --- | --- |
| -1   | 0.8  |
| 0    | 2.2  |
| 1    | 2.8  |

Calculate the sums required in the LSE equations:

$$\sum_{i=1}^n x_i \hat{y}_i = (-1)(0.8) + 0(2.2) + (1)(2.8) = 1.0$$

$$\sum_{i=1}^n y_i = 0.8 + 2.2 + 2.8 = 5.8$$

$$\bar{x} = (-1 + 0 + 1)/3 = 0$$

$$\hat{y}_1 = a(-1) + b = -a + b$$

$$\hat{y}_2 = a(0) + b = b$$

$$\hat{y}_3 = a(1) + b = a + b$$

Substitute these values into the LSE equations:

$$1.0 - n \bar{x} (a + b) = 0$$

$$5.8 - n (\bar{x})^2 = 0$$

Solve for $a$ and $b$:

```mermaid
graph LR;
A[(1-3(0)(a+b))]-->B[(=0)];
C[(5.8-(0)^2)]-->D[(=0)];
```

**Common Pitfalls**
-------------------

* **Failing to calculate the correct sums**: Make sure to carefully calculate the required sums for each data point.
* **Solving the wrong system of equations**: Double-check that you are solving the correct system of equations.

**Quick Summary**
-----------------

* Least square approximation is a method used to find the best fit line that minimizes the sum of the squared errors between observed data points and the predicted values.
* The best fit line in the least square sense is given by: $y = ax + b$
* Use the LSE equations to solve for $a$ and $b$: $\sum_{i=1}^n (x_i \hat{y}_i) - n \bar{x} \bar{\hat{y}} = 0$ and $\sum_{i=1}^n x_i^2 - n \bar{x}^2 = 0$
* Carefully calculate the required sums for each data point, and solve the correct system of equations.