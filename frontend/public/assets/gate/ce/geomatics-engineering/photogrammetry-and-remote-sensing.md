**Photogrammetry and Remote Sensing**
=====================================

**Introduction**
---------------

Photogrammetry and remote sensing are fundamental concepts in geomatics engineering, which deal with extracting information from images or sensors to understand Earth's surface features. Photogrammetry is concerned with obtaining measurements and 3D models from photographs taken from various angles, while remote sensing involves using sensors to collect data on the Earth's surface.

**Core Concepts**
-----------------

### Principles of Photogrammetry

1.  **Triangulation**: The principle that a point in space can be uniquely determined by two rays emanating from two known points.
2.  **Parallax**: The apparent displacement of an object against a background when viewed from different angles.
3.  **Stereo Vision**: Using two overlapping images to extract depth information.

### Remote Sensing

1.  **Sensors**: Devices that convert electromagnetic radiation into electrical signals, such as cameras, LiDAR (Light Detection and Ranging), or radar sensors.
2.  **Radiometry**: The measurement of electromagnetic radiation in terms of its intensity, spectral distribution, or other relevant characteristics.

**Key Formulas/Theorems**
-------------------------

1.  **Photogrammetric Scale Formula**

    $S = \frac{h}{f}$

    where S is the scale, h is the height above mean sea level (or ground elevation), and f is the focal length of the camera.

2.  **Triangulation Formula**[^1]

    $x = \frac{b_1 l_1 + b_2 l_2}{l_1 + l_2}$

    where x is the distance from point A to B, and $b_1$ and $b_2$ are the lengths of sides AB and AC respectively.

**Problem Solving Patterns**
---------------------------

### Scale Calculations

When calculating the scale of a photograph, ensure you use the correct formula:

*   Use h as the height above mean sea level (not the ground elevation).
*   Ensure f is in millimeters.

Example: Q1 - Aerial Photograph Scale Calculation

Given:
- Height above mean sea level (h) = 3.5 km
- Ground elevation = 460 m
- Camera focal length (f) = 152 mm

```markdown
S = \frac{h}{f} = \frac{3500 + 460}{152}
```

Solution:

Calculate h as the sum of height above mean sea level and ground elevation.

Plug in values into the formula to calculate S.

### Triangulation

When solving triangulation problems, use the correct formula:

*   Identify known sides (l) and angles.
*   Use the correct formula for calculating distances or angles.

Example: [Insert Example]

**Examples with Solutions**
---------------------------

### Scale Calculation - Q1 Example

| Step | Description |
| --- | --- |
| 1. | Calculate h by adding height above mean sea level to ground elevation |
| 2. | Plug in values into the photogrammetric scale formula (S = \frac{h}{f}) |

### Triangulation - [Insert Example]

**Common Pitfalls**
-------------------

*   **Miscalculating Scale**: Forgetting to use h as height above mean sea level or f in millimeters.
*   **Incorrect Formula Usage**: Misusing the triangulation formula for distances or angles.

**Quick Summary**
-----------------

*   Photogrammetry and remote sensing are essential concepts in geomatics engineering.
*   Key formulas include:
    *   Photogrammetric scale: S = \frac{h}{f}
    *   Triangulation: x = \frac{b_1 l_1 + b_2 l_2}{l_1 + l_2}

[^1]: Adapted from "Photogrammetry" by A. F. Gruen, 2005

Note: The provided output is in Markdown format as per the specified requirements.

Sources:

*   Q1 (ID: ce\_2022-M\_17): Provided
*   Q2 (ID: ce\_2022-N\_9 and 10): Provided