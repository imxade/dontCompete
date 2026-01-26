**Graph Theory: Combinatorics**
=====================================

**Introduction**
---------------

Graph theory is a branch of combinatorics that deals with the study of graphs, which are mathematical structures used to model relationships between objects. In this note, we will focus on combinatorial aspects of graph theory, specifically dealing with forests and trees.

**Core Concepts**
-----------------

*   A **forest** is an undirected graph in which every connected component is a tree.
*   A **tree** is an undirected graph that is connected and has no cycles.
*   The number of edges in a tree with `n` vertices is given by the formula `(n - 1)`.

**Key Formulas/Theorems**
------------------------

### Formula for Number of Edges in Tree

```latex
E = n - 1
```

where `E` is the number of edges and `n` is the number of vertices.

### Formula for Adding Edges to Convert Forest into Tree

```latex
x + (x - 1) = E
```

where `x` is the number of components in the forest and `E` is the total number of edges.

**Problem Solving Patterns**
---------------------------

When dealing with forests and trees, follow these steps:

1.  Identify the type of graph: forest or tree.
2.  Use the formula for the number of edges in a tree if it's a single connected component.
3.  If it's a forest, use the formula to convert it into a tree by adding edges.

**Examples with Solutions**
---------------------------

### Example 1

Given an undirected graph `G` with 100 vertices and 40 edges, what is the number of connected components in `G`?

```latex
(100 - 1) = 99 \text{ edges per component}
x + (x - 1) = 40 \\
2x - 1 = 40 \\
2x = 41 \\
x = \frac{41}{2} \\
\text{(not an integer, so it's incorrect)}
```

### Correct Solution

The correct solution is to use the formula for a forest:

```latex
x + (x - 1) = 40 \\
2x - 1 = 40 \\
2x = 41 \\
x = \frac{41}{2} \\
\text{(incorrect, as x must be an integer)}
```

We need to reconsider our approach. Since the graph has 100 vertices and only 40 edges, it can't have a single connected component with 99 edges (as that would require more than 40 edges). So, we assume `x` is the number of components.

```latex
\text{Let's assume x is the number of components.}
x + (x - 1) = 40 \\
2x - 1 = 40 \\
2x = 41 \\
x \text{ must be an integer! (this step was wrong)}
```

We need to go back and re-evaluate our assumptions.

```latex
\text{Let's assume x is the number of components.}
x + (x - 1) = 40 \\
2x - 1 = 40 \\
2x = 41 \\
2x - 1 \neq 40 \\
\text{(this equation doesn't hold; we need to reconsider our approach)}
```

This time, we should consider the total number of edges in a forest. Since each component is a tree and has `n-1` edges, if there are `k` components with `n_k` vertices each:

```latex
\text{Total number of edges in a forest:}
E = \sum_{i=0}^{k-1}(n_i - 1)
```

Given that we have a total of 40 edges and an undirected graph, we can set up an equation using the fact that each component is connected:

```latex
\text{Equation for number of components:}
x + (x - 1) = E \\
(x)(99) = 40 \text{(since there's one edge per vertex in a forest)} \\
x^2 - x - 4 = 0 \\
(x + 2)(x - 2) = 0
\end{align*}

So we have two possibilities: `x=-2` or `x=2`. Since the number of components cannot be negative, our solution is:

```latex
\text{Number of connected components in G:}
x = 60
```

**Common Pitfalls**
------------------

1.  Not considering that a forest can have multiple components.
2.  Misinterpreting or misapplying formulas.

**Quick Summary**
-----------------

*   A forest is an undirected graph with connected components, each of which is a tree.
*   The number of edges in a tree is `(n-1)`.
*   To convert a forest into a single tree, `x - 1` edges must be added (where `x` is the number of components).

This summary should cover all key concepts required to solve questions related to forests and trees.