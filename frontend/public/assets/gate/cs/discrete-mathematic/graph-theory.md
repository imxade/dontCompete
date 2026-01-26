**Graph Theory**
================

### Introduction
---------------

Graph theory is a branch of discrete mathematics that studies the properties and structures of graphs, which are non-linear data structures consisting of nodes (vertices) connected by edges. Graphs have numerous applications in computer science, engineering, and other fields.

### Core Concepts
-----------------

#### **What is a Graph?**
A graph G = (V, E) consists of:

*   A set of vertices V = {v1, v2, ..., vn}
*   A set of edges E = {(u, v)| u, v ∈ V}

#### **Types of Edges**

*   **Undirected Edge**: an edge without direction (e.g., AB)
*   **Directed Edge** or **Arc**: an edge with a specified direction (e.g., AB→)

### Key Formulas/Theorems
---------------------------

1.  **Handshaking Lemma**:
    $$
    \sum_{v\in V} \deg(v) = 2|E|
    $$

    Where $\deg(v)$ is the degree of vertex v, and |E| is the number of edges.

2.  **Tree Properties**

    *   A tree with n vertices has n - 1 edges.
    *   Every tree with more than one vertex has at least two leaves (vertices with degree 1).

### Problem Solving Patterns
---------------------------

#### **Determining Spanning Trees**
A spanning tree of a graph is a subgraph that includes all the vertices and some edges. We can calculate the number of spanning trees using the following formula:

$$
T = \frac{n^{n-2}}{2}
$$

where n is the number of vertices.

#### **Depth-First Traversal**
A depth-first traversal (DFT) visits a vertex before visiting any of its neighbors. A DFT can be classified into four types: 

*   **Back Edge**: An edge that goes back to an ancestor vertex.
*   **Cross Edge**: An edge that goes to a non-ancestor and non-descendant vertex.
*   **Forward Edge**: An edge that connects a parent vertex with one of its descendants.
*   **Tree Edge**: An edge connecting two adjacent vertices in the traversal tree.

### Examples with Solutions
---------------------------

**Example 1: Determining Spanning Trees**

A complete graph K4 has four vertices (A, B, C, D). Calculate the number of spanning trees.

Solution:

| V | E |
| --- | --- |
| 4 | $\frac{4 \times 3}{2} = 6$ |

$$
T = \frac{n^{n-2}}{2} = \frac{4^{4-2}}{2} = \frac{16}{2} = 8
$$

But in a complete graph, each vertex is connected to every other vertex. Hence:

| V | E |
| --- | --- |
| 4 | $\frac{n(n-1)}{2} = \frac{4(3)}{2} = 6$ |

Since the number of edges remains constant (6), we can apply the formula directly.

$$
T = \frac{n^{n-2}}{2} = \frac{4^{4-2}}{2} = \frac{16}{2} = 8
$$

However, since it's a complete graph, there are multiple spanning trees. We calculate this as follows:

For n vertices, the number of edges in a complete graph is $\frac{n(n-1)}{2}$. Each edge can be either included or excluded from the spanning tree.

Thus, for each edge, we have 2 choices, leading to $2^{\frac{n(n-1)}{2}}$ possible spanning trees. Since there are n vertices, we need to exclude one vertex and its associated edges. This reduces our number of options by a factor of $\frac{n}{n} = 1$, making the total number of spanning trees:

$$
T' = \frac{n^{n-2}}{2} = \frac{4^{4-2}}{2} = \frac{16}{2} = 8
$$

However, since there are multiple spanning trees in a complete graph, we need to account for this by multiplying the result above by $2^{\frac{n(n-1)}{2} - (n-1)}$.

Since $\frac{n(n-1)}{2} - (n-1) = \frac{(n-2)(n+1)}{2}$, and there are n vertices:

$$
T'' = 2^{\frac{(n-2)(n+1)}{2}} \times T' = 16
$$

Hence, the total number of spanning trees in a complete graph with four vertices is indeed $\boxed{16}$.

### Common Pitfalls
-------------------

*   **Oversimplifying** complex concepts.
*   **Not accounting for edge cases** in graphs (e.g., isolated vertices).
*   **Misapplying formulas**, especially when the given graph type doesn't fit perfectly into the formula's assumptions.

### Quick Summary
---------------

| Concept        | Description                                                                                         |
| :------------- | :------------------------------------------------------------------------------------------------- |
| Graph          | A set of vertices connected by edges.                                                                |
| Tree           | A subgraph with all vertices and n - 1 edges (n being the number of vertices).                       |
| Handshaking    | The sum of vertex degrees equals twice the edge count.                                                 |
| Depth-First Traversal | Visits a vertex before visiting any neighbors; can be classified into back, cross, forward, or tree edges.|

Note: This study note has been designed to provide comprehensive coverage of Graph Theory concepts with exam-focused explanations and detailed examples. It should serve as a valuable resource for students aiming to excel in the GATE CS exam, particularly when it comes to graph theory questions like those provided in the source materials.