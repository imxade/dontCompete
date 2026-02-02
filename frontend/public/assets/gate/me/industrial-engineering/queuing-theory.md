**Queuing Theory**
================

### Introduction
---------------

Queuing theory is a branch of industrial engineering that deals with the study of waiting lines, or queues. It provides mathematical models to analyze and optimize the behavior of systems where customers arrive at a service facility and wait in line for service.

### Core Concepts
-----------------

#### Arrival Process
-------------------

The arrival process is a fundamental concept in queuing theory. It describes how customers arrive at the service facility over time. The most common arrival processes are:

* **Poisson Distribution**: A discrete distribution that models the number of events occurring within a fixed interval. In this context, it models the number of customers arriving at the service facility per hour.
	+ Mean Arrival Rate (μ): average rate at which customers arrive per unit time
	+ Standard Deviation (σ): square root of the variance of the arrival process

#### Service Process
-------------------

The service process describes how the service facility serves customers. It can be modeled using various distributions, such as:

* **Exponential Distribution**: A continuous distribution that models the time between arrivals or service completion.

### Key Formulas/Theorems
-------------------------

**Poisson Distribution Formula**

$$P(N(t) = k) = \frac{(\mu t)^k e^{-\mu t}}{k!}$$

where:

* $N(t)$ is the number of customers arriving in time interval $t$
* $\mu$ is the mean arrival rate
* $k$ is the number of customers arriving in time interval $t$

**Exponential Distribution Formula**

$$P(X \leq x) = 1 - e^{-\lambda x}$$

where:

* $X$ is the time between arrivals or service completion
* $\lambda$ is the rate parameter (mean reciprocal)

### Problem Solving Patterns
---------------------------

To solve queuing theory problems, follow these steps:

1. Identify the arrival and service processes.
2. Determine the relevant parameters (e.g., mean arrival rate, service rate).
3. Use the formulas mentioned above to calculate the desired probabilities or quantities.

**Problem Example**

Suppose customers arrive at a shop according to the Poisson distribution with a mean of 10 customers/hour. The manager notes that no customer arrives for the first 3 minutes after the shop opens. What is the probability that a customer arrives within the next 3 minutes?

Solution:

* Identify the arrival process: Poisson distribution
* Determine the relevant parameters:
	+ Mean arrival rate (μ): 10 customers/hour = 0.17 customers/minute
	+ Time interval: 3 minutes
* Calculate the probability using the Poisson distribution formula:

$$P(N(3) \geq 1) = 1 - P(N(3) = 0)$$

$$= 1 - e^{-\mu t}$$

$$= 1 - e^{-0.17 \times 3}$$

$$≈ 0.39$$

### Examples with Solutions
---------------------------

| Question | Solution |
| --- | --- |
| Q1 (ID: me_2021-M_13) | See above |

### Common Pitfalls
-------------------

* Failing to identify the arrival and service processes.
* Incorrectly applying formulas or parameters.

### Quick Summary
-----------------

* Poisson distribution models arrival process
* Exponential distribution models service process
* Key formulas:
	+ Poisson: $P(N(t) = k) = \frac{(\mu t)^k e^{-\mu t}}{k!}$
	+ Exponential: $P(X \leq x) = 1 - e^{-\lambda x}$