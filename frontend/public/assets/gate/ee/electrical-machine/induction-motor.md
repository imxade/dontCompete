**Induction Motor**
================

### Introduction
An induction motor is a type of AC electric motor that uses electromagnetic induction to produce torque and motion. It consists of a stator (stationary part) with windings that carry alternating current, and a rotor (rotating part) that also carries alternating current.

### Core Concepts
The operation of an induction motor can be understood using the following concepts:

* **Electromagnetic Induction**: The principle that an electromotive force is induced in a conductor when it moves through a magnetic field.
* **Synchronous Speed**: The speed at which the rotating magnetic field produced by the stator windings would rotate if the rotor were not present.
* **Rotor Slippage**: The difference between the synchronous speed and the actual speed of the rotor.

### Key Formulas/Theorems
The following formulas are crucial for understanding induction motors:

$$f_s = \frac{P \cdot f}{120} \text{ (synchronous speed)}$$

$$N_r = \left(1 - \frac{s}{P}\right) \times N_s \text{ (rotor speed)}$$

where:
- $f_s$ is the synchronous speed,
- $P$ is the number of poles in the motor,
- $f$ is the frequency of the AC supply,
- $N_r$ is the rotor speed,
- $s$ is the slip, and
- $N_s$ is the synchronous speed.

### Problem Solving Patterns
To solve induction motor problems, follow these steps:

1. Identify the given parameters: number of poles ($P$), frequency of AC supply ($f$), and rotor speed ($N_r$).
2. Calculate the synchronous speed using the formula above.
3. Use the rotor speed to find the slip.
4. Substitute the values into the formula for rotor speed to find the actual speed.

### Examples with Solutions

**Example 1**
A three-phase, 8-pole induction motor has a frequency of 40 Hz and operates at 585 rpm. What is its synchronous speed?

Solution:
Using the formula above:

$$f_s = \frac{P \cdot f}{120} = \frac{8 \cdot 40}{120} = 26.67 \text{ rps}$$

Since there are 60 seconds in a minute, we convert this to rpm:

$$N_s = 26.67 \times 60 = 1600 \text{ rpm}$$

**Example 2**
An induction motor has a synchronous speed of 1000 rpm and operates at 900 rpm. What is its slip?

Solution:
Using the formula for rotor speed:

$$N_r = (1 - s/P) \times N_s$$

We are given $N_r$ as 900 rpm, $N_s$ as 1000 rpm, and we need to find $s$. Rearranging the formula:

$$s = P\left(1 - \frac{N_r}{N_s}\right) = 4\left(1 - \frac{900}{1000}\right) = 2$$

### Common Pitfalls
Be cautious of these common mistakes when dealing with induction motors:

* Confusing synchronous speed and rotor speed.
* Not considering the number of poles in calculations.

### Quick Summary
Key points to remember:

* Induction motor uses electromagnetic induction for operation.
* Synchronous speed is calculated using $f_s = P \cdot f / 120$.
* Rotor speed is related to slip and synchronous speed by $N_r = (1 - s/P) \times N_s$.