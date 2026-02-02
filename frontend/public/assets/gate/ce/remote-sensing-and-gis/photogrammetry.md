**Photogrammetry**
================

**Introduction**
---------------

Photogrammetry is a discipline that deals with the extraction of geometric information from photographs. It is a remote sensing technique used to determine the dimensions, orientation, and position of objects within images or video streams. Photogrammetry has various applications in fields like geospatial analysis, engineering, architecture, and more.

**Core Concepts**
----------------

Photogrammetry involves using multiple overlapping images taken from different angles to reconstruct 3D models of objects or scenes. The fundamental principles are based on the concept that corresponding points between images can be used to estimate the relative positions and orientations of cameras.

### Principle of Correspondence

The principle of correspondence states that if two images are taken at the same location but with a slight change in orientation, certain features will remain consistent across both images.

### Epipolar Geometry

Epipolar geometry is concerned with the study of the relationship between corresponding points on two images. It provides insights into how cameras move relative to each other and their position in space.

**Key Formulas/Theorems**
-------------------------

LaTeX used for math:

$$
\begin{aligned}
E &= mc^2 \\
\end{aligned}
$$

For photogrammetry, the key formulas include:

* **Scale**: The ratio of the distance between corresponding points on a photograph to the actual distance in reality.
* **Ground Sampling Distance (GSD)**: The minimum size of an object that can be resolved in an image.

The formula for calculating scale is given by:

$$
\text{Scale} = \frac{\text{Focal Length}}{\text{Height of Object}}
$$

**Problem Solving Patterns**
---------------------------

1.  **Identify Key Information**: Understand the height and focal length provided to calculate the scale.
2.  **Calculate Scale**: Use the formula to compute the scale based on given values.

**Examples with Solutions**
-------------------------

### Example 1:

Aerial photograph taken from a height of $3.5 \text{ km}$ above mean sea level, using a camera with total length $152 \text{ mm}$. Average ground elevation is $460 \text{ m}$ above mean sea level.

```markdown
## Step 1: Identify Key Information
Height = $3.5 \text{ km}$ (or $3500 \text{ m}$)
Focal Length = $152 \text{ mm}$ (to be converted to meters for consistency)
Average Ground Elevation = $460 \text{ m}$
```

## Step 2: Calculate Scale
Convert focal length from millimeters to meters.
Scale calculation:
$$
\begin{aligned}
\text{Scale} &= \frac{\text{Focal Length (in meters)}}{\text{Height of Object - Average Ground Elevation}} \\
&= \frac{152/1000}{3500 - 460} \\
&= \frac{0.152}{3040} \\
&= 1 : \boxed{20,000}
\end{aligned}
$$

### Answer:

The scale of the photograph is $1 : 20,000$.

**Common Pitfalls**
-------------------

-   **Units**: Ensure to maintain consistent units throughout calculations.
-   **Negative Scale Values**: Pay attention to signs; scale values are positive in most contexts.

**Quick Summary**
------------------

*   Photogrammetry uses images to reconstruct three-dimensional models of objects or scenes.
*   Correspondence principle and epipolar geometry are foundational concepts.
*   Key formulas include scale and ground sampling distance (GSD).
*   Apply problem-solving patterns like identifying key information and performing calculations correctly.

[Image URL: A Wikimedia Commons image illustrating aerial photography principles.](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Aerial_photography_principles.svg/1280px-Aerial_photography_principles.svg.png)

`![Aerial Photography Principles](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Aerial_photography_principles.svg/1280px-Aerial_photography_principles.svg.png)`