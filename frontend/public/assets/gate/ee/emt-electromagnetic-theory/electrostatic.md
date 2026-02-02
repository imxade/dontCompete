**Electrostatic Theory**
=======================

**Introduction**
---------------

Electrostatics deals with the study of electric charges and their interactions at rest. It's a fundamental branch of electromagnetism, focusing on phenomena where charges are not in motion. Understanding electrostatics is crucial for comprehending various physical systems and technologies.

**Core Concepts**
-----------------

*   **Electric Charge**: A fundamental property that causes forces between objects. Charges can be either positive or negative.
*   **Coulomb's Law**: Describes the force between two point charges. It states that the magnitude of the electrostatic force between two point charges is directly proportional to the product of their magnitudes and inversely proportional to the square of the distance between them.

    $$ F = \frac{ k \cdot q_1 \cdot q_2 }{ r^2} $$

*   **Electric Field**: A vector field that surrounds charged particles. It's a measure of the electric force per unit charge at any point in space.
*   **Gauss's Law**: States that the total electric flux through a closed surface is proportional to the charge enclosed within that surface.

    $$ \oint_S \vec{E} \cdot d\vec{A} = \frac{ Q_{enclosed} }{ \epsilon_0 } $$

**Key Formulas/Theorems**
-------------------------

*   **Electric Field Intensity**: The electric field intensity at a point due to multiple charges can be calculated using the superposition principle.

    $$ E_{net} = E_1 + E_2 + ... + E_n $$
*   **Potential Difference**: The potential difference between two points is given by:

    $$ V = \int_{A}^{B} \vec{E} \cdot d\vec{l} $$

**Problem Solving Patterns**
---------------------------

### Finding Electric Field Intensity due to Multiple Charges

Given multiple charges and their positions, we can find the net electric field at a point using the superposition principle.

1.  **Calculate Electric Field due to Each Charge**: Use Coulomb's Law or Gauss's Law for each charge.
2.  **Apply Superposition Principle**: Add up all the individual electric fields to get the net electric field.

### Example

Suppose we have three charges: $q_1$, $q_2$, and $q_3$ located at points $A$, $B$, and $C$. We want to find the net electric field at point $P$ due to these charges. The position vectors of the charges are:

*   $ \vec{r_{1}} =  \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix} $
*   $ \vec{r_{2}} =  \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix} $
*   $ \vec{r_{3}} =  \begin{pmatrix} x_3 \\ y_3 \\ z_3 \end{pmatrix} $

We can use the following steps:

1.  Calculate the electric field due to each charge at point P using Coulomb's Law or Gauss's Law.
2.  Add up all the individual electric fields to get the net electric field.

### Example Solution

Suppose we have three charges: $q_1 = 2 \mu C$, $q_2 = -3 \mu C$, and $q_3 = 4 \mu C$. The position vectors of the charges are:

*   $ \vec{r_{1}} =  \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} $
*   $ \vec{r_{2}} =  \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix} $
*   $ \vec{r_{3}} =  \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} $

We want to find the net electric field at point P located at $(x, y, z) = (0.5, 0, 0)$ due to these charges.

Using Coulomb's Law or Gauss's Law, we can calculate the electric field due to each charge at point P:

$$ E_1 = \frac{ k \cdot q_1 }{ r_{1P}^2} $$
$$ E_2 = \frac{ k \cdot q_2 }{ r_{2P}^2} $$
$$ E_3 = \frac{ k \cdot q_3 }{ r_{3P}^2} $$

Adding up all the individual electric fields, we get:

$$ E_{net} = E_1 + E_2 + E_3 $$