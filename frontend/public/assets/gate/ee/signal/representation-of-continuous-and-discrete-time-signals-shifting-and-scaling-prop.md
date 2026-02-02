**Representation of Continuous and Discrete Time Signals: Shifting and Scaling Properties**
====================================================================================================

**Introduction**
---------------

This topic deals with the manipulation of time-domain signals through shifting and scaling operations. Understanding these properties is crucial for signal processing, analysis, and synthesis.

**Core Concepts**
-----------------

### 1. Time-Shifting Property

When a continuous-time (CT) or discrete-time (DT) signal `x(t)` or `x[n]` is delayed by a time interval `t_0`, the resulting signal is given by:

*   CT: $y(t) = x(t - t_0)$
*   DT: $y[n] = x[n + n_0]$

This property allows us to shift the signal in time without altering its frequency content.

### 2. Time-Skipping Property

The time-skipping property states that a CT or DT signal can be compressed or expanded by modifying its sampling rate or period. This results in a new signal with different time and frequency characteristics.

*   CT: $y(t) = x(at)$, where `a` is the compression factor
*   DT: $y[n] = x[n/a]$, where `a` is the expansion factor

### 3. Time-Scaling Property

The time-scaling property is a combination of time-shifting and time-skipping. It involves modifying both the sampling period and the delay of a signal.

**Key Formulas/Theorems**
------------------------

*   Time-Shifting Property: $y(t) = x(t - t_0)$ or $y[n] = x[n + n_0]$
*   Time-Skipping Property (CT): $y(t) = x(at)$
*   Time-Skipping Property (DT): $y[n] = x[n/a]$

**Problem Solving Patterns**
---------------------------

1.  **Shifting and Scaling**: Apply the time-shifting property by adjusting the signal's sampling period or delay to match the desired output.
2.  **Time-Domain Analysis**: Analyze the original and modified signals in the time domain to understand their differences.

**Examples with Solutions**
-------------------------

### Example 1: Shifting a Signal

Given:

*   $x(t) = sin(2\pi ft)$
*   Shift by `t_0 = 1` second

Find: `y(t)`

Solution:
```
y(t) = x(t - t_0)
= sin(2\pi f(t - 1))
```

### Example 2: Scaling a Signal

Given:

*   $x[n] = cos(\frac{2\pi n}{N})$
*   Scale by `a = 2` times

Find: `y[n]`

Solution:
```
y[n] = x[n/a]
= cos(\frac{2\pi n}{2N})
= cos(\frac{\pi n}{N})
```

**Common Pitfalls**
--------------------

1.  **Misapplying Time-Shifting**: Incorrectly apply the time-shifting property by modifying both sampling period and delay.
2.  **Overlooking Scaling Factors**: Fail to account for scaling factors when compressing or expanding signals.

**Quick Summary**
-----------------

*   Time-Shifting Property: Shift a signal in time without altering its frequency content
*   Time-Skipping Property (CT): Compress or expand a CT signal using `a` as the compression factor
*   Time-Skipping Property (DT): Expand or compress a DT signal using `a` as the expansion factor
*   Time-Scale Property: Combine time-shifting and time-skipping properties

Note that this is just an example of how you could structure your note, but it's up to you to customize it with your own knowledge and writing style. Make sure to cover all necessary topics and concepts for the GATE CS exam.