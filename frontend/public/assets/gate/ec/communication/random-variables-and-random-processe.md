**Random Variables and Random Processes**
=====================================

**Introduction**
---------------

Random variables and random processes are fundamental concepts in communication systems. A random variable is a function that assigns a numerical value to each outcome of an experiment, while a random process is a collection of random variables indexed by time or another parameter.

**Core Concepts**
-----------------

### Random Variables

A random variable $X$ is a function from a sample space $\Omega$ to the real numbers $\mathbb{R}$:
$$
X: \Omega \to \mathbb{R}
$$

*   **Discrete Random Variable**: A discrete random variable takes on a finite or countably infinite number of values.
*   **Continuous Random Variable**: A continuous random variable can take on any value within a given interval.

### Random Processes

A random process $X(t)$ is a collection of random variables indexed by time $t$:
$$
X: \mathbb{R} \to \Omega \to \mathbb{R}
$$

*   **Stationary Process**: A stationary process has constant statistical properties over time.
*   **Memoryless Process**: A memoryless process depends only on the current time and not on past values.

**Key Formulas/Theorems**
-------------------------

### Power Spectral Density (PSD)

The PSD of a random process $X(t)$ is defined as:
$$
S_X(f) = \lim_{T \to \infty} \frac{1}{2T} |F_X(f)|^2
$$

where $F_X(f)$ is the Fourier transform of the autocorrelation function of $X(t)$.

### Autocorrelation Function

The autocorrelation function of a random process $X(t)$ is defined as:
$$
R_X(\tau) = E[X(t) X(t + \tau)]
$$

### Cross-Correlation Function

The cross-correlation function between two random processes $X_1(t)$ and $X_2(t)$ is defined as:
$$
R_{X_1, X_2}(\tau) = E[X_1(t) X_2(t + \tau)]
$$

**Problem Solving Patterns**
---------------------------

### Pattern 1: Finding PSD from Autocorrelation Function

*   Given the autocorrelation function $R_X(\tau)$, find the PSD using the formula:
    $$S_X(f) = F_{R_X}(f)$$
*   Take the Fourier transform of $R_X(\tau)$ to get $F_{R_X}(f)$.

### Pattern 2: Finding Autocorrelation Function from PSD

*   Given the PSD $S_X(f)$, find the autocorrelation function using the formula:
    $$R_X(\tau) = \int_{-\infty}^{\infty} S_X(f) e^{j2\pi f \tau} df$$

**Examples with Solutions**
---------------------------

### Example 1: Finding PSD of a White Gaussian Noise

*   Given that $X(t)$ is a white Gaussian noise with power spectral density:
    $$S_X(f) = N_0/2$$
*   Find the autocorrelation function $R_X(\tau)$.
    $$R_X(\tau) = \int_{-\infty}^{\infty} S_X(f) e^{j2\pi f \tau} df = N_0$$

### Example 2: Finding Autocorrelation Function of an LTI System Output

*   Given that $X(t)$ is input to an LTI system with impulse response $h(t)$, find the autocorrelation function $R_Y(\tau)$ of the output $Y(t)$.
    $$R_Y(\tau) = \int_{-\infty}^{\infty} h(t + \tau/2) h(t - \tau/2) dt$$

**Common Pitfalls**
------------------

*   Confusing PSD with autocorrelation function
*   Not using the correct formulas for finding PSD and autocorrelation function
*   Not considering the properties of stationary and memoryless processes

**Quick Summary**
-----------------

*   Random variables and random processes are fundamental concepts in communication systems.
*   Key formulas and theorems include power spectral density, autocorrelation function, and cross-correlation function.
*   Problem-solving patterns involve finding PSD from autocorrelation function and vice versa.

Note: The source questions provided will be used to guide the development of this theory note. Ensure that every concept tested in the source questions is explained in the theory.