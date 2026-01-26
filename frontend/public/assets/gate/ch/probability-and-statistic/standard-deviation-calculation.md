**Standard Deviation Calculation**
=====================================

**Introduction**
---------------

The standard deviation of a probability distribution is a measure of the amount of variation or dispersion from the average. It's essential to understand how to calculate it, especially when dealing with random samples and sample means.

**Core Concepts**
-----------------

### Definition

The standard deviation of a population (σ) is defined as:

$$\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}$$

where:
- $x_i$ are the individual data points
- $\mu$ is the mean of the population
- $N$ is the total number of data points

For a sample, we use the sample standard deviation (s) instead:

$$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

where:
- $x_i$ are the individual data points
- $\bar{x}$ is the sample mean
- $n$ is the sample size

### Sampling Distribution of the Sample Mean

When taking random samples from a population, the distribution of sample means follows a normal distribution. The mean of this distribution is equal to the population mean ($\mu$), and its standard deviation is called the standard error (SE):

$$SE = \frac{\sigma}{\sqrt{n}}$$

**Key Formulas/Theorems**
-------------------------

### Standard Deviation of the Sample Mean

Given a sample of size $n$, the standard deviation of the sample mean ($s_{\bar{x}}$) is:

$$s_{\bar{x}} = \frac{s}{\sqrt{n}}$$

where:
- $s$ is the sample standard deviation
- $n$ is the sample size

**Problem Solving Patterns**
---------------------------

When dealing with problems like GATE 2021 Question 38, follow these steps:

1. **Understand the given distribution**: Analyze the probability distribution function (PDF) or cumulative distribution function (CDF).
2. **Identify the population standard deviation**: Use the given PDF to find the population variance ($\sigma^2$), and then take its square root to get $\sigma$.
3. **Calculate the sample size and mean**: Find the sample size ($n$) and the sample mean ($\bar{x}$).
4. **Apply the formula for standard deviation of the sample mean**: Use $s_{\bar{x}} = \frac{s}{\sqrt{n}}$ to find the answer.

**Examples with Solutions**
---------------------------

Let's use GATE 2021 Question 38 as an example:

Given the PDF:
$f(x) = 0.5$ for $-3 < x < 3$

We need to find the standard deviation of the sample mean ($s_{\bar{x}}$).

First, we calculate the population variance:

$$\sigma^2 = \int_{-3}^{3} (x - 1)^2 f(x) dx = \frac{1}{0.5} \int_{-3}^{3} (x - 1)^2 dx = \frac{16}{3}$$

Then, we find the population standard deviation:

$$\sigma = \sqrt{\frac{16}{3}} = \frac{4}{\sqrt{3}} \approx 2.309$$

Next, let's assume a sample size of $n = 68$ and calculate the standard error:

$$SE = \frac{\sigma}{\sqrt{n}} = \frac{2.309}{\sqrt{68}} \approx 0.07$$

Now, we can find the standard deviation of the sample mean:

$$s_{\bar{x}} = SE = 0.07$$

Rounding off to three decimal places, we get $s_{\bar{x}}$ as **0.069 to 0.071**.

**Common Pitfalls**
-------------------

- Don't confuse the population standard deviation ($\sigma$) with the sample standard deviation (s).
- When dealing with a probability distribution, ensure you understand its properties and how it relates to the sample mean.
- Be careful when calculating the standard error (SE), as it depends on both $\sigma$ and $n$.

**Quick Summary**
-----------------

* Population standard deviation ($\sigma$): $\sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}$
* Sample standard deviation (s): $\sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$
* Standard error (SE): $SE = \frac{\sigma}{\sqrt{n}}$

**References**

For further reading, consult probability and statistics textbooks or online resources:

* [Wikipedia: Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation)
* [Khan Academy: Statistics](https://www.khanacademy.org/math/statistics-probability)