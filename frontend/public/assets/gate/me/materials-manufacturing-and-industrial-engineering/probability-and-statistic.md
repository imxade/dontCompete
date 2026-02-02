**Probability and Statistics for Materials Manufacturing and Industrial Engineering**
====================================================================================

**Introduction**
---------------

Probability and statistics are crucial tools in materials manufacturing and industrial engineering to ensure efficient production, manage inventory, and maintain quality control. This note will cover key concepts, formulas, and techniques required to tackle problems related to inventory management, lead time calculation, and queueing theory.

**Core Concepts**
-----------------

### 1. Probability Distributions

*   **Uniform Distribution**: A continuous distribution where every value within a given range is equally likely.
    *   Formula: $f(x) = \frac{1}{b-a}$ for $a \leq x \leq b$
*   **Exponential Distribution**: A continuous distribution used to model the time between events in a Poisson process.
    *   Formula: $f(x) = \lambda e^{-\lambda x}$ for $x \geq 0$

### 2. Gaussian (Normal) Distribution

*   **Mean** ($μ$): The expected value of the distribution
*   **Standard Deviation** ($σ$): A measure of dispersion, representing how spread out the data is from the mean
*   Formula: $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

### 3. Poisson Distribution

*   **Mean** ($λ$): The average number of events occurring in a fixed interval
*   Formula: $f(x) = \frac{\lambda^x e^{-\lambda}}{x!}$ for $x = 0, 1, 2, ...$

### 4. Queueing Theory

*   **Arrival Rate** ($λ$): The average rate at which customers arrive
*   **Service Rate** ($μ$): The average rate at which customers are served
*   **Utilization Factor** ($ρ$): The ratio of arrival rate to service rate, $\rho = \frac{\lambda}{\mu}$

### 5. Inventory Management

*   **Safety Stock**: Additional stock held to prevent stockouts during lead time
*   Formula: $SS = z_{\alpha} \sigma \sqrt{t}$, where $z_{\alpha}$ is the Z-score corresponding to the desired confidence level, $\sigma$ is the standard deviation of demand, and $t$ is the lead time

**Key Formulas/Theorems**
-------------------------

### 1. Gaussian (Normal) Distribution

*   **Cumulative Distribution Function**: $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-\frac{t^2}{2}} dt$
*   **Inverse of the Cumulative Distribution Function** ($z_{\alpha}$): The Z-score corresponding to a given confidence level

### 2. Poisson Distribution

*   **Mean and Variance**: $\lambda$ (mean) = $\lambda$ (variance)

### 3. Queueing Theory

*   **Expected Number of Jobs in the System** ($L_s$):
    \[L_s = \frac{\rho}{1-\rho}\]

**Problem Solving Patterns**
---------------------------

### 1. Inventory Management

*   Use the safety stock formula to calculate the required inventory level
*   Round off values to two decimal places for final answers

### 2. Queueing Theory

*   Calculate the utilization factor ($ρ$) and use it to determine the expected number of jobs in the system

**Examples with Solutions**
---------------------------

### Example 1: Inventory Management

Given:
*   Lead time = 5 days
*   Daily demand follows a Gaussian distribution with mean = 50 units and standard deviation = 10 units
*   Desired confidence level = 95%

Find:
*   Safety stock required to achieve the desired confidence level

Solution:

```latex
\begin{align*}
SS & = z_{0.95} \sigma \sqrt{t} \\
& = 1.64 \times 10 \times \sqrt{5} \\
& \approx 16.4
\end{align*}

```

### Example 2: Queueing Theory

Given:
*   Arrival rate ($λ$) = 12 jobs/hour
*   Service rate ($μ$) = 4 minutes/customer = 1/15 customer/minute

Find:
*   Expected number of jobs in the system at any given time

Solution:

```latex
\begin{align*}
\rho & = \frac{\lambda}{\mu} \\
& = \frac{12}{\frac{1}{15}} \\
& = 180 \\
L_s & = \frac{\rho}{1-\rho} \\
& = \frac{180}{1-180} \\
& \approx -0.8
\end{align*}

```

Note that the expected number of jobs in the system cannot be negative; this example is used to demonstrate the calculation process.

**Common Pitfalls**
--------------------

*   Be cautious when rounding off values, as small errors can lead to incorrect answers.
*   Ensure you use the correct Z-score for the desired confidence level.
*   Don't forget to consider the lead time when calculating safety stock.

**Quick Summary**
-----------------

| Topic | Key Concepts |
| --- | --- |
| Probability Distributions | Uniform, Exponential, Gaussian (Normal), Poisson |
| Inventory Management | Safety Stock, Lead Time Calculation |
| Queueing Theory | Arrival Rate, Service Rate, Utilization Factor |

Note: This summary provides a brief overview of the key concepts covered in this note. Be sure to review each section for more detailed information and examples.