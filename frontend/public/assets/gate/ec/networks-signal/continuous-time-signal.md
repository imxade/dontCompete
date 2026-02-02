**Continuous Time Signal**
==========================

### Introduction
A continuous time signal (CTS) is a mathematical function that describes a physical quantity or property that varies with time, such as voltage, current, temperature, or pressure. CTS are essential in various fields like electrical engineering, control systems, and signal processing.

### Core Concepts

#### Continuous Time Signal Representation
A CTS can be represented mathematically using the following notations:

* $x(t)$: the continuous-time signal itself
* $t$: time variable (usually a real number)
* $\mathcal{R}$: set of all real numbers representing time

#### Fourier Transform
The Fourier transform is a fundamental tool for analyzing CTS. It decomposes a CTS into its frequency components.

$$\mathcal{F}\{x(t)\} = X(j\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}dt$$

* $X(j\omega)$: Fourier transform of the signal $x(t)$
* $\omega$: angular frequency (radians per second)
* $j$: imaginary unit ($j^2 = -1$)

#### Time-Domain and Frequency-Domain Representations
A CTS can be represented in both time domain and frequency domain:

Time Domain: $x(t) = \ldots, 3u_1(t-2), 2u_0(t-1), u_{-1}(t)$

Frequency Domain: $\mathcal{F}\{x(t)\} = X(j\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}dt$

### Key Formulas/Theorems
LaTeX used for math equations:

$$\mathcal{F}\{ax(t) + bu(t)\} = aX(\omega) + bU(\omega) \quad (\text{Linearity})$$

$$\mathcal{F}\{x(t-\tau)\} = e^{-j\omega\tau}X(\omega) \quad (\text{Time-Shifting Property})$$

### Problem Solving Patterns
When solving CTS-related problems, follow these steps:

1. **Identify the problem**: Determine what information is given and what is being asked.
2. **Apply Fourier Transform**: Use the Fourier transform to analyze the signal in the frequency domain.
3. **Analyze Frequency Components**: Interpret the frequency components of the signal.
4. **Convert Back to Time Domain (if necessary)**: If required, convert the signal back from frequency domain to time domain.

### Examples with Solutions
**Example 1:** Given $x(t) = \begin{cases} t^2 & 0 < t < 3 \\ 0 & \text{otherwise} \end{cases}$, find its Fourier transform using the definition of the Fourier Transform.

```mermaid
graph LR
A[Given x(t)] --> B[Fourier Transform]
B --> C[Integrate x(t)e^(-jωt)dt from -∞ to ∞]
C --> D[Result: X(jω)]
```

**Solution:**

$$\mathcal{F}\{x(t)\} = \int_0^3 t^2 e^{-j\omega t} dt = \frac{6}{\omega^3}(1-e^{-j\omega 3})$$

### Common Pitfalls
When solving CTS problems, be aware of the following:

* Ensure correct application of Fourier Transform properties.
* Be cautious with domain shifts and scaling.
* Verify units and dimensions in your solutions.

### Quick Summary
Here are key points to revise:

• Continuous time signals (CTS) can be represented mathematically using notations like $x(t)$, $t$, and $\mathcal{R}$.
• The Fourier transform is a fundamental tool for analyzing CTS, decomposing them into frequency components.
• Linearity, Time-Shifting Property, and other properties are essential for solving CTS-related problems.

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve the source questions. Practice with more examples to master these concepts!