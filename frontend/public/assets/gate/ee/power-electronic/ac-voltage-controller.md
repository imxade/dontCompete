**Ac Voltage Controller**
=========================

**Introduction**
---------------

An AC voltage controller is a power electronic device used to control the output voltage of an AC supply in response to changes in the load or system requirements. It plays a crucial role in many applications, including lighting systems, motor drives, and renewable energy systems.

**Core Concepts**
-----------------

### Working Principle

An AC voltage controller uses a triac (triode for alternating current) as its active component. The triac is a three-terminal device that can conduct current in both directions. It has two terminals, T1 and T2, which are used to control the flow of current.

In an ac voltage controller, the triac is triggered at a specific angle to control the output voltage. When the triac is triggered, it starts conducting current, and the output voltage begins to rise. The rate at which the voltage rises depends on the load connected to the controller.

### Minimum Triggering Angle

The minimum triggering angle is the smallest angle at which the triac can be triggered to obtain a controlled output voltage. It depends on the load impedance and the AC supply frequency.

### Phase Angle

The phase angle, denoted by φ, is the angle between the voltage and current waveforms in an ac circuit. In an RL load, the phase angle is given by:

$$\tan{\phi} = \frac{X_L}{R}$$

where $X_L$ is the inductive reactance and R is the resistance.

### Conduction Angle

The conduction angle is the angle between the triggering instant and the next zero crossing of the voltage waveform. It determines the duration for which the triac conducts current.

**Key Formulas/Theorems**
-------------------------

*   Minimum Triggering Angle: $$\alpha > \phi$$
*   Phase Angle: $$\tan{\phi} = \frac{X_L}{R}$$
*   Conduction Angle: $$\gamma = 2\alpha - \pi$$

**Problem Solving Patterns**
---------------------------

1.  Identify the load impedance and AC supply frequency.
2.  Determine the minimum triggering angle using the given formulas.
3.  Calculate the phase angle using the load impedance and resistance.
4.  Use the conduction angle to determine the duration of current flow.

**Examples with Solutions**
-------------------------

### Example 1

A single-phase triac-based AC voltage controller feeds a series RL load. The input AC supply is 230 V, 50 Hz. The values of R and L are 10 Ω and 18.37 mH, respectively. Find the minimum triggering angle to obtain controllable output voltage.

**Solution**

*   Given: $R = 10 \Omega$, $L = 18.37$ mH, $f = 50 Hz$
*   Calculate phase angle:
    $$\tan{\phi} = \frac{X_L}{R}$$
    $$\tan{\phi} = \frac{2\pi f L}{R}$$
    $$\tan{\phi} = \frac{2\pi \times 50 \times 18.37 \times 10^{-3}}{10}$$
    $$\tan{\phi} = 0.5797$$
    $$\phi = \arctan(0.5797)$$
    $$\phi \approx 30^{\circ}$$
*   Minimum triggering angle:
    $$\alpha > \phi$$
    Therefore, the minimum triggering angle is $30^{\circ}$.

### Example 2

A triac-based AC voltage controller feeds a series RL load. The input AC supply is 230 V, 50 Hz. The values of R and L are 20 Ω and 27 mH, respectively. Find the conduction angle for a minimum triggering angle of $45^{\circ}$.

**Solution**

*   Given: $R = 20 \Omega$, $L = 27$ mH, $f = 50 Hz$, $\alpha = 45^{\circ}$
*   Calculate phase angle:
    $$\tan{\phi} = \frac{X_L}{R}$$
    $$\tan{\phi} = \frac{2\pi f L}{R}$$
    $$\tan{\phi} = \frac{2\pi \times 50 \times 27 \times 10^{-3}}{20}$$
    $$\tan{\phi} = 0.8494$$
    $$\phi = \arctan(0.8494)$$
    $$\phi \approx 42^{\circ}$$
*   Conduction angle:
    $$\gamma = 2\alpha - \pi$$
    $$\gamma = 2 \times 45 - \pi$$
    $$\gamma \approx 89.24^{\circ}$$

**Common Pitfalls**
-------------------

1.  Incorrectly calculating the phase angle or minimum triggering angle.
2.  Forgetting to consider the load impedance and AC supply frequency.

**Quick Summary**
-----------------

*   Ac voltage controller: a power electronic device used to control output voltage in response to changes in load or system requirements.
*   Triac: active component used in ac voltage controllers, conducts current in both directions.
*   Minimum triggering angle: smallest angle at which triac can be triggered to obtain controlled output voltage.
*   Phase angle: angle between voltage and current waveforms in an ac circuit.
*   Conduction angle: determines duration of current flow.

**References**
---------------

1.  "Power Electronics" by B.L. Theraja and A.K. Theraja
2.  "AC Voltage Controllers" by R.M. Nelms