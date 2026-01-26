**LTI System Analysis**
=======================

**Introduction**
---------------

In this note, we'll delve into the analysis of Linear Time-Invariant (LTI) systems. An LTI system is a mathematical model that describes how signals are transformed as they pass through a system. Understanding LTI systems is crucial in signal processing and control theory.

**Core Concepts**
-----------------

### Linearity

An LTI system is said to be linear if it satisfies the following properties:

1. **Homogeneity**: If an input signal $x(t)$ produces an output signal $y(t)$, then a scaled version of the input signal, $\alpha x(t)$, will produce a scaled version of the output signal, $\alpha y(t)$.
2. **Additivity**: If two input signals $x_1(t)$ and $x_2(t)$ produce output signals $y_1(t)$ and $y_2(t)$ respectively, then the sum of these input signals, $x_1(t) + x_2(t)$, will produce a sum of the output signals, $y_1(t) + y_2(t)$.

### Time-Invariance

An LTI system is said to be time-invariant if its response to an input signal depends only on the signal itself and not on when it was applied. Mathematically, this means that for a given input signal $x(t)$ and output signal $y(t)$, the following equation holds:

$$h(\tau) = h(-\tau) \quad \text{and} \quad x_1(t) * h(t) = y_1(t) \implies x_2(t) * h(t) = y_2(t)$$

where $*$ denotes convolution.

### Convolution and Impulse Response

Convolution is a mathematical operation that combines two functions by sliding one function over the other. The impulse response of an LTI system is the output when the input is a unit impulse $\delta(t)$.

For an LTI system with impulse response $h(t)$, the output signal $y(t)$ can be computed using convolution:

$$y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau)h(t - \tau)d\tau$$

### Frequency Response and Transfer Function

The frequency response of an LTI system is its output in the frequency domain, given by:

$$H(j\omega) = F\{h(t)\}$$

where $F$ denotes the Fourier transform. The transfer function of an LTI system is defined as:

$$H(s) = \mathcal{L}\{h(t)\}$$

where $\mathcal{L}$ denotes the Laplace transform.

**Key Formulas/Theorems**
---------------------------

### Convolution Theorem

The convolution theorem states that for any two functions $x(t)$ and $h(t)$, their convolution is equal to the product of their Fourier transforms:

$$\mathcal{F}\{x(t) * h(t)\} = X(j\omega)H(j\omega)$$

### Fourier Transform Properties

| Property | Formula |
| --- | --- |
| Linearity | $\mathcal{F}\{\alpha x(t) + \beta y(t)\} = \alpha X(j\omega) + \beta Y(j\omega)$ |
| Time-Shifting | $\mathcal{F}\{x(t - a)\} = e^{-j\omega a}X(j\omega)$ |

### Laplace Transform Properties

| Property | Formula |
| --- | --- |
| Linearity | $\mathcal{L}\{\alpha x(t) + \beta y(t)\} = \alpha X(s) + \beta Y(s)$ |
| Time-Shifting | $\mathcal{L}\{e^{at}x(t)\} = X(s - a)$ |

**Problem Solving Patterns**
---------------------------

1.  **Identify the impulse response**: Understand that the impulse response is the output of an LTI system when the input is a unit impulse.
2.  **Apply convolution**: Use convolution to find the output signal $y(t)$ given an input signal $x(t)$ and an impulse response $h(t)$.
3.  **Analyze frequency response**: Compute the frequency response $H(j\omega)$ of an LTI system using its transfer function or impulse response.

**Examples with Solutions**
---------------------------

### Example 1: Convolution

Find the output signal $y(t)$ when the input signal is:

$$x(t) = \cos(10t) + 2\sin(15t)$$

and the impulse response is:

$$h(t) = \frac{1}{5}\sin(40t)$$

**Step 1**: Apply convolution to find $y(t)$.

$$y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau)h(t - \tau)d\tau$$

**Step 2**: Use Fourier transform properties to simplify the convolution integral.

$$Y(j\omega) = X(j\omega)H(j\omega)$$

### Solution

Using a calculator or software tool, we find that:

$$y(t) = \cos(10t)\frac{1}{5}\sin(40t) + 2\sin(15t)\frac{1}{5}\sin(40t)$$

Simplifying further yields:

$$y(t) = \left(\frac{1}{5} - \frac{4}{5}\right)\cos(10t)\sin(40t) + \left(\frac{2}{5} + \frac{8}{5}\right)\sin(15t)\sin(40t)$$

This example illustrates the process of applying convolution to find an output signal.

**Common Pitfalls**
-----------------

1.  **Misinterpreting time-invariance**: Remember that time-invariance means the response depends only on the input signal itself and not on when it was applied.
2.  **Incorrect application of convolution theorem**: Double-check your work when using the convolution theorem to ensure you're applying the correct properties.

**Quick Summary**
-----------------

*   LTI systems are linear, meaning they preserve scaling and addition properties.
*   Time-invariance ensures that the response depends only on the input signal itself.
*   Convolution combines two functions by sliding one over the other.
*   Frequency response is the output in the frequency domain, given by $H(j\omega)$.

By following this study note, you should be well-prepared to tackle LTI system analysis problems and similar questions.