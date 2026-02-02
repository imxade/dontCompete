**lti - Signal**
================

**Introduction**
---------------

The Exponential Fourier Series (EFS) representation of a continuous-time periodic signal is a fundamental concept in Signals and Systems. It provides an efficient way to represent signals using complex exponentials, making it easier to analyze and manipulate them.

**Core Concepts**
-----------------

A continuous-time periodic signal `x(t)` with period `T_0` can be represented as:

$$x(t) = \sum_{k=-\infty}^{\infty} a_k e^{j k \omega_0 t}$$

where:

* $\omega_0$ is the fundamental angular frequency, given by $\omega_0 = \frac{2\pi}{T_0}$.
* $a_k$ are the complex coefficients of the series.

**Key Formulas/Theorems**
-------------------------

The average value of a signal `x(t)` over one period is given by:

$$\bar{x} = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} x(t) dt$$

The average power of a signal `x(t)` is given by:

$$P_x = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} |x(t)|^2 dt$$

**Problem Solving Patterns**
---------------------------

* Given the EFS representation, find the average value and power of the signal.
* Use the given coefficients to calculate the sum of the series.

**Examples with Solutions**
---------------------------

### Example 1:

Given that `x(t)` is a real and even signal with fundamental period `T_0 = 6` sec, and its EFS representation is:

$$x(t) = \sum_{k=-\infty}^{\infty} a_k e^{j k \omega_0 t}$$

where $\omega_0 = \frac{2\pi}{T_0}$.

* Find the average value of `x(t)` over one period.
* Find the average power of `x(t)` over one period.

### Solution:

First, find the average value:

$$\bar{x} = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} x(t) dt = \frac{1}{6} \left[ a_0 + 2a_1 e^{j \omega_0 t}\right]$$

Since `x(t)` is even, the average value will be:

$$\bar{x} = a_0$$

Given that the average value of `x(t)` is 2, we have:

$$a_0 = 2$$

Next, find the average power:

$$P_x = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} |x(t)|^2 dt = \frac{1}{6} \sum_{k=-\infty}^{\infty} k^2 a_k^2$$

Given that:

$$a_k = \begin{cases} 3, & k=1 \\ -1, & k=3 \\ 0, & \text{otherwise}\end{cases}$$

we have:

$$P_x = \frac{1}{6} (9 + 9) = \frac{18}{6} = 3.00$$

### Example 2:

Given that `x(t)` is a real and even signal with fundamental period `T_0 = 6` sec, and its EFS representation is:

$$x(t) = \sum_{k=-\infty}^{\infty} a_k e^{j k \omega_0 t}$$

where $\omega_0 = \frac{2\pi}{T_0}$.

* Find the average value of `x(t)` over one period.
* Find the average power of `x(t)` over one period.

### Solution:

First, find the average value:

$$\bar{x} = a_0$$

Given that the average value of `x(t)` is 2, we have:

$$a_0 = 2$$

Next, find the average power:

$$P_x = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} |x(t)|^2 dt = \frac{1}{6} \sum_{k=-\infty}^{\infty} k^2 a_k^2$$

Given that:

$$a_k = \begin{cases} 3, & k=1 \\ -1, & k=3 \\ 0, & \text{otherwise}\end{cases}$$

we have:

$$P_x = \frac{1}{6} (9 + 9) = \frac{18}{6} = 3.00$$

**Common Pitfalls**
------------------

* Forget to use the fundamental period `T_0` in calculations.
* Fail to consider that the signal is real and even.
* Ignore the given coefficients and their implications.

**Quick Summary**
-----------------

* EFS representation of a periodic signal: $x(t) = \sum_{k=-\infty}^{\infty} a_k e^{j k \omega_0 t}$.
* Average value of `x(t)` over one period: $\bar{x} = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} x(t) dt$.
* Average power of `x(t)` over one period: $P_x = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} |x(t)|^2 dt$.