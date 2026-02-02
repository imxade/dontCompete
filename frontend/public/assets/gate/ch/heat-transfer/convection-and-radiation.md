**Heat Transfer - Convection and Radiation**
==============================================

### Introduction
---------------

Heat transfer occurs through three primary mechanisms: conduction, convection, and radiation. In this section, we will focus on convection and radiation, with a special emphasis on their application in heat exchangers.

### Core Concepts
------------------

### Convection

Convection is the transfer of heat through the movement of fluids. It occurs when there is a temperature difference between two regions of a fluid, causing it to expand or contract, resulting in bulk motion.

**Newton's Law of Cooling**

$$\frac{dT}{dt} = -k(T - T_{env})$$

where $T$ is the temperature of the object, $T_{env}$ is the ambient temperature, and $k$ is a constant.

### Radiation

Radiation is the transfer of heat through electromagnetic waves. It does not require a medium to propagate and occurs between objects at all temperatures.

**Stefan-Boltzmann Law**

$$Q = \epsilon \sigma A (T^4 - T_{env}^4)$$

where $Q$ is the rate of heat transfer, $\epsilon$ is the emissivity of the object, $\sigma$ is the Stefan-Boltzmann constant, $A$ is the surface area of the object, and $T$ and $T_{env}$ are the temperatures of the object and its environment, respectively.

### Key Formulas/Theorems
-------------------------

* **Heat Exchanger Effectiveness**
$$\epsilon = \frac{Q}{C_p (T_{in} - T_{out})}$$
* **Number of Transfer Units (NTU)**
$$NTU = \frac{UA}{C_p}$$

### Problem Solving Patterns
---------------------------

1.  Identify the type of heat transfer mechanism involved (convection, radiation, or conduction).
2.  Apply the relevant equations and formulas to calculate the required quantities (heat transfer rate, temperature difference, etc.).
3.  Use dimensional analysis to check units and ensure consistency.

### Examples with Solutions
---------------------------

1.  **Convection**

    *   Problem: A fluid flows through a pipe with an inner diameter of 0.05 m and a length of 10 m. The inlet temperature is 100°C, and the outlet temperature is 80°C. If the specific heat capacity is 4186 J/kg·K, calculate the mass flow rate.

    *   Solution:

        \begin{align*}
        Q &= C_p \dot{m} (T_{in} - T_{out}) \\
        &\Rightarrow \dot{m} = \frac{Q}{C_p (T_{in} - T_{out})} \\
        &\text{Apply heat exchanger effectiveness:}\\
        &\epsilon = \frac{Q}{C_p (T_{in} - T_{out})} \\
        &\Rightarrow Q = C_p \dot{m} (T_{in} - T_{out}) \\
        &\text{Given } A = \pi d L,\\
        &Q = k A \frac{\Delta T}{L}\\
        &\text{Since } \epsilon = 1,\\
        &C_p \dot{m} (T_{in} - T_{out}) = k A \frac{(T_{in} - T_{out})}{L}\\
        &\Rightarrow \dot{m} = \frac{k A}{C_p L}
        \end{align*}

    *   **Answer:** $\boxed{\text{Calculate } k, \epsilon}$

2.  **Radiation**

    *   Problem: Two objects with emissivities of 0.8 and 0.9 are at temperatures of 100°C and 80°C, respectively. Calculate the heat transfer rate between them.

    *   Solution:

        \begin{align*}
        Q &= \epsilon_1 \sigma A (T_1^4 - T_{env}^4) + \epsilon_2 \sigma A (T_2^4 - T_{env}^4)\\
        &\text{Apply Stefan-Boltzmann law:}\\
        &Q = \epsilon \sigma A (T^4 - T_{env}^4)\\
        &\Rightarrow Q = (\epsilon_1 + \epsilon_2) \sigma A ((T_1^4 - T_2^4))
        \end{align*}

    *   **Answer:** $\boxed{\text{Calculate } Q}$

### Common Pitfalls
------------------

*   Incorrect application of heat transfer mechanisms (convection, radiation, or conduction).
*   Failure to identify the correct equation and formula for the problem at hand.
*   Ignoring units and dimensional analysis.

### Quick Summary
-----------------

| Concept | Key Points |
| --- | --- |
| Convection | Newton's Law of Cooling; heat transfer through fluid motion. |
| Radiation | Stefan-Boltzmann Law; heat transfer through electromagnetic waves. |
| Heat Exchanger Effectiveness | $\epsilon = \frac{Q}{C_p (T_{in} - T_{out})}$ |
| Number of Transfer Units (NTU) | $NTU = \frac{UA}{C_p}$ |

### References
---------------

1.  **[1]**: Bejan, A., & Kraus, A. D. (2003). _Heat transfer handbook_. John Wiley & Sons.
2.  **[2]**: Incropera, F. P., & Dewitt, D. P. (1996). _Fundamentals of heat and mass transfer_.

Note: The above examples are simplified for demonstration purposes. In practice, you may need to consider additional factors such as fluid properties, geometry, and boundary conditions.