**Cascade Control Strategy**
==========================

**Introduction**
---------------

In process control, cascade control is a strategy used to improve the stability and accuracy of control systems. It involves using a secondary controller to regulate a primary variable, which in turn controls the main process.

**Core Concepts**
-----------------

The key concept behind cascade control is that the secondary controller adjusts its setpoint based on the actual value of the primary variable. This allows for more precise control over the process.

Let's consider the example from the source question:

![Cascade Control Strategy](https://en.wikipedia.org/wiki/Cascade_control#/media/File:Cascade_control.png)

**Key Formulas/Theorems**
-------------------------

The transfer function between the output (𝑦) and the secondary disturbance $d_2$ is defined as:

$$G_{yd_2} = \frac{Y(s)}{D_2(s)}$$

We are given that this transfer function is equal to:

$$\frac{(1)(0.1s+1)}{11s^2 + 21s + 1}$$

However, we need to simplify the expression.

**Problem Solving Patterns**
---------------------------

When solving cascade control problems, follow these steps:

1. Identify the primary and secondary controllers.
2. Determine the transfer functions between the output and each disturbance.
3. Combine the transfer functions using the formula above.

**Examples with Solutions**
-------------------------

### Example 1

Given:

* Transfer function between output and primary disturbance: $\frac{Y(s)}{D_1(s)} = \frac{10s+1}{11s^2 + 21s + 1}$
* Transfer function between output and secondary disturbance: $\frac{Y(s)}{D_2(s)} = \frac{(1)(0.1s+1)}{11s^2 + 21s + 1}$

Find the combined transfer function.

```latex
\frac{Y(s)}{D_2(s)} = \frac{(10s+1)(0.1s+1)}{(11s^2 + 21s + 1)^2}
```

### Example 2

Given:

* Transfer function between output and primary disturbance: $\frac{Y(s)}{D_1(s)} = \frac{s+1}{(10s^2 + 20s + 1)}
* Transfer function between output and secondary disturbance: $\frac{Y(s)}{D_2(s)} = \frac{(0.1s+1)}{11s^2 + 21s + 1}$

Find the combined transfer function.

```latex
\frac{Y(s)}{D_2(s)} = \frac{(s+1)(0.1s+1)}{(10s^2 + 20s + 1)(11s^2 + 21s + 1)}
```

**Common Pitfalls**
-------------------

* Students often forget to combine the transfer functions correctly.
* They may also confuse the primary and secondary controllers.

**Quick Summary**
------------------

* Cascade control involves using a secondary controller to regulate a primary variable.
* The transfer function between output and each disturbance must be combined using the formula above.
* Simplify the expression to obtain the final answer.

Note: This is a basic example of cascade control. In practice, there may be more complex systems with multiple variables and disturbances.