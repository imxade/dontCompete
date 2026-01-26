**Graph Theory**
================

### Introduction
-----------------

Graph theory is a branch of mathematics that studies graphs as discrete structures consisting of vertices (also called nodes or points) connected by edges. It has numerous applications in computer science, particularly in data structures and algorithms.

### Core Concepts
------------------

#### Graph Definition
A graph $G$ is defined as an ordered pair $(V, E)$ where:

*   $V$ is a set of vertices (nodes)
*   $E \subseteq V \times V$ is the set of edges between pairs of vertices

#### Types of Graphs
There are several types of graphs, including:

*   **Simple graph**: A graph with no multiple edges or loops.
*   **Multigraph**: A graph that allows multiple edges between a pair of vertices.
*   **Weighted graph**: A graph where each edge has a weight (label) associated with it.

#### Graph Operations
Some important operations on graphs include:

*   **Union**: The union of two graphs $G_1$ and $G_2$, denoted by $G_1 \cup G_2$, is the graph whose vertex set is the union of the vertex sets of $G_1$ and $G_2$, and whose edge set consists of all edges from both graphs.
*   **Intersection**: The intersection of two graphs $G_1$ and $G_2$, denoted by $G_1 \cap G_2$, is the graph whose vertex set is the intersection of the vertex sets of $G_1$ and $G_2$, and whose edge set consists only of those edges common to both graphs.
*   **Complement**: The complement of a graph $G$, denoted by $\overline{G}$, is the graph with the same vertices as $G$, but with an edge between two vertices if and only if there is no edge between them in $G$.

### Key Formulas/Theorems
----------------------------

#### Chromatic Number
The chromatic number of a graph $G$, denoted by $\chi(G)$, is the minimum number of colors needed to color all vertices such that no two adjacent vertices have the same color.

*   **Brooks' Theorem**: For any connected graph $G$ without triangles (i.e., no vertex with three edges), if $\Delta(G) = \deg(v)$ for some vertex $v$, then $\chi(G) = \Delta(G)$.
*   **Color-Critical Graphs**: A graph $G$ is color-critical if $\chi(G - e) < \chi(G)$ for any edge $e$. Color-critical graphs are used to study the chromatic number of a graph.

#### Edge Counting
The following formulas count the edges in a graph:

*   **Handshaking Lemma**: If $G$ is an undirected graph with vertex degrees $d_1, d_2, ..., d_n$, then the sum of all degrees equals twice the number of edges: $$\sum_{i=1}^{n} d_i = 2|E(G)|$$
*   **Tutte's Formula**: If $G$ is an undirected graph with vertex degrees $d_1, d_2, ..., d_n$, then the number of edges can be computed using the following formula: $$|E(G)| = \frac{1}{2} \left(\sum_{i=1}^{n} d_i - \sum_{i<j} |d_i - d_j|\right)$$

### Problem Solving Patterns
------------------------------

When solving graph-related problems, follow these patterns:

*   **Use the given information wisely**: Understand what is being asked and use the provided information to determine the solution.
*   **Draw a diagram or visualize the problem**: Graphs can be complex, so drawing a diagram or visualizing the problem can help clarify relationships between vertices and edges.

### Examples with Solutions
---------------------------

**Example 1:** Find the chromatic number of a graph with five vertices, where three of them have degree two and two have degree one.

*   **Step 1:** Draw the graph.
*   **Step 2:** Identify independent sets to use for coloring. In this case, we can create an independent set with all vertices, since none of them are adjacent.
*   **Step 3:** Apply Vizing's theorem: $$\Delta(G) \leq \chi'(G) \leq \Delta(G) + 1$$

Since $\Delta(G) = 2$, the chromatic number $\chi'(G)$ must be either $2$ or $3$. We have two vertices with degree one, so we can assign these two colors. The remaining three vertices will need at least one more color.

Therefore, the chromatic number of this graph is $\boxed{3}$.

**Example 2:** Find the edge count for a complete bipartite graph $K_{m,n}$ where m=4 and n=5.

*   **Step 1:** Understand that in a complete bipartite graph, each vertex on one side has an edge to every other vertex on the other side.
*   **Step 2:** Calculate the total number of edges using the formula: $|E(K_{m,n})| = mn$
*   **Answer:** $4 \times 5 = 20$ edges

### Common Pitfalls
--------------------

When working with graphs, avoid these common pitfalls:

*   **Miscounting edges**: Double-check your calculations when determining edge counts.
*   **Incorrect application of formulas**: Understand the underlying principles behind each formula before applying it.

### Quick Summary
-------------------

Graph theory is crucial in computer science, particularly in data structures and algorithms. Key concepts include graph definition, types of graphs, operations on graphs, chromatic number, Brooks' theorem, edge counting (Handshaking Lemma and Tutte's Formula), problem-solving patterns, examples with solutions, and common pitfalls to avoid.

**References:**

*   **Graph Theory** by Harary et al. (1965)
*   **The Handbook of Graph Theory** edited by Jonathan L. Gross (2004)