**Classification of Signals**
==========================

**Introduction**
---------------

Signal classification is a fundamental concept in signal processing and systems engineering. It helps us understand the properties and behavior of signals, which is crucial for designing and analyzing systems that process these signals. In this theory note, we will cover the key concepts related to signal classification.

**Core Concepts**
-----------------

A system can be classified based on its input-output relationship and time domain behavior. The main types of systems are:

* **Causal Systems**: A system is causal if its output at any instant depends only on the present or past values of the input.
* **Non-Causal Systems**: A system is non-causal if its output at any instant also depends on future values of the input.

**Key Formulas/Theorems**
-------------------------

LaTeX is not supported in this response, but we can describe the formulas and use Markdown for equations. For example:

Equation 1: Causality condition
--------------------------------

A system is causal if:

$$y(t) = \int_{-\infty}^{t} h(\tau)x(t - \tau)d\tau$$

where $h(\tau)$ is the impulse response of the system.

**Problem Solving Patterns**
---------------------------

1.  **Check for Causality**: If the output depends only on present or past input values, the system is causal.
2.  **Analyze Time Domain Behavior**: Check if the output at any instant also depends on future input values. If so, the system is non-causal.

**Examples with Solutions**
---------------------------

### Example 1:

Consider a system with input $x(t) = \cos(2t)$ and output $y(t) = x(t - 1)$. Determine if the system is causal or non-causal.

Solution: The output depends only on past values of the input, so the system is causal.

### Example 2:

Consider a system with input $x(t) = \cos(2t)$ and output $y(t) = x(t + 1)$. Determine if the system is causal or non-causal.

Solution: The output depends on future values of the input, so the system is non-causal.

**Common Pitfalls**
------------------

*   **Not checking for causality**: Always verify if the output depends only on present or past input values.
*   **Not analyzing time domain behavior**: Failure to check if the output also depends on future input values can lead to incorrect conclusions.

**Quick Summary**
-----------------

*   Causal systems: output depends only on present or past input values
*   Non-causal systems: output may depend on future input values
*   Check for causality and analyze time domain behavior when classifying signals

Let me know if this helps. I'll be happy to make any further modifications as needed!