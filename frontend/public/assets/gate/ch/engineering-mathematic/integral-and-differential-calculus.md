**Integral and Differential Calculus**
=====================================

**Introduction**
---------------

Calculus is a branch of mathematics that deals with the study of continuous change, particularly in the context of functions and limits. It has two main branches: Differential Calculus (study of rates of change and slopes) and Integral Calculus (study of accumulation of quantities). In this note, we will focus on integral calculus, specifically dealing with polar coordinates.

**Core Concepts**
----------------

### Polar Coordinates

Polar coordinates are a way to represent points in a plane using a distance (`r`) from the origin and an angle (`θ`) measured counterclockwise from the positive x-axis. The conversion between Cartesian (rectangular) coordinates (`x`, `y`) and polar coordinates is given by:

* `x = r cos(θ)`
* `y = r sin(θ)`

### Area of a Region in Polar Coordinates

The area of a region bounded by a curve `r = f(θ)` can be calculated using the formula:

`Area = ∫[α, β] (1/2)r² dθ`

where `α` and `β` are the limits of integration.

### Area of a Cardioid

A cardioid is a special type of curve that has the equation `r = a(1 - cos(θ))`. To find the area of the cardioid, we can use the formula for area in polar coordinates:

`Area = ∫[0, 2π] (1/2)(a(1 - cos(θ)))² dθ`

**Key Formulas/Theorems**
-------------------------

* `∫[α, β] f(x) dx`: Area under a curve
* `∫[α, β] r² dθ`: Area of a region in polar coordinates

```latex
\int_{0}^{2\pi} \frac{1}{2}(a(1 - \cos(\theta)))^2 d\theta = \frac{\pi a^2}{2}
```

**Problem Solving Patterns**
---------------------------

### Cardioid Area Problem

When solving problems involving the area of a cardioid, remember to:

* Convert the polar equation to Cartesian coordinates (if necessary)
* Use the formula for area in polar coordinates
* Integrate with respect to `θ` from 0 to 2π

**Examples with Solutions**
---------------------------

### Example 1: Area of a Cardioid

Find the area of the cardioid given by `r = a(1 - cos(θ))`, where `a = 2`.

```latex
\int_{0}^{2\pi} \frac{1}{2}(2(1 - \cos(\theta)))^2 d\theta
= \frac{\pi (2)^2}{2}
= \boxed{2\pi}
```

### Example 2: Area of a Region in Polar Coordinates

Find the area of the region bounded by the curve `r = 3 + 2 sin(θ)`.

```latex
\int_{0}^{\pi/2} \frac{1}{2}(3 + 2 \sin(\theta))^2 d\theta
= \boxed{9}
```

**Common Pitfalls**
------------------

* Forgetting to convert polar equations to Cartesian coordinates when necessary
* Incorrectly applying formulas for area in polar coordinates

**Quick Summary**
-----------------

* Polar coordinates: `x = r cos(θ)`, `y = r sin(θ)`
* Area of a region in polar coordinates: `∫[α, β] (1/2)r² dθ`
* Cardioid area formula: `∫[0, 2π] (1/2)(a(1 - cos(θ)))² dθ`

Note: This is just one possible way to create a comprehensive theory note. The format and content may be adjusted based on specific requirements or preferences.