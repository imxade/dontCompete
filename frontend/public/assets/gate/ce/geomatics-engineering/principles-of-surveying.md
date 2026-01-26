**Principles of Surveying**
==========================

### Introduction

Surveying is a branch of geomatics engineering that deals with determining the position and properties of natural features, such as boundaries, terrain, and monuments. It involves the collection and analysis of spatial data to create accurate maps and models of the physical environment.

### Core Concepts

#### 1. Theodolite Surveying

A theodolite is an optical instrument used for measuring angles between visible celestial bodies or points on a map. The main components of a theodolite are:

* **Telescope**: used to observe distant objects
* **Level**: ensures the theodolite's axis is horizontal
* **Circle and Graduation**: measure angles in degrees, minutes, and seconds

The process of setting up a theodolite involves the following steps:

1. Leveling the instrument to ensure its axis is horizontal.
2. Setting the telescope to observe the object (e.g., a staff or landmark).
3. Reading the angle between the object and the instrument's vertical axis.

#### 2. Zenith Angle

The zenith angle is the angle between the direction of an object and the vertical plane passing through the observer's location. It is used in triangulation surveys to determine distances and positions.

Given a zenith angle (Z) and the vertical angle (V), we can calculate the difference:

$oxed{\text{Δ} = Z - V}$

**Example:**

If the zenith angle is 93°00'00'' and the vertical angle is A93°, then:

$\text{Δ} = 93^{\circ}00'00'' - A93^{\circ} = -3^{\circ}00'00''$

#### 3. Horizontal Distance

The horizontal distance between two points can be calculated using trigonometry, given the angle and one of the distances.

Let $\theta$ be the angle, $d_1$ be the known distance, and $d_2$ be the unknown distance:

$d_2 = d_1 \cdot \tan(\theta)$

**Example:**

If the horizontal distance between two points is 400m and the angle is A7°, then:

$d_2 = 400 \cdot \tan(A7^{\circ})$

### Key Formulas/Theorems

* **Trigonometric Formulae**
	+ $\sin(\theta) = \frac{\text{opposite}}{\text{hypotenuse}}$
	+ $\cos(\theta) = \frac{\text{adjacent}}{\text{hypotenuse}}$
	+ $\tan(\theta) = \frac{\text{opposite}}{\text{adjacent}}$

### Problem Solving Patterns

1. **Theodolite Surveying:**
	* Use the angle and distance between two points to calculate the horizontal distance.
	* Apply trigonometric formulae to solve problems involving zenith angles and vertical angles.
2. **Distance Measurement:**
	* Use trigonometry to calculate distances given an angle and one of the sides.

### Examples with Solutions

**Q1:** A theodolite is set up at station A. The RL of instrument axis is 212.250 m. The angle of elevation to the top of a 4m long staff, held vertical at station B, is A7°. The horizontal distance between stations A and B is 400m. Neglecting the errors due to curvature of earth and refraction, the RL (in m) of station B is _______.

**Solution:**

1. Level the instrument and set up the telescope.
2. Read the angle and calculate the vertical angle (A93°).
3. Apply trigonometry to find the horizontal distance:
$d_2 = 400 \cdot \tan(A7^{\circ})$
4. Calculate the RL of station B using the formula:

$RL_B = RL_A + d_2 \cdot \sin(\text{angle})$

**Q2:** A surveyor observes a zenith angle of A93°00'00'' during a theodolite survey. The corresponding vertical angle is ______.

**Solution:**

1. Use the formula to find the difference between the zenith and vertical angles:
$\Delta = Z - V$
2. Apply trigonometry to solve for the vertical angle:

$V = Z - \Delta$

### Common Pitfalls

* **Incorrect application of trigonometric formulae**
* **Neglecting errors due to curvature of earth and refraction**

### Quick Summary

* **Theodolite Surveying:** measure angles between visible celestial bodies or points on a map
* **Zenith Angle:** angle between direction of an object and vertical plane passing through observer's location
* **Horizontal Distance:** calculate using trigonometry given an angle and one of the sides