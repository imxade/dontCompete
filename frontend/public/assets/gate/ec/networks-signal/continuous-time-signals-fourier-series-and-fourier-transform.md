**Continuous Time Signals Fourier Series and Fourier Transform**
===========================================================

**Introduction**
---------------

In this section, we will cover the essential concepts of continuous time signals, their representation using Fourier series and transform. This is a fundamental topic in Signal Processing and Network Analysis.

**Core Concepts**
-----------------

### Periodic Continuous-Time Signals

A periodic signal x(t) has a period T such that:

x(t) = x(t + T), ∀ t ∈ R

The minimum value of the period is called the fundamental period, denoted as T0.

### Fourier Series Representation

Any periodic continuous-time signal can be represented as:

x(t) = ∑[a_k cos(ω_0 k t) + b_k sin(ω_0 k t)], k=1→∞

where a_k and b_k are the Fourier coefficients, and ω_0 is the fundamental frequency.

### Fourier Transform

The Fourier transform of a continuous-time signal x(t) is given by:

X(jω) = ∫(-∞→∞) x(t)e^{-jωt}dt

The inverse Fourier transform is:

x(t) = (1/2π) ∫(-∞→∞) X(jω)e^{jωt}dω

**Key Formulas/Theorems**
-------------------------

### Linearity of the Fourier Transform

Given two signals x_1(t) and x_2(t), their sum is also a signal:

x(t) = x_1(t) + x_2(t)

The Fourier transform of the sum is the sum of the individual transforms:

X(jω) = X_1(jω) + X_2(jω)

### Convolution Property

The convolution of two signals in time domain corresponds to multiplication in frequency domain:

x(t) \* h(t) ⇌ X(jω)H(jω)

where H(jω) is the Fourier transform of the impulse response h(t).

### Parseval's Theorem

The energy of a signal in time domain is equal to its energy in frequency domain:

∫(-∞→∞) |x(t)|^2dt = (1/2π) ∫(-∞→∞) |X(jω)|^2dω

**Problem Solving Patterns**
---------------------------

When solving problems related to Fourier series and transform, follow these steps:

1.  Identify the signal type (periodic or aperiodic).
2.  Determine if the signal can be represented using Fourier series or transform.
3.  Apply linearity of the Fourier transform as needed.
4.  Use convolution property for filtering.
5.  Verify Parseval's theorem.

**Examples with Solutions**
---------------------------

### Example 1

Find the Fourier series representation of a periodic signal x(t) = sin(2πt/T), where T is the period.

Solution:

The fundamental frequency ω_0 = 2π/T.

x(t) = ∑[a_k cos(ω_0 k t) + b_k sin(ω_0 k t)], k=1→∞

Using Euler's formula, we get:

x(t) = ∑[(cos(kω_0t) - jsin(kω_0t))/j] = ∑[sin(kω_0t)]

The only non-zero term is when k=1, and a_1 = 1.

Therefore, the Fourier series representation of x(t) is:

x(t) = sin(2πt/T)

### Example 2

Find the convolution of two signals x(t) = e^(-at)u(t) and h(t) = δ(t - τ), where u(t) is the unit step function, a is a positive constant, and τ is a delay.

Solution:

The Fourier transform of x(t) is:

X(jω) = (1/(a + jω))

The Fourier transform of h(t) is:

H(jω) = e^{-jωτ}

Using the convolution property, we get:

x(t) \* h(t) ⇌ X(jω)H(jω)

Therefore, the convolution of x(t) and h(t) in time domain is:

x(t) \* h(t) = ∫(-∞→∞) e^(-(a + j(ω-t))/2)u(t - τ)dτ

**Common Pitfalls**
-------------------

1.  Confusing Fourier series with Fourier transform.
2.  Not applying the linearity of the Fourier transform correctly.
3.  Forgetting to use Parseval's theorem.

**Quick Summary**
------------------

Key points covered:

*   Periodic and aperiodic continuous-time signals
*   Fourier series representation
*   Linearity of the Fourier transform
*   Convolution property
*   Parseval's theorem

Focus on these concepts and practice solving problems to excel in this topic.