**Radiation Heat Transfer**
==========================

### Introduction
Radiation heat transfer occurs due to the exchange of electromagnetic waves between objects, regardless of the medium or distance separating them. This mode of heat transfer is significant in high-temperature applications and when conduction and convection are negligible.

### Core Concepts

#### Blackbody Radiation
A blackbody is an idealized object that absorbs all incident radiation, with no reflection or transmission. The energy distribution of a blackbody's radiation is described by the **Planck's Law**:

$$B_{\lambda}(T) = \frac{2hc^2}{\lambda^5} \frac{1}{e^{hc/\lambda kT} - 1}$$

where $B_{\lambda}(T)$ is the spectral radiance, $\lambda$ is the wavelength, $h$ is Planck's constant, $c$ is the speed of light, and $k$ is Boltzmann's constant.

#### Emissivity
Emissivity ($\epsilon$) is a measure of an object's ability to emit radiation. It ranges from 0 (perfect reflector) to 1 (blackbody). The **Stefan-Boltzmann Law** relates the total energy radiated by an object to its temperature:

$$E = \sigma T^4$$

where $E$ is the total energy, $\sigma$ is the Stefan-Boltzmann constant, and $T$ is the temperature.

#### Radiation Shielding
A radiation shield is used to reduce heat transfer between two objects. The shield's emissivity and conductive resistance are critical in determining its effectiveness.

### Key Formulas/Theorems

$$\begin{align*}
E &= \sigma T^4\\
B_{\lambda}(T) &= \frac{2hc^2}{\lambda^5} \frac{1}{e^{hc/\lambda kT} - 1}\\
\epsilon &= \frac{\text{actual radiation}}{\text{blackbody radiation}}
\end{align*}$$

### Problem Solving Patterns

When dealing with radiation heat transfer, consider the following:

* Determine if the objects are in thermal equilibrium or not.
* Identify the mode of heat transfer (radiation, conduction, or convection).
* Use emissivity and absorptivity values to calculate energy exchange.

### Examples with Solutions

**Example 1:**
Two large parallel plates have temperatures $T_1 = 900\text{ K}$ and $T_2 = 300\text{ K}$. A radiation shield of low emissivity ($\epsilon_s \approx 0.05$) is placed between them.

* Step 1: Calculate the energy radiated by each plate:
$$E_1 = \sigma T_1^4, E_2 = \sigma T_2^4$$
* Step 2: Use the shield's emissivity to calculate the energy transmitted through it:
$$E_{\text{trans}} = E_1 \epsilon_s + E_2 (1 - \epsilon_s)$$

**Solution:** ($\sigma \approx 5.67 \times 10^{-8}\text{ W/m}^2\text{K}^4$)

$$E_1 \approx 2.04 \times 10^6\text{ W/m}^2, E_2 \approx 3.73 \times 10^3\text{ W/m}^2$$

$$E_{\text{trans}} \approx (2.04 \times 10^6)(0.05) + (3.73 \times 10^3)(1 - 0.05)$$
$$E_{\text{trans}} \approx 102000\text{ W/m}^2$$

The temperature of the shield ($T_s$) can be found by equating the energy transmitted through it to the energy radiated by it:

$$E_{\text{trans}} = E_s = \sigma T_s^4$$
$$T_s^4 = \frac{E_{\text{trans}}}{\sigma}$$

**Solution:** $T_s \approx 759\text{ K}$

### Common Pitfalls

* Failing to account for the shield's emissivity in radiation calculations.
* Incorrectly assuming thermal equilibrium between objects.

### Quick Summary
* Radiation heat transfer is significant at high temperatures and when conduction/convection are negligible.
* Use Planck's Law, Stefan-Boltzmann Law, and emissivity values to calculate energy exchange.
* Consider the shield's emissivity in radiation calculations.