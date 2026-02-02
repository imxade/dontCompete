**Periodic and Aperiodic Signals**
=====================================

### Introduction
A signal is said to be periodic if it repeats itself after a certain time interval, known as the period. On the other hand, an aperiodic signal does not have any repeating pattern.

### Core Concepts

#### Periodicity
A signal x(t) is said to be periodic with period T if it satisfies the condition:

x(t + T) = x(t)

This means that the signal repeats itself after every time interval of length T.

#### Aperiodicity
If a signal does not satisfy the condition of periodicity, it is said to be aperiodic. In other words, an aperiodic signal does not repeat itself after any fixed time interval.

### Key Formulas/Theorems

* **Periodicity Condition**:

$$x(t + T) = x(t) \quad \forall t$$

* **Aperiodicity Condition**:
	No specific condition can be formulated for aperiodicity, as it is the absence of periodicity.

### Problem Solving Patterns

1.  To determine if a signal is periodic or aperiodic, look for repeating patterns in its waveform.
2.  If the signal repeats itself after a certain time interval, then it is periodic.
3.  On the other hand, if there is no repeating pattern, then the signal is aperiodic.

### Examples with Solutions

#### Example 1: Periodic Signal
Consider the following signal:

$$x(t) = \sin(2\pi t/T)$$

This signal repeats itself after every time interval of length T. Therefore, it is periodic with period T.

#### Solution:
We can verify this by substituting (t + T) into the expression for x(t):

$$x(t + T) = \sin(2\pi (t + T)/T) = \sin(2\pi t/T + 2\pi) = \sin(2\pi t/T) = x(t)$$

#### Example 2: Aperiodic Signal
Consider the following signal:

$$x(t) = e^{-|t|}$$

This signal does not repeat itself after any fixed time interval. Therefore, it is aperiodic.

### Common Pitfalls
Students often miss the fact that periodicity and aperiodicity are determined by the behavior of the signal over all time, not just for specific intervals or values.

### Quick Summary
*   Periodic signal: repeats itself after a certain time interval (T)
*   Aperiodic signal: does not repeat itself after any fixed time interval

### Mermaid Diagram
```mermaid
graph LR
    A[Periodic Signal] -->|repeats itself after T|> B[Time]
    C[Aperiodic Signal] -->|does not repeat|> D[Time]
```

Note that the diagram above is a simple representation of periodic and aperiodic signals. In reality, these concepts are more nuanced and require careful analysis of the signal's behavior over time.

### References

*   [1] Signals & Systems by Oppenheim & Willsky (Chapter 3)
*   [2] Discrete-Time Signal Processing by Oppenheim & Schafer (Chapter 2)

This theory note covers all theoretical concepts, formulas, and insights required to solve the source questions.