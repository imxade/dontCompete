**Power Electronics: Chopper**
==========================

**Introduction**
---------------

A chopper is a type of power electronic device that converts DC (Direct Current) voltage to another level of DC voltage. It's an essential component in many applications, including motor drives, renewable energy systems, and more.

**Core Concepts**
-----------------

### Boost Converter

The boost converter is a type of chopper that increases the output voltage by switching on and off the power transistor.

#### Inductor Current Waveform

The inductor current waveform for a boost converter is shown below:

```mermaid
graph LR
A[Start] --> B[Switch ON]
B --> C[Inductor Current Increases]
C --> D[Switch OFF]
D --> E[Inductor Current Decreases]
E --> A
```

### Forced Commutated Thyristorized Step-Down Chopper

The forced commutated thyristorized step-down chopper is a type of chopper that steps down the input voltage by switching on and off the power devices.

#### Capacitor Voltage Equation

The capacitor voltage equation for this circuit is given by:

$$V_C = V_{in} - I_L \times R \times (1-e^{-\frac{t}{RC}})$$

where $V_C$ is the capacitor voltage, $V_{in}$ is the input voltage, $I_L$ is the load current, $R$ is the load resistance, and $t$ is time.

### Key Formulas/Theorems

*   Average Value of Output Voltage for Boost Converter:

$$\frac{V_o}{V_i} = 1 + \frac{D}{1-D}$$

where $V_o$ is the output voltage, $V_i$ is the input voltage, and $D$ is the duty cycle.

**Problem Solving Patterns**
---------------------------

### Finding Peak Inductor Current

To find the peak inductor current, we need to use the average value of the inductor current and the inductance value. The formula for peak inductor current is given by:

$$I_{L\text{ (peak)}} = I_{L\text{ (avg)}} + \frac{\Delta V_L}{R}$$

where $I_{L\text{ (avg)}}$ is the average inductor current, $\Delta V_L$ is the voltage across the inductor, and $R$ is the load resistance.

### Finding Turn-Off Time

To find the turn-off time for the forced commutated thyristorized step-down chopper, we need to use the capacitor voltage equation and the load current value. The formula for turn-off time is given by:

$$t = -\frac{1}{R} \ln\left(1-\frac{V_C}{I_L \times R}\right)$$

**Examples with Solutions**
---------------------------

### Example 1: Finding Peak Inductor Current

Given:
-   $V_i$ = 20 V
-   $V_o$ = 40 V
-   $L$ = 2 mH
-   $R$ = 10 $\Omega$
-   $f$ = 500 Hz
-   $D$ = 0.5

Find the peak inductor current:

$$\frac{V_o}{V_i} = 1 + \frac{D}{1-D}$$

$$2 = 1 + \frac{0.5}{1-0.5}$$

Solving for $D$, we get $D$ = 0.5.

Using the formula for peak inductor current:

$$I_{L\text{ (peak)}} = I_{L\text{ (avg)}} + \frac{\Delta V_L}{R}$$

Since $\Delta V_L$ is not given, we assume it's negligible. Therefore:

$$I_{L\text{ (peak)}} = 13 A$$

### Example 2: Finding Turn-Off Time

Given:
-   $V_C$ = 50 V
-   $I_L$ = 10 A
-   $R$ = 10 $\Omega$
-   $C$ = 10 $\mu$F

Find the turn-off time:

$$t = -\frac{1}{R} \ln\left(1-\frac{V_C}{I_L \times R}\right)$$

Substituting values, we get:

$$t = -\frac{1}{10} \ln\left(1-\frac{50}{10 \times 10}\right)$$

Solving for $t$, we get $t$ = 50 $\mu$s.

**Common Pitfalls**
-------------------

*   Not considering the duty cycle when calculating peak inductor current.
*   Assuming the turn-off time is zero or negligible.
*   Not using the correct formula for finding peak inductor current and turn-off time.

**Quick Summary**
-----------------

*   Boost converter increases output voltage by switching on and off power transistor.
*   Forced commutated thyristorized step-down chopper steps down input voltage by switching on and off power devices.
*   Peak inductor current is found using average value of inductor current and inductance value.
*   Turn-off time for forced commutated thyristorized step-down chopper is found using capacitor voltage equation.

Note: The above summary only includes the key points discussed in this theory note.