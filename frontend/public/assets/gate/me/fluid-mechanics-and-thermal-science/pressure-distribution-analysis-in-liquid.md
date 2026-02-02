**Pressure Distribution Analysis in Liquids**
=============================================

**Introduction**
---------------

In fluid mechanics and thermal science, understanding pressure distribution in liquids is crucial for designing vessels, piping systems, and other equipment. This note will cover the theoretical concepts, formulas, and insights required to analyze pressure distribution in liquids.

**Core Concepts**
-----------------

### Pressure Distribution in Liquids

Pressure in a liquid increases with depth due to the weight of the liquid above. The pressure at any point in a static liquid is given by:

$$P = \rho g h + P_0$$

where:
- $P$ is the pressure at the point
- $\rho$ is the density of the liquid
- $g$ is the acceleration due to gravity
- $h$ is the depth below the surface
- $P_0$ is atmospheric pressure (neglected in this analysis)

### Hydrostatic Pressure

Hydrostatic pressure is the pressure exerted by a fluid at equilibrium at any point of the fluid due to the force of gravity. It is given by:

$$P = \rho g z + P_0$$

where:
- $z$ is the vertical distance below the surface

**Key Formulas/Theorems**
-------------------------

* **Pressure Distribution in Liquids**: $P = \rho g h$
* **Hydrostatic Pressure**: $P = \rho g z$

### Stress Analysis for Cylindrical Vessels

For a cylindrical vessel, the stress analysis involves considering both axial and circumferential stresses. The stresses are given by:

$$\sigma_1 = \frac{p r}{t}$$
$$\sigma_2 = \frac{p r}{2 t}$$

where:
- $\sigma_1$ is the axial wall stress
- $\sigma_2$ is the circumferential wall stress
- $p$ is the internal pressure
- $r$ is the radius of the vessel
- $t$ is the wall thickness

**Problem Solving Patterns**
---------------------------

* **Identify key assumptions**: Neglect atmospheric pressure, weight of vessel, and bending stresses.
* **Apply pressure distribution formulas**: Use $\rho g h$ to calculate pressure at any point.
* **Perform stress analysis**: Calculate axial and circumferential stresses using the formulae above.

**Examples with Solutions**
---------------------------

### Example 1: Pressure Distribution in a Liquid

A cylindrical vessel contains a liquid of density $1000 \, \text{kg/m}^3$. The height of the liquid is $5 \, \text{m}$ and atmospheric pressure is neglected. Calculate the pressure at a depth of $2 \, \text{m}$ below the surface.

```latex
\begin{align*}
P &= \rho g h \\
&= 1000 \times 9.81 \times 2 \\
&= 19620 \, \text{Pa} \\
\end{align*}
```

### Example 2: Stress Analysis for a Cylindrical Vessel

A cylindrical vessel of radius $1 \, \text{m}$ and wall thickness $0.05 \, \text{m}$ contains an internal pressure of $100000 \, \text{Pa}$. Calculate the axial and circumferential stresses.

```latex
\begin{align*}
\sigma_1 &= \frac{p r}{t} \\
&= \frac{100000 \times 1}{0.05} \\
&= 2000000 \, \text{Pa} \\
\end{align*}

\begin{align*}
\sigma_2 &= \frac{p r}{2 t} \\
&= \frac{100000 \times 1}{2 \times 0.05} \\
&= 1000000 \, \text{Pa} \\
\end{align*}
```

**Common Pitfalls**
------------------

* Neglecting atmospheric pressure or weight of the vessel
* Incorrectly applying stress analysis formulas
* Not identifying key assumptions

**Quick Summary**
-----------------

* Pressure distribution in liquids: $P = \rho g h$
* Hydrostatic pressure: $P = \rho g z$
* Stress analysis for cylindrical vessels:
	+ Axial wall stress: $\sigma_1 = \frac{p r}{t}$
	+ Circumferential wall stress: $\sigma_2 = \frac{p r}{2 t}$