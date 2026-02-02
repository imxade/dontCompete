**Transistors**
================

### Introduction
---------------

Transistors are semiconductor devices that play a crucial role in modern electronic circuits. They are essentially current amplifiers and can act as either switches or amplifiers depending on their configuration. In this note, we will focus on the fundamental concepts of transistors, including their operation, key formulas, problem-solving patterns, and examples.

### Core Concepts
-----------------

#### Bipolar Junction Transistor (BJT)

A BJT consists of three layers: two p-type regions separated by an n-type region. The two p-n junctions are the base-emitter (BE) junction and the collector-base (CB) junction. When a small current flows through the BE junction, it can control the larger current flowing through the CB junction.

#### Transistor Operation

* **Active Region**: In this mode, the transistor operates as an amplifier. The base-emitter voltage controls the collector current.
* **Saturation Region**: In this mode, the transistor is fully on, and the collector current is maximum.
* **Cut-off Region**: In this mode, the transistor is fully off, and the collector current is minimum.

### Key Formulas/Theorems
-------------------------

#### Current Gain

The current gain of a BJT is defined as:

$$\beta = \frac{I_C}{I_B}$$

where $I_C$ is the collector current and $I_B$ is the base current.

#### Ebers-Moll Model

The Ebers-Moll model describes the behavior of a BJT. It states that:

$$I_E = I_S \left( e^{\frac{V_{BE}}{V_T}} - 1 \right)$$

where $I_E$ is the emitter current, $I_S$ is the reverse saturation current, $V_{BE}$ is the base-emitter voltage, and $V_T$ is the thermal voltage.

### Problem Solving Patterns
---------------------------

#### Matched Transistors

When all transistors in a circuit are matched, they have the same current gain ($\beta$) and can be replaced with each other without affecting the circuit's behavior.

**Example:** Given that all transistors in a circuit have a current gain of 20 ($\beta = 20$), find the collector current $I_C$ when the base current is 1.25 mA.

Solution:

Since $\beta = \frac{I_C}{I_B}$, we can write:

$$I_C = \beta I_B = 20 \times 1.25 mA = 25 mA$$

#### Transistors with Different Current Gains

When transistors have different current gains, the collector current is affected.

**Example:** Given that transistor $Q_1$ has a current gain of $\beta_1 = 99$ and transistor $Q_2$ has a current gain of $\beta_2 = 49$, find the collector current $I_{C2}$ when the base current is 50 mA.

Solution:

We can use the Ebers-Moll model to write:

$$I_E = I_S \left( e^{\frac{V_{BE}}{V_T}} - 1 \right)$$

Since $\beta_1$ and $\beta_2$ are different, we have:

$$\frac{I_{C1}}{I_B} = \beta_1 \neq \frac{I_{C2}}{I_B} = \beta_2$$

To find $I_{C2}$, we can use the fact that:

$$I_E = I_S \left( e^{\frac{V_{BE}}{V_T}} - 1 \right) = I_{C2} + I_{B2}$$

Substituting $I_B = 50 mA$ and $\beta_2 = 49$, we get:

$$I_{C2} = \beta_2 I_B = 49 \times 50 mA = 2450 mA$$

However, the question asks for the current in microampere. To convert to microampere, divide by $1000$:

$$I_{C2} = \frac{2450 mA}{1000} = 2.45 A = 2450 \mu A$$