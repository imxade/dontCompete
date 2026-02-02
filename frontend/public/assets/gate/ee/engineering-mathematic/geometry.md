**Geometry Theory Note**
=========================

**Introduction**
---------------

Geometry is a branch of mathematics that deals with the study of shapes, sizes, positions, and dimensions of objects. In engineering mathematics, geometry plays a crucial role in solving problems related to circuits, electronics, and electrical engineering.

**Core Concepts**
-----------------

### Intersection of Circles

When two circles intersect orthogonally at a point, their tangents are perpendicular to each other.

### Perpendicular Distance

The perpendicular distance from the center of one circle to the circumference of another is equal to the radius of the smaller circle minus the radius of the larger circle.

**Key Formulas/Theorems**
-------------------------

LaTeX
: 
$$d = r_1 - r_2$$

where $d$ is the perpendicular distance, $r_1$ is the radius of the larger circle, and $r_2$ is the radius of the smaller circle.

### Circle Equation

The general equation of a circle with center $(h,k)$ and radius $r$ is given by:

LaTeX
: 
$$(x-h)^2 + (y-k)^2 = r^2$$

**Problem Solving Patterns**
---------------------------

1.  When dealing with intersecting circles, first identify the point of intersection.
2.  Use the properties of tangents and perpendicular lines to solve for unknowns.

**Examples with Solutions**
-------------------------

### Example 1

Suppose two circles intersect orthogonally at the point $(u,v)$. The equation of the first circle is $x^2+y^2=4$, and the equation of the second circle is $(x-2)^2+(y+1)^2=9$. Find $uv$.

LaTeX
: 
$$\begin{aligned}
x^2+y^2 &= 4 \\
(x-2)^2+(y+1)^2 &= 9
\end{aligned}$$

Subtracting the first equation from the second, we get:

LaTeX
: 
$$\begin{aligned}
(2-2)(x)+(-1+1)y+4-4 &= (0+2^2)+(0+1^2)-9 \\
0x + 0y - 0 &= 4-9 \\
-5 &= -5
\end{aligned}$$

Now, to find $uv$, we need the values of $u$ and $v$. Using the equations of the circles:

LaTeX
: 
$$\begin{aligned}
(u+2)^2+(v+1)^2 &= 9 \\
u^2+v^2 &= 4
\end{aligned}$$

Subtracting the second equation from the first, we get:

LaTeX
: 
$$(2u+2)(x)+(v+1)y-0=5.$$
Substitute $(u,v)$ into this expression to find $uv$: 
$$(2u+2)^2+(v+1)^2=9$$

Solving for $u$ and $v$, we get:

LaTeX
: 
$$\begin{aligned}
(2u+2)^2+(v+1)^2 &= 9 \\
4(u^2+1)+4uv+4(v^2+1) &= 9 \\
4u^2+8u+8+4v^2+4v+1 &= 9 \\
4(u^2+v^2)+(8u+4v+5) &= -1
\end{aligned}$$

Since the circles intersect orthogonally, we can write:

LaTeX
: 
$$(u-0)^2+(v-0)^2 = (2)^2 + (-1)^2 \implies u^2+v^2=4+1.$$

Substitute this into the previous equation to get:

LaTeX
: 
$$16+8u+4v+5=-1\implies 8u+4v=-22.$$
Now, substitute $u=v-0$ into this expression and solve for $uv$: 

LaTeX
: $$ \begin{aligned}
8(v-0)+4v & = -22 \\
8v + 4v &= -22\\
12v&= -22\implies v=-22/12.
\end{aligned}$$

Now, substitute this expression for $v$ into the original equation of the second circle to solve for $u$: 

LaTeX
: $$ \begin{aligned}
(x-2)^2+(y+1)^2 &= 9\\
(u^2+v^2) & =4 \\
u^2 + v^2 &= 4 \\
u^2 + (-22/12)^2&=4\implies u^2 = (64-484)/144= -420 /144 \implies u=\pm i \sqrt{35}
\end{aligned}$$

Substitute $(u,v)=(i\sqrt{35},-11/6)$ into the expression for $uv$:

LaTeX
: 
$$\begin{aligned}
u v &= (i\sqrt{35}) (-11/6) \\
&= -11i\sqrt{35}/6.
\end{aligned}$$

However, there is no real solution.

The equation of a circle with center at $(h,k)$ and radius $r$ can be represented by the following diagram in Mermaid format: 
```mermaid
graph LR
    A[(0,0)] --> B[Circle]
```

**Common Pitfalls**
-------------------

1.  When solving problems involving intersecting circles, make sure to identify the point of intersection correctly.
2.  Use the properties of tangents and perpendicular lines to solve for unknowns.

**Quick Summary**
------------------

*   Circle equation: $(x-h)^2 + (y-k)^2 = r^2$
*   Intersection of circles: When two circles intersect orthogonally, their tangents are perpendicular.
*   Perpendicular distance: $d=r_1 - r_2$

This comprehensive theory note covers all the key concepts and formulas required to solve geometry-related problems in the GATE exam. The examples provided demonstrate how to apply these concepts to real-world problems.