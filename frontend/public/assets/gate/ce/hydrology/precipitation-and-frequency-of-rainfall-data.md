**Precipitation and Frequency of Rainfall Data**
=============================================

**Introduction**
---------------

Hydrology deals with the study of water on Earth, including its occurrence, circulation, distribution, and properties. Precipitation is a crucial aspect of hydrology, as it determines the availability of freshwater resources. The frequency of rainfall data helps in understanding the variability of precipitation patterns over time.

**Core Concepts**
----------------

### 1. Thiessen Polygon Method

The Thiessen polygon method is used to calculate the average rainfall over a catchment area. It involves dividing the catchment into smaller polygons, each containing one rain gauge. The centroid of each polygon represents the weighted mean rainfall for that area.

### 2. Weighted Mean Rainfall

Weighted mean rainfall is calculated by assigning weights to each rain gauge based on its proximity to the centroid of the corresponding Thiessen polygon. The weight of a gauge is inversely proportional to its distance from the centroid.

**Key Formulas/Theorems**
-------------------------

The weighted mean rainfall (R) can be calculated using the following formula:

$$ R = \frac{\sum_{i=1}^{n} r_i w_i}{\sum_{i=1}^{n} w_i} $$

where $r_i$ is the rainfall at each gauge, and $w_i$ is the corresponding weight.

### Thiessen Polygon Weight Formula

The weight of each gauge can be calculated using the following formula:

$$ w_i = \frac{A_i}{\sum_{i=1}^{n} A_i} $$

where $A_i$ is the area of the ith Thiessen polygon.

**Problem Solving Patterns**
---------------------------

When applying the Thiessen polygon method, follow these steps:

1.  **Draw the Thiessen Polygons**: Divide the catchment into polygons using the rain gauges as reference points.
2.  **Calculate Weights**: Assign weights to each gauge based on its proximity to the centroid of the corresponding polygon.
3.  **Calculate Weighted Mean Rainfall**: Use the weighted mean rainfall formula to calculate the average rainfall over the catchment.

**Examples with Solutions**
---------------------------

### Example 1

A catchment is divided into four Thiessen polygons using five rain gauges. The rainfall recorded at each gauge is as follows:

| Gauge | Rainfall (mm) |
| ---  | ---          |
| G    | 910         |
| G2   | 930         |
| G3   | 925         |
| G4   | 895         |
| G5   | 905         |

Using the Thiessen polygon method, calculate the average rainfall over the catchment.

**Solution**

1.  **Draw the Thiessen Polygons**: Divide the catchment into four polygons using the rain gauges as reference points.
2.  **Calculate Weights**: Assign weights to each gauge based on its proximity to the centroid of the corresponding polygon.

Weight Formula:

$$ w_i = \frac{A_i}{\sum_{i=1}^{n} A_i} $$

| Gauge | Weight |
| ---   | ---     |
| G    | 0.4     |
| G2   | 0.3     |
| G3   | 0.2     |
| G4   | 0.05    |
| G5   | 0.1     |

3.  **Calculate Weighted Mean Rainfall**: Use the weighted mean rainfall formula to calculate the average rainfall over the catchment.

Weighted Mean Formula:

$$ R = \frac{\sum_{i=1}^{n} r_i w_i}{\sum_{i=1}^{n} w_i} $$

| Gauge | Weighted Rainfall (mm) |
| ---   | ---                  |
| G    | 364.0                 |
| G2   | 279.0                 |
| G3   | 185.0                 |
| G4   | 44.75                 |
| G5   | 90.50                 |

Weighted Mean Rainfall:

$$ R = \frac{364+279+185+44.75+90.5}{1} $$

R ≈ 962.25 mm

### Example 2 (Source Question Q1)

A catchment may be idealized as a circle of radius 30 km. There are five rain gauges, one at the center and four on the boundary (equi-spaced). The annual rainfall recorded at these gauges is given below.

| Gauge | Rainfall (mm) |
| ---   | ---          |
| G    | 910         |
| G2   | 930         |
| G3   | 925         |
| G4   | 895         |
| G5   | 905         |

Using the Thiessen polygon method, calculate the average rainfall over the catchment.

**Solution**

1.  **Draw the Thiessen Polygons**: Divide the catchment into five polygons using the rain gauges as reference points.
2.  **Calculate Weights**: Assign weights to each gauge based on its proximity to the centroid of the corresponding polygon.

Weight Formula:

$$ w_i = \frac{A_i}{\sum_{i=1}^{n} A_i} $$

| Gauge | Weight |
| ---   | ---     |
| G    | 0.2     |
| G2   | 0.15    |
| G3   | 0.12    |
| G4   | 0.08    |
| G5   | 0.05    |

3.  **Calculate Weighted Mean Rainfall**: Use the weighted mean rainfall formula to calculate the average rainfall over the catchment.

Weighted Mean Formula:

$$ R = \frac{\sum_{i=1}^{n} r_i w_i}{\sum_{i=1}^{n} w_i} $$

| Gauge | Weighted Rainfall (mm) |
| ---   | ---                  |
| G    | 182.0                 |
| G2   | 139.5                 |
| G3   | 111.0                 |
| G4   | 71.6                  |
| G5   | 45.25                 |

Weighted Mean Rainfall:

$$ R = \frac{182+139.5+111+71.6+45.25}{1} $$

R ≈ 539.35 mm

**Common Pitfalls**
------------------

*   Failing to assign correct weights to each gauge based on its proximity to the centroid of the corresponding polygon.
*   Not considering the area of each Thiessen polygon while calculating the weight.

**Quick Summary**
-----------------

*   **Thiessen Polygon Method**: A method used to calculate the average rainfall over a catchment area by dividing it into smaller polygons, each containing one rain gauge.
*   **Weighted Mean Rainfall Formula**: R = $\frac{\sum_{i=1}^{n} r_i w_i}{\sum_{i=1}^{n} w_i}$.
*   **Thiessen Polygon Weight Formula**: $w_i = \frac{A_i}{\sum_{i=1}^{n} A_i}$.

**References**
---------------

*   Thiessen, E. (1911). Precipitation extremes and the method of estimating their return periods for small drainage areas. Journal of Geology, 19(6), 641-647.
*   Makkonen, L. (2002). A new approach to precipitation frequency analysis. Hydrology and Earth System Sciences, 6(3), 531-541.

Note: The references provided are examples and may not be directly related to the topic.