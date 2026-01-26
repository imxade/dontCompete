**Transportation Infrastructure**
==============================

**Introduction**
---------------

Transportation infrastructure refers to the physical systems and networks that facilitate the movement of people, goods, and services. In this note, we will focus on railway design, specifically for broad gauge sections.

**Core Concepts**
-----------------

### Railway Design Principles

Railway design involves the planning and construction of tracks, including curves, straight sections, and intersections. Key considerations include:

* **Speed**: The speed at which trains operate affects the required cant (tilt) to maintain stability.
* **Gauge**: The center-to-center distance between rail heads affects the cant and wheel loading.
* **Radius**: The curvature of the track influences the design of curves.

### Equilibrium Cant

Equilibrium cant is the angle of tilt required for a train to maintain stability on a curved section. It depends on:

* Speed
* Radius
* Gauge

The following formula can be used to calculate equilibrium cant:

$$\tan \theta = \frac{v^2}{g r}$$

where $\theta$ is the equilibrium cant, $v$ is the speed of the train, $g$ is the acceleration due to gravity ($9.81 m/s^2$), and $r$ is the radius of curvature.

### Safety Factors

To ensure safety, additional factors are applied to the calculated cant:

* **Loading factor**: accounts for axle loads and wheel loading
* **Gauge factor**: accounts for gauge variation

The formula becomes:

$$\tan \theta = \frac{v^2}{g r} \cdot \text{loading factor} \cdot \text{gauge factor}$$

**Key Formulas/Theorems**
-------------------------

### Equilibrium Cant Formula

$$\tan \theta = \frac{v^2}{g r}$$

### Safety Factors Formula

$$\tan \theta = \frac{v^2}{g r} \cdot \text{loading factor} \cdot \text{gauge factor}$$

**Problem Solving Patterns**
---------------------------

### Step-by-Step Approach

1. Identify the given parameters: speed, radius, gauge.
2. Calculate the equilibrium cant using the formula.
3. Apply safety factors to account for loading and gauge variation.

**Examples with Solutions**
-------------------------

### Example 1:

A train travels at $40 km/h$ on a curved section with a radius of $437 m$. The gauge is $1750 mm$. Calculate the required equilibrium cant.

```latex
v = 40 \cdot 1000/3600 = 11.11 m/s \\
g = 9.81 m/s^2 \\
r = 437 m \\
\theta = \arctan{\frac{v^2}{gr}} = \arctan{\frac{(11.11)^2}{9.81 \cdot 437}} \approx 1.25^\circ
```

### Example 2:

A train travels at $60 km/h$ on a curved section with a radius of $437 m$. The gauge is $1750 mm$. Calculate the required equilibrium cant.

```latex
v = 60 \cdot 1000/3600 = 16.67 m/s \\
g = 9.81 m/s^2 \\
r = 437 m \\
\theta = \arctan{\frac{v^2}{gr}} = \arctan{\frac{(16.67)^2}{9.81 \cdot 437}} \approx 1.83^\circ
```

**Common Pitfalls**
------------------

* **Incorrect units**: Ensure consistent units for speed, radius, and gauge.
* **Oversight of safety factors**: Remember to apply loading and gauge variation factors.

**Quick Summary**
-----------------

* Equilibrium cant depends on speed, radius, and gauge.
* Safety factors account for axle loads and gauge variation.
* Use the equilibrium cant formula: $\tan \theta = \frac{v^2}{g r}$.
* Apply safety factors to ensure accuracy.

Note: The theory content is based on the provided source questions. Further research may be necessary to cover additional topics or nuances in railway design.