**Magnetic Field and Plane Wave**
================================

### Introduction
-----------------

A plane wave is a type of electromagnetic wave that propagates through a medium, such as vacuum or air. The magnetic field of a uniform plane wave in vacuum is given by the equation:

$$\mathbf{H} = \frac{1}{2}\sqrt{\frac{\epsilon_0}{\mu_0}}E\cos(\omega t - k\cdot r)\hat{x} + \sin(\omega t - k\cdot r)\hat{y}$$

where $\mathbf{H}$ is the magnetic field, $E$ is the electric field, $\epsilon_0$ is the permittivity of free space, $\mu_0$ is the permeability of free space, $\omega$ is the angular frequency, and $k$ is the wave number.

### Core Concepts
-----------------

* **Electromagnetic Waves**: Electromagnetic waves are oscillations that can propagate through a medium. They consist of electric and magnetic fields that vary sinusoidally in time.
* **Plane Wave**: A plane wave is a type of electromagnetic wave that propagates in a single direction, with the electric and magnetic field vectors perpendicular to each other and to the direction of propagation.
* **Poynting Vector**: The Poynting vector ($\mathbf{S}$) is a measure of the energy flow through a surface. It is given by:

$$\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{H}$$

### Key Formulas/Theorems
---------------------------

* **Plane Wave Equation**: The plane wave equation is given by:

$$\nabla^2\mathbf{E} - \mu_0\epsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2} = 0$$

* **Poynting Theorem**: The Poynting theorem states that the energy flow through a surface is given by:

$$\nabla\cdot\mathbf{S} + \mu_0\epsilon_0\frac{\partial}{\partial t}\left(\frac{1}{2}\mathbf{E}\cdot\mathbf{E}\right) = -\mathbf{J}\cdot\mathbf{E}$$

where $\mathbf{J}$ is the current density.

### Problem Solving Patterns
-----------------------------

* **Identify the type of wave**: Determine whether the problem involves a plane wave, spherical wave, or other types of waves.
* **Use the plane wave equation**: Use the plane wave equation to solve problems involving electromagnetic waves in free space.
* **Apply the Poynting theorem**: Apply the Poynting theorem to calculate energy flow through surfaces.

### Examples with Solutions
-----------------------------

* **Example 1**: A uniform plane wave has an electric field of $E_0 = 10\text{ V/m}$ and propagates in free space. Calculate the magnetic field.
	+ Solution: Using the equation for the magnetic field, we get:

$$H_x = \frac{1}{2}\sqrt{\frac{\epsilon_0}{\mu_0}}E_0\cos(\omega t - k\cdot r)$$

where $\epsilon_0 = 8.85\times10^{-12}\text{ F/m}$ and $\mu_0 = 4\pi\times10^{-7}\text{ H/m}$. Substituting the values, we get:

$$H_x = \frac{1}{2}\sqrt{\frac{(8.85\times10^{-12})(4\pi\times10^{7})}{(4\pi\times10^{-7})}}(10)\cos(\omega t - k\cdot r)$$

Simplifying, we get:

$$H_x = 1.414\times10^{3}\cos(\omega t - k\cdot r)$$
* **Example 2**: A uniform plane wave has an electric field of $E_0 = 20\text{ V/m}$ and propagates in free space. Calculate the Poynting vector.
	+ Solution: Using the equation for the Poynting vector, we get:

$$S_x = \frac{1}{\mu_0}E_0H_y$$

where $H_y$ is given by the magnetic field equation:

$$H_y = \sin(\omega t - k\cdot r)$$

Substituting the values, we get:

$$S_x = \frac{(20)(\sin(\omega t - k\cdot r))}{(4\pi\times10^{-7})}$$

Simplifying, we get:

$$S_x = 5.027\times10^{6}\sin(\omega t - k\cdot r)$$

### Common Pitfalls
---------------------

* **Incorrect application of the plane wave equation**: Make sure to use the correct form of the plane wave equation for free space.
* **Ignoring boundary conditions**: Pay attention to boundary conditions when solving problems involving electromagnetic waves in different media.

### Quick Summary
------------------

* Plane waves are a type of electromagnetic wave that propagates through free space.
* The magnetic field of a uniform plane wave is given by:

$$\mathbf{H} = \frac{1}{2}\sqrt{\frac{\epsilon_0}{\mu_0}}E\cos(\omega t - k\cdot r)\hat{x} + \sin(\omega t - k\cdot r)\hat{y}$$

* Use the plane wave equation and Poynting theorem to solve problems involving electromagnetic waves in free space.