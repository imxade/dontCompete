**Electric Field**
================

### Introduction
----------------

The electric field is a fundamental concept in electromagnetism that describes the force experienced by a test charge at a given point in space. It's a vector field that encodes the distribution of electric charges and influences other charged objects.

### Core Concepts
------------------

#### Electric Field as a Vector Field
------------------------------------

*   The electric field $\mathbf{E}$ is defined as the force per unit charge, i.e., $\mathbf{F} = q\mathbf{E}$.
*   It's a vector field that points from positive to negative charges.

### Key Formulas/Theorems
-------------------------

#### Electric Field due to a Point Charge
--------------------------------------

$$\mathbf{E} = \frac{kq}{r^2}\hat{\mathbf{r}}$$

where:

*   $k$ is Coulomb's constant ($8.99 \times 10^9 \, \text{N}\cdot\text{m}^2/\text{C}^2$)
*   $q$ is the magnitude of the charge
*   $r$ is the distance from the charge to the point where the field is being measured
*   $\hat{\mathbf{r}}$ is the unit vector pointing radially away from the charge

#### Electric Field due to a Dipole
----------------------------------

$$\mathbf{E} = \frac{kq}{2}\left(\frac{\mathbf{r}}{r^3} - 3\frac{(\mathbf{r} \cdot \mathbf{p})\mathbf{r}}{r^5}\right)$$

where:

*   $\mathbf{p}$ is the dipole moment
*   $r$ is the distance from the dipole to the point where the field is being measured

### Problem Solving Patterns
---------------------------

#### Example 1: Electric Field due to a Point Charge
---------------------------------------------------

Suppose we have a charge of magnitude $q = 2 \, \text{C}$ located at the origin. Find the electric field at a distance of $r = 3 \, \text{m}$ from the charge.

**Solution**

Using the formula for the electric field due to a point charge:

$$\mathbf{E} = \frac{kq}{r^2}\hat{\mathbf{r}}$$

We can plug in the given values and calculate the result:

$$\mathbf{E} = \frac{(8.99 \times 10^9 \, \text{N}\cdot\text{m}^2/\text{C}^2)(2 \, \text{C})}{(3 \, \text{m})^2}\hat{\mathbf{r}}$$

$$= (5.99 \times 10^8 \, \text{N}/\text{C})\hat{\mathbf{r}}$$

#### Example 2: Electric Field due to a Dielectric Slab
----------------------------------------------------

Consider a large parallel plate capacitor with a gap filled entirely with a dielectric slab of relative permittivity $\epsilon_r = 5$. The plates are initially charged to a potential difference of $V$ volts and then disconnected from the source. If the dielectric slab is pulled out completely, find the ratio of the new electric field in the gap to the original electric field.

**Solution**

When the dielectric slab is inserted, the capacitance increases by a factor of $\epsilon_r$. When it's removed, the capacitance decreases back to its original value. Since the charge on the capacitor remains constant, the potential difference also decreases by the same factor:

$$V' = \frac{Q}{C'} = \frac{Q}{\epsilon_r C} = \frac{V}{5}$$

The electric field in a capacitor is given by:

$$E = \frac{V}{d}$$

where $d$ is the distance between the plates. Since the potential difference decreases by a factor of 5, the new electric field will be:

$$E' = \frac{V'}{d} = \frac{1}{5}\left(\frac{V}{d}\right) = \frac{1}{5}E$$

Therefore, the ratio of the new electric field to the original electric field is:

$$\frac{E'}{E} = \frac{1}{5}$$

### Common Pitfalls
--------------------

*   Forgetting that the electric field due to a point charge depends on the distance from the charge.
*   Misapplying formulas for electric fields due to dipoles or dielectric slabs.

### Quick Summary
------------------

*   Electric field is defined as force per unit charge ($\mathbf{F} = q\mathbf{E}$).
*   Key formulas: $E = \frac{kq}{r^2}\hat{\mathbf{r}}$ and $\mathbf{E} = \frac{kq}{2}\left(\frac{\mathbf{r}}{r^3} - 3\frac{(\mathbf{r} \cdot \mathbf{p})\mathbf{r}}{r^5}\right)$.
*   Electric field due to a point charge decreases with distance ($1/r^2$).
*   Dielectric slabs affect electric fields in capacitors by increasing or decreasing the capacitance.