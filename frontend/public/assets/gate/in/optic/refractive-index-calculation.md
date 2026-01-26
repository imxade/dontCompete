**Refractive Index Calculation**
=====================================

### Introduction
The refractive index of a medium is defined as the ratio of the speed of light in vacuum to the speed of light in that medium. It plays a crucial role in understanding how light behaves when passing from one medium to another. In this theory note, we will delve into the concepts and formulas required for calculating refractive indices.

### Core Concepts
#### Refractive Index (n)
The refractive index of a medium is denoted by $n$ and is defined as:

$$ n = \frac{c}{v} $$

where $c$ is the speed of light in vacuum ($3.00 \times 10^8$ m/s) and $v$ is the speed of light in the medium.

#### Snell's Law
When a light beam passes from one medium to another, it follows the law of refraction, also known as Snell's law:

$$ n_1 \sin(\theta_1) = n_2 \sin(\theta_2) $$

where $n_1$ and $n_2$ are the refractive indices of the two media, and $\theta_1$ and $\theta_2$ are the angles of incidence and refraction, respectively.

### Key Formulas/Theorems
$$ n = \frac{c}{v} $$

$$ n_1 \sin(\theta_1) = n_2 \sin(\theta_2) $$

### Problem Solving Patterns
#### Q1: Refractive Index Calculation for Optical Fibre Coupling
To calculate the minimum value of the focal length of the lens to attain maximum coupling to the fibre, we need to consider the refractive indices of the lens and the fibre.

Given:
- Refractive index of the lens ($n_l$) = 1.5
- Refractive index of the core of the fibre ($n_c$) = 1.55
- Refractive index of the cladding of the fibre ($n_{cl}$) = 1.54

We can use Snell's law to relate the angles of incidence and refraction:

$$ n_l \sin(\theta_1) = n_f \sin(\theta_2) $$

where $n_f$ is the refractive index of the fibre.

To maximize coupling, we need to minimize the focal length of the lens. This can be achieved by minimizing the angle of incidence ($\theta_1$).

#### Q2: Refractive Index Calculation for Destructive Interference
In this problem, light of wavelength 600 nm is incident normally on a slab of finite thickness $t$. For destructive interference to occur at point R, the path difference must be either $\frac{\lambda}{2}$ or an odd multiple of $\frac{\lambda}{2}$.

Given:
- Wavelength ($\lambda$) = 600 nm
- Refractive index of the slab ($n_s$) = 1.5

We can use the formula for path difference:

$$ \Delta x = t(n_s - n_0) $$

where $n_0$ is the refractive index of air (approximately equal to 1).

### Examples with Solutions
**Example 1: Refractive Index Calculation for Optical Fibre Coupling**

Given:
- Beam diameter = 10 mm
- Focal length = ?

We can use Snell's law to relate the angles of incidence and refraction:

$$ n_l \sin(\theta_1) = n_f \sin(\theta_2) $$

where $n_l$ is the refractive index of the lens, $n_f$ is the refractive index of the fibre, $\theta_1$ is the angle of incidence, and $\theta_2$ is the angle of refraction.

To minimize the focal length, we need to maximize the angle of incidence ($\theta_1$). This can be achieved by maximizing the refractive index of the lens.

```python
import math

# Given values
nl = 1.5  # Refractive index of the lens
nc = 1.55  # Refractive index of the core of the fibre
ncl = 1.54  # Refractive index of the cladding of the fibre
focal_length = 27.5 / (nl * nc)  # Minimum value of focal length

print("The minimum value of the focal length is:", focal_length, "mm")
```

**Example 2: Refractive Index Calculation for Destructive Interference**

Given:
- Wavelength ($\lambda$) = 600 nm
- Thickness of slab ($t$) = ?

We can use the formula for path difference:

$$ \Delta x = t(n_s - n_0) $$

where $n_s$ is the refractive index of the slab and $n_0$ is the refractive index of air (approximately equal to 1).

```python
import math

# Given values
lambda_val = 600e-9  # Wavelength in meters
ns = 1.5  # Refractive index of the slab

# Calculate thickness for destructive interference
t_min = lambda_val / 2  # Minimum value of thickness

print("The minimum value of thickness is:", t_min * 1000, "nm")
```

### Common Pitfalls
- Students often forget to consider the refractive indices of the media involved.
- They may not apply Snell's law correctly or use incorrect values for the angles.

### Quick Summary

* Refractive index ($n$) = $\frac{c}{v}$
* Snell's law: $n_1 \sin(\theta_1) = n_2 \sin(\theta_2)$
* Path difference for destructive interference: $\Delta x = t(n_s - n_0)$