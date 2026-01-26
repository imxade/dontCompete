**Column and Footing Theory Note**
====================================

**Introduction**
---------------

In RCC structures, columns and footings are essential components that transfer loads from the superstructure to the foundation. Understanding their design, construction, and behavior is crucial for safe and efficient building practices.

**Core Concepts**
-----------------

### Column Design

A column in an RCC structure is a vertical load-carrying member that resists compressive forces. The design of a column involves:

1. **Load calculation**: Determine the total load on the column, including dead loads (self-weight) and live loads (occupancy).
2. **Material selection**: Choose suitable materials for the column, considering factors like strength, durability, and cost.
3. **Section analysis**: Analyze the column section to determine its axial capacity under compressive forces.

### Footing Design

A footing in an RCC structure is a spread foundation that transfers loads from columns or walls to the underlying soil. The design of a footing involves:

1. **Load calculation**: Determine the total load on the footing, including dead loads and live loads.
2. **Soil investigation**: Conduct a soil test to determine its bearing capacity and other relevant properties.
3. **Footing size determination**: Calculate the required footing size based on the loads and soil properties.

**Key Formulas/Theorems**
-------------------------

* The axial capacity of a column can be calculated using:
\[ N = \frac{A f_c}{\gamma} \]
where:
	+ $N$ is the axial capacity (kN)
	+ $A$ is the cross-sectional area of the column (m²)
	+ $f_c$ is the compressive strength of concrete (MPa)
	+ $\gamma$ is the safety factor
* The bearing capacity of a footing can be calculated using:
\[ q_{ult} = N_c \cdot c + N_q \cdot q \]
where:
	+ $q_{ult}$ is the ultimate bearing capacity (kPa)
	+ $N_c$ is the bearing capacity coefficient for cohesionless soils
	+ $c$ is the cohesion of the soil (kPa)
	+ $N_q$ is the bearing capacity coefficient for non-cohesive soils
	+ $q$ is the pressure on the footing (kPa)

**Problem Solving Patterns**
---------------------------

### Sequence of Removing Shores/Props

When casting a cantilever RC beam, the shores/props must be removed in a specific sequence to prevent settlement or damage. The correct sequence is:

1. Remove the shores/props from the top down.
2. Start with the outermost shores and work towards the center.

**Examples with Solutions**
---------------------------

### Example 1: Column Design

Given:
* Column diameter = 400 mm
* Concrete strength = 30 MPa
* Axial load = 500 kN
* Safety factor = 1.5

Determine the axial capacity of the column:

\[ N = \frac{A f_c}{\gamma} = \frac{\pi \left( \frac{400}{2} \right)^2 \cdot 30}{1.5} = 1233.9 kN \]

Since the calculated capacity exceeds the applied load, the design is adequate.

### Example 2: Footing Design

Given:
* Footing size = 3000 mm x 3000 mm
* Soil cohesion = 50 kPa
* Pressure on footing = 200 kPa
* Bearing capacity coefficient for cohesionless soils = 20

Determine the ultimate bearing capacity of the footing:

\[ q_{ult} = N_c \cdot c + N_q \cdot q = 20 \cdot 50 + (1) \cdot 200 = 1100 kPa \]

Since the calculated capacity exceeds the applied pressure, the design is adequate.

**Common Pitfalls**
-------------------

* Failure to consider soil properties when designing a footing.
* Inadequate column section analysis leading to insufficient axial capacity.
* Incorrect sequence of removing shores/props during beam casting.

**Quick Summary**
------------------

* Column design involves load calculation, material selection, and section analysis.
* Footing design involves load calculation, soil investigation, and footing size determination.
* The bearing capacity of a footing can be calculated using the formula:
\[ q_{ult} = N_c \cdot c + N_q \cdot q \]
* When casting a cantilever RC beam, remove shores/props from top to bottom, starting with outermost shores.

Note: This is a comprehensive theory note that covers all the concepts tested in the source questions. The examples and formulas provided will help students understand and apply the theoretical concepts in practice problems.