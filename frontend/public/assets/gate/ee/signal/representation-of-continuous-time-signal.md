**Representation of Continuous-Time Signals**
=====================================================

**Introduction**
---------------

Continuous-time signals are an essential part of signal processing, representing real-world phenomena such as audio, images, and physical measurements. In this note, we will cover the representation of continuous-time signals, including energy calculations and scaling properties.

**Core Concepts**
-----------------

A **continuous-time signal**, denoted by $x(t)$, is a function that maps time $t$ to an amplitude in the real or complex numbers. The **energy** of a continuous-time signal, denoted by $E$, is defined as:

$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt$$

### Scaling Property 1: Time Shift

When we shift a continuous-time signal in time by an amount $a$, the energy remains unchanged. This can be expressed mathematically as:

$$\int_{-\infty}^{\infty} |x(t-a)|^2 dt = \int_{-\infty}^{\infty} |x(t)|^2 dt = E$$

### Scaling Property 2: Time Scaling

When we scale a continuous-time signal in time by an amount $a$, the energy is scaled by $\frac{1}{|a|^2}$:

$$\int_{-\infty}^{\infty} \left|x\left(\frac{t}{a}\right)\right|^2 dt = |a|^2 \int_{-\infty}^{\infty} |x(t)|^2 dt = |a|^2 E$$

### Scaling Property 3: Frequency Scaling

When we scale a continuous-time signal in frequency by an amount $b$, the energy remains unchanged:

$$\int_{-\infty}^{\infty} \left|x(t e^{i\omega b})\right|^2 dt = \int_{-\infty}^{\infty} |x(t)|^2 dt = E$$

**Key Formulas/Theorems**
-------------------------

### Energy of a Scaled Signal

The energy of a scaled signal is given by:

$$E_x(a) = |a|^{2 \alpha} E_x$$

where $a$ is the scaling factor and $\alpha$ is the order of the signal.

**Problem Solving Patterns**
-----------------------------

1. **Identify the scaling property**: Determine whether the problem involves a time shift, time scaling, or frequency scaling.
2. **Apply the correct formula**: Use the appropriate formula for the identified scaling property to calculate the energy of the scaled signal.
3. **Simplify and solve**: Simplify the expression and solve for the required value.

**Examples with Solutions**
---------------------------

### Example 1

Suppose we have a continuous-time signal $x(t)$ with energy $E$. If we scale this signal in time by an amount $a$, what is the new energy?

Solution:

Using Scaling Property 2, we have:

$$\int_{-\infty}^{\infty} \left|x\left(\frac{t}{a}\right)\right|^2 dt = |a|^{2} E$$

### Example 2

Suppose we have a continuous-time signal $x(t)$ with energy $E$. If we scale this signal in frequency by an amount $b$, what is the new energy?

Solution:

Using Scaling Property 3, we have:

$$\int_{-\infty}^{\infty} \left|x(t e^{i\omega b})\right|^2 dt = \int_{-\infty}^{\infty} |x(t)|^2 dt = E$$

**Common Pitfalls**
--------------------

* Failing to identify the correct scaling property.
* Incorrect application of formulas or incorrect simplification.

**Quick Summary**
------------------

| Concept | Formula/Property |
| --- | --- |
| Time Shift | $\int_{-\infty}^{\infty} |x(t-a)|^2 dt = E$ |
| Time Scaling | $\int_{-\infty}^{\infty} \left|x\left(\frac{t}{a}\right)\right|^2 dt = |a|^2 E$ |
| Frequency Scaling | $\int_{-\infty}^{\infty} \left|x(t e^{i\omega b})\right|^2 dt = E$ |

Note: The above summary is a concise representation of the key concepts and formulas covered in this note.