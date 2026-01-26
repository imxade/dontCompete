**Fourier Transform Theory Note**
=====================================

**Introduction**
---------------

The Fourier Transform (FT) is a mathematical tool used to decompose a function or signal into its constituent frequencies. It's a crucial concept in Signal Processing, allowing us to analyze and manipulate signals in the frequency domain.

**Core Concepts**
-----------------

### What is the Fourier Transform?

Given a continuous-time signal `x(t)`, the FT is defined as:

$$X(j\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}dt$$

where `ω` is the angular frequency.

### Linearity and Time-Shifting Properties

The FT has two important properties:

1. **Linearity**: The FT of a linear combination of signals is the same as the sum of their individual FTs.
2. **Time-Shifting**: A time-shift in the signal corresponds to a phase shift in its FT.

These properties are crucial for solving problems related to filtering, convolution, and modulation.

**Key Formulas/Theorems**
-------------------------

### Fourier Transform Properties

1. **Inverse Fourier Transform**: Given `X(jω)`, we can recover the original signal using:

$$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega)e^{j\omega t}d\omega$$
2. **Fourier Transform of Derivatives**: If `x(t)` has a derivative `x'(t)`, then:

$$X'(j\omega) = j\omega X(j\omega)$$

### Parseval's Theorem

Parseval's theorem states that the energy of a signal in the time domain is equal to its power spectral density (PSD) in the frequency domain.

$$\int_{-\infty}^{\infty} |x(t)|^2dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(j\omega)|^2d\omega$$

**Problem Solving Patterns**
---------------------------

### Finding the Fourier Transform of a Signal

To find `X(jω)`, apply the FT definition to the signal.

### Using Parseval's Theorem

When given a signal and its PSD, use Parseval's theorem to find the energy in the time domain.

### Time-Shifting and Convolution

Use the linearity and time-shifting properties to solve problems related to filtering and convolution.

**Examples with Solutions**
---------------------------

### Example 1: Finding the Fourier Transform of `x(t) = e^(-at)` for a > 0

Apply the FT definition:

$$X(j\omega) = \int_{-\infty}^{\infty} e^{-at}e^{-j\omega t}dt = \frac{1}{a + j\omega}$$

### Example 2: Using Parseval's Theorem

Given `x(t)` with energy `E`, find the PSD using:

$$|X(j\omega)|^2 = \frac{2\pi E}{d\omega}$$

**Common Pitfalls**
------------------

1. **Misapplying Linearity**: Be careful when combining signals.
2. **Forgetting to Use `j`**: Remember that `j` is the imaginary unit.

**Quick Summary**
-----------------

* FT definition: `X(jω) = ∫_{-∞}^{\infty} x(t)e^{-jωt}dt`
* Linearity and time-shifting properties
* Parseval's theorem
* Key formulas:
	+ Inverse FT
	+ FT of derivatives
	+ Parseval's theorem

Note: The following Mermaid diagram illustrates the process of finding the Fourier Transform.
```mermaid
graph LR
A[Signal x(t)] --> B[Apply FT definition]
B --> C[FT X(jω)]
C --> D[Linearity and time-shifting properties]
D --> E[Paseval's theorem]
E --> F[Inverse FT, if needed]
```
This theory note provides a comprehensive overview of the Fourier Transform, covering core concepts, key formulas, problem-solving patterns, examples with solutions, common pitfalls, and a quick summary. It should serve as a reliable resource for students preparing for the GATE CS exam.