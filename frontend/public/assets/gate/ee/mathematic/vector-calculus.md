**Vector Calculus Theory Note**
=====================================

**Introduction**
---------------

Vector calculus is a branch of mathematics that deals with the differentiation and integration of vector fields. It provides a powerful tool for solving problems involving rates of change, accumulation, and maxima/minima in multivariable spaces.

### Core Concepts

* **Gradient**: A vector field $\nabla f(x,y,z)$ representing the rate of change of the scalar function $f(x,y,z)$ at each point.
* **Divergence**: A scalar field $\nabla \cdot \mathbf{F}(x,y,z)$ representing the net flow of the vector field $\mathbf{F}$ out of a small region around a point.
* **Curl**: A vector field $\nabla \times \mathbf{F}(x,y,z)$ representing the rotation or circulation of the vector field $\mathbf{F}$ at each point.

### Key Formulas/Theorems

$\boxed{\nabla f(x,y,z) = \frac{\partial f}{\partial x} \mathbf{i} + \frac{\partial f}{\partial y} \mathbf{j} + \frac{\partial f}{\partial z} \mathbf{k}}$

$\boxed{\nabla \cdot \mathbf{F}(x,y,z) = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}}$

$\boxed{\nabla \times \mathbf{F}(x,y,z) = \begin{vmatrix}\mathbf{i} & \mathbf{j} & \mathbf{k}\\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z}\\ F_x & F_y & F_z\end{vmatrix}}$

### Problem Solving Patterns

* **Directional Derivative**: Find the directional derivative of a scalar function $f(x,y,z)$ at point $(x_0, y_0, z_0)$ in the direction of vector $\mathbf{u}$ using the formula: $D_{\mathbf{u}} f(x_0, y_0, z_0) = \nabla f(x_0, y_0, z_0) \cdot \frac{\mathbf{u}}{\|\mathbf{u}\|}$.
* **Gradient and Divergence**: Use the gradient and divergence operators to solve problems involving maxima/minima, accumulation, and rates of change.

### Examples with Solutions

**Example 1**

Find the directional derivative of $f(x,y,z) = xy + yz$ at point $(1,1,1)$ in the direction of $\mathbf{u} = \begin{pmatrix} 2 \\ -3 \\ 4 \end{pmatrix}$.

Solution:

$\nabla f(x,y,z) = \frac{\partial}{\partial x}(xy + yz)\mathbf{i} + \frac{\partial}{\partial y}(xy + yz)\mathbf{j} + \frac{\partial}{\partial z}(xy + yz)\mathbf{k}$

$= y\mathbf{i} + (x+z)\mathbf{j} - xy\mathbf{k}$

$\nabla f(1,1,1) = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$

$\frac{\mathbf{u}}{\|\mathbf{u}\|} = \frac{1}{\sqrt{29}} \begin{pmatrix} 2 \\ -3 \\ 4 \end{pmatrix}$

$D_{\mathbf{u}} f(1,1,1) = \nabla f(1,1,1) \cdot \frac{\mathbf{u}}{\|\mathbf{u}\|} = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \cdot \frac{1}{\sqrt{29}} \begin{pmatrix} 2 \\ -3 \\ 4 \end{pmatrix}$

$= \frac{-1}{\sqrt{29}}$

**Common Pitfalls**

* Forgetting to apply the correct formula or operator.
* Not checking units and dimensions.

### Quick Summary
--------------------------------------

* Gradient, Divergence, Curl are essential operators in vector calculus.
* Directional derivative can be found using the dot product of the gradient and the unit vector in the direction of $\mathbf{u}$.

Note: This is a basic theory note and may not cover all aspects of Vector Calculus. For more detailed information, refer to standard textbooks or online resources.