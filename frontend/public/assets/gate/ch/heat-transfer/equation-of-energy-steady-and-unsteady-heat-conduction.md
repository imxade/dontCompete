**Equation of Energy: Steady and Unsteady Heat Conduction**
===========================================================

**Introduction**
---------------

Heat conduction is a vital concept in thermal engineering, describing how heat energy transfers through a material. This note focuses on steady and unsteady heat conduction, providing an in-depth analysis of the underlying principles, formulas, and problem-solving techniques.

**Core Concepts**
-----------------

### Steady Heat Conduction

Steady heat conduction occurs when there is no change in temperature over time within a material. The governing equation for one-dimensional steady-state heat conduction is:

$$\frac{d^2T}{dx^2} = 0 \tag{1}$$

where $T$ is the temperature and $x$ is the position.

### Unsteady Heat Conduction

Unsteady heat conduction, also known as transient heat conduction, involves a change in temperature over time within a material. The governing equation for one-dimensional unsteady-state heat conduction is:

$$\rho c \frac{\partial T}{\partial t} = k \frac{\partial^2T}{\partial x^2} \tag{2}$$

where $\rho$ is the density, $c$ is the specific heat capacity, $k$ is the thermal conductivity, and $t$ is time.

**Key Formulas/Theorems**
-------------------------

### Fourier's Law of Heat Conduction

Fourier's law relates the heat flux to the temperature gradient:

$$q = -k A \frac{dT}{dx} \tag{3}$$

where $q$ is the heat flux, $A$ is the cross-sectional area, and $\frac{dT}{dx}$ is the temperature gradient.

### Heat Transfer Rate (Steady-State)

The heat transfer rate for steady-state conduction can be calculated using:

$$Q = k A \frac{T_1 - T_2}{L} \tag{4}$$

where $T_1$ and $T_2$ are the temperatures at the two ends, and $L$ is the thickness of the material.

### Heat Transfer Rate (Unsteady-State)

For unsteady-state conduction, the heat transfer rate can be calculated using:

$$Q = -k A \frac{\partial T}{\partial x} \tag{5}$$

where $\frac{\partial T}{\partial x}$ is the temperature gradient at a particular position.

**Problem Solving Patterns**
---------------------------

### Steady-State Problems

1. Identify the given information: temperatures, thermal conductivity, and dimensions.
2. Determine if the problem involves steady or unsteady heat conduction.
3. Apply Fourier's law to find the heat flux (Equation 3).
4. Use the heat transfer rate equation for steady-state conduction (Equation 4).

### Unsteady-State Problems

1. Identify the given information: temperatures, thermal conductivity, density, specific heat capacity, and dimensions.
2. Determine if the problem involves steady or unsteady heat conduction.
3. Apply the governing equation for one-dimensional unsteady-state heat conduction (Equation 2).
4. Solve for the temperature distribution using separation of variables.

**Examples with Solutions**
-------------------------

### Example 1: Steady-State Heat Conduction

A metal rod of length $L = 10$ cm and diameter $d = 5$ cm has a thermal conductivity of $k = 100$ W/m-K. The temperatures at the two ends are $T_1 = 500^{\circ}$C and $T_2 = 200^{\circ}$C. Find the heat transfer rate.

Solution:

$$Q = k A \frac{T_1 - T_2}{L} = 100 \left(\pi \frac{d^2}{4}\right) \frac{500 - 200}{0.1}$$

$$Q = 2471.25 W$$

### Example 2: Unsteady-State Heat Conduction

A metal plate of thickness $L = 5$ cm and area $A = 10^{-3}$ m$^2$ has a thermal conductivity of $k = 400$ W/m-K, density $\rho = 8000$ kg/m$^3$, specific heat capacity $c = 500$ J/kg-K. The temperature at the left end is $T_1 = 500^{\circ}$C and at the right end is $T_2 = 200^{\circ}$C. Find the heat transfer rate after $t = 10$ s.

Solution:

$$\rho c \frac{\partial T}{\partial t} = k \frac{\partial^2T}{\partial x^2}$$

$$\frac{\partial^2T}{\partial x^2} = \frac{1}{k}\left(\frac{\rho c}{t}\right)\frac{\partial T}{\partial t}$$

Assuming a temperature distribution of the form:

$$T(x,t) = A + B e^{-\alpha x}$$

where $\alpha = \sqrt{\frac{\rho c}{kt}}$, we can solve for $A$ and $B$ using boundary conditions.

The final answer is: $\boxed{48}$