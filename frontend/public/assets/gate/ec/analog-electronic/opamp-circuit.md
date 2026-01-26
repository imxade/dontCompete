**Op-Amp Circuit Theory Note**
==========================

### Introduction
---------------

An operational amplifier (op-amp) circuit is a fundamental component in analog electronics, used for amplifying or modifying signals. The op-amp's high gain and differential input capabilities make it an essential building block for various circuits.

### Core Concepts
-----------------

*   **Ideal Op-Amp Assumptions**
    *   Infinite gain
    *   Zero input offset voltage
    *   Infinite input resistance
    *   Zero output resistance
*   **Non-Idealities and Limitations**
    *   Gain-bandwidth product (GB)
    *   Input bias current
    *   Offset voltage
    *   Non-linearity

### Key Formulas/Theorems
-------------------------

*   **Inverting Amplifier** $V_o = -\frac{R_f}{R_i} V_{in}$[^1]
*   **Non-Inverting Amplifier** $V_o = \left( 1 + \frac{R_f}{R_i} \right) V_{in}$[^2]

### Problem Solving Patterns
---------------------------

1.  **Capacitive Coupling and Charging**
    *   Use the formula $Q = C \Delta V$ for capacitors in series or parallel.
    *   Consider the time constant $\tau = RC$ when analyzing charging effects.
2.  **Ideal Op-Amp Assumptions**:
    *   Assume infinite gain to simplify problems with low-frequency signals.
    *   Use the differential amplifier equation $V_o = \frac{R_f}{R_i} (V_{in+} - V_{in-})$ for voltage-follower and summing-amplifier configurations.
3.  **Pulse Response**:
    *   Apply the initial condition $\frac{dQ}{dt} = I(t)$ to the capacitor equation $Q = \int I(t) dt$
    *   Analyze output signals considering capacitive charging times

### Examples with Solutions
---------------------------

1.  **Capacitor Voltage Difference**
    Q41: Find the difference between maximum and minimum values of the capacitor voltage in the given circuit.

    ```
          +---------------+
          |               |
          |  +-------+   |
          |  |       |   |
          |  |   R    |   |
          |  |       |   |
          |  +-------+   |
          |               |
          v               v
    Vc =   C1 * V+ - C2 * V-        (i)
    ```
    From the equation above, we can write:

    $$\frac{dQ_1}{dt} = I_{in} = \frac{V_{out}}{R}$$

    Integrating both sides and considering the capacitor discharge:

    $$C_1 * V_c(t) = -\int I_{in} dt$$

    Since we have a step input with amplitude 12 V, the initial voltage is zero. The final voltage at t=20 ms will be:
    ```
          Vc_final = 12V
    ```

2.  **3 dB Frequency**
    Q26: Determine the correct option regarding the 3-dB frequency in an ideal OP-AMP circuit.

    Consider a low-pass filter with the transfer function:

    $$H(s) = \frac{1}{\sqrt{(1 + s\tau)^2}}$$

    The magnitude of the gain at the 3 dB point is given by:

    $|H(j \omega)| = \frac{1}{\sqrt{2}}$

    Substituting $\omega = \omega_0$ and solving for $\omega_0$, we get:

    $$\omega_0 = \frac{1}{\tau}$$

3.  **Pulse Response**
    Q4: Find the output voltage in an ideal OP-AMP circuit with a given input pulse.

    ```
          +---------------+
          |               |
          |  +-------+   |
          |  |       |   |
          |  |  C1  |   |
          |  |       |   |
          |  +-------+   |
          |               |
          v               v
    Vout =  -C2 * V_in        (ii)
    ```

    From the equation above, we can write:

    $$V_{out}(t) = \frac{1}{C_2} \int I(t) dt$$

    Integrating both sides and considering the initial capacitor discharge:

    $$V_{out}(0) = -\frac{Q(0)}{C_2}$$

    Since we have a step input with amplitude 12 V, the initial charge is zero. The final voltage at t=20 ms will be:
    ```
          V_out_final = -12V
    ```

### Common Pitfalls
-------------------

*   Failing to consider ideal op-amp assumptions and their limitations.
*   Not accounting for capacitive charging times in pulse response problems.

### Quick Summary
----------------

*   Ideal op-amp assumptions: infinite gain, zero input offset voltage, infinite input resistance, and zero output resistance.
*   Key formulas:
    *   Inverting amplifier: $V_o = -\frac{R_f}{R_i} V_{in}$[^1]
    *   Non-inverting amplifier: $V_o = \left( 1 + \frac{R_f}{R_i} \right) V_{in}$[^2]
*   Problem-solving patterns:
    *   Capacitive coupling and charging
    *   Ideal op-amp assumptions
    *   Pulse response

[^1]: Inverting amplifier transfer function.
[^2]: Non-inverting amplifier transfer function.