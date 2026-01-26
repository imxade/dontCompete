**Plane Waves and Properties**
==========================

**Introduction**
---------------

A uniform plane wave is a fundamental solution to Maxwell's equations, representing a propagating disturbance in an electromagnetic field. It is characterized by its electric and magnetic field components, which oscillate in phase with each other.

**Core Concepts**
-----------------

### Electric and Magnetic Fields

In a uniform plane wave, the electric field $\mathbf{E}$ and magnetic field $\mathbf{H}$ are perpendicular to each other and to the direction of propagation. The electric field is represented by $E_x$ in the x-direction, $E_y$ in the y-direction, and $E_z$ in the z-direction.

### Wave Equation

The wave equation for a uniform plane wave is given by:

$$\nabla^2 \mathbf{E} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$$

where $\mu_0$ is the permeability of free space and $\epsilon_0$ is the permittivity of free space.

### Phase Velocity

The phase velocity $v_p$ of a uniform plane wave is given by:

$$v_p = \frac{c}{\sqrt{\mu_r \epsilon_r}}$$

where $c$ is the speed of light in vacuum, $\mu_r$ is the relative permeability of the medium, and $\epsilon_r$ is the relative permittivity of the medium.

**Key Formulas/Theorems**
-------------------------

### Plane Wave Equation

The plane wave equation for a uniform plane wave is given by:

$$\mathbf{E}(\mathbf{r}, t) = \hat{\mathbf{x}} E_0 \cos(kx - \omega t + \phi_x) + \hat{\mathbf{y}} E_0 \cos(ky - \omega t + \phi_y)$$

where $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$ are unit vectors in the x and y directions, respectively.

### Magnetic Field Components

The magnetic field components for a uniform plane wave are given by:

$$\begin{aligned}
B_x &= 0 \\
B_y &= 0 \\
B_z &= \frac{\omega}{v_p} E_0 \cos(kx - \omega t + \phi_x)
\end{aligned}$$

### Power Flow

The power flow $P$ for a uniform plane wave is given by:

$$P = \frac{1}{2} \frac{E_0^2}{\eta}$$

where $\eta$ is the intrinsic impedance of the medium.

**Problem Solving Patterns**
---------------------------

### Identifying Wave Components

When solving problems involving plane waves, it's essential to identify the wave components (electric and magnetic fields) and their direction of propagation. This can be done by analyzing the given equations or diagrams.

### Applying Wave Equation

To solve problems involving wave propagation, apply the wave equation for a uniform plane wave:

$$\nabla^2 \mathbf{E} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$$

**Examples with Solutions**
-------------------------

### Example 1: Plane Wave Equation

Given the electric field components $E_x$ and $E_y$, derive the plane wave equation for a uniform plane wave.

Solution:
The plane wave equation is given by:

$$\mathbf{E}(\mathbf{r}, t) = \hat{\mathbf{x}} E_0 \cos(kx - \omega t + \phi_x) + \hat{\mathbf{y}} E_0 \cos(ky - \omega t + \phi_y)$$

where $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$ are unit vectors in the x and y directions, respectively.

### Example 2: Magnetic Field Components

Given the electric field components $E_x$ and $E_y$, derive the magnetic field components for a uniform plane wave.

Solution:
The magnetic field components are given by:

$$\begin{aligned}
B_x &= 0 \\
B_y &= 0 \\
B_z &= \frac{\omega}{v_p} E_0 \cos(kx - \omega t + \phi_x)
\end{aligned}$$

**Common Pitfalls**
------------------

### Inconsistent Units

Be careful to use consistent units when solving problems involving plane waves.

### Overlooking Wave Components

Make sure to identify all wave components (electric and magnetic fields) in a given problem.

**Quick Summary**
-----------------

* Uniform plane wave equation: $\mathbf{E}(\mathbf{r}, t) = \hat{\mathbf{x}} E_0 \cos(kx - \omega t + \phi_x) + \hat{\mathbf{y}} E_0 \cos(ky - \omega t + \phi_y)$
* Magnetic field components: $B_x = 0, B_y = 0, B_z = \frac{\omega}{v_p} E_0 \cos(kx - \omega t + \phi_x)$
* Power flow: $P = \frac{1}{2} \frac{E_0^2}{\eta}$