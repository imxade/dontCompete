**Routing Protocols: Shortest Path Flooding Distance Vector and Link State Routing**
===========================================================

### Introduction
Routing protocols are essential for forwarding packets between networks. Two primary types of routing protocols are distance vector (DV) and link state (LS). We will explore how they work, their strengths, and weaknesses.

### Core Concepts
#### Distance Vector Routing
Distance vector routing protocols exchange routing information with neighboring routers using a vector that represents the minimum distance to reach each destination network.

**Key Properties**

*   **Routing Table**: Each router maintains a table with network IDs as keys and the minimum distance to reach those networks as values.
*   **Update Frequency**: Routers typically send periodic updates (e.g., every 30 seconds) containing their current routing table.
*   **Vector Exchange**: Upon receiving an update, each router adds its own cost to reach the destination network to the received vector.

#### Link State Routing
Link state routing protocols collect and share information about all links within a network. Each router maintains a map of the entire network topology.

**Key Properties**

*   **Topology Map**: Routers build and maintain a graph representing the network's connectivity.
*   **Update Frequency**: Similar to DV, LS routers send periodic updates (e.g., every 60 seconds) describing changes in their local view of the network.
*   **Neighbor Information**: Each router shares information about its directly connected neighbors.

### Key Formulas/Theorems
#### Distance Vector Routing
For a distance vector protocol with a hop count metric, the shortest path can be found using Dijkstra's algorithm.

$$d_{ij} = \min\limits_k d_i + c_{ik}$$

where:
*   $d_{ij}$ is the minimum distance from router $i$ to network $j$
*   $d_i$ is the current distance to reach network $i$
*   $c_{ik}$ is the cost of reaching router $k$ from router $i$

#### Link State Routing
Link state routing uses Dijkstra's algorithm as well, but with a focus on link weights (costs) instead of hop counts.

$$d_{ij} = \min\limits_k d_i + c_{ij}$$

where:
*   $c_{ij}$ is the cost associated with the link between routers $i$ and $j$

### Problem Solving Patterns
When analyzing questions involving routing protocols, remember:

1.  **Identify the type of protocol** (DV or LS) used in the network.
2.  **Understand how updates are propagated** and which information is exchanged.
3.  **Focus on the specific scenario**, such as link failures or changes in network topology.

### Examples with Solutions
Consider a simple network with two routers, $A$ and $B$. Both use DV with a hop count metric.

1.  What is the shortest path from $A$ to $C$ if $AB = 2$ and $BC = 3$?
    *   Using Dijkstra's algorithm:
        *   $d_{AC} = \min(d_A + AB, d_B + BC) = \min(0+2, \infty+3) = 2$
2.  Suppose link $AB$ fails in the previous network. What is the new shortest path from $A$ to $C$?
    *   After convergence:
        *   $d_{AC} = d_A + AD = 1$

### Common Pitfalls
*   Don't confuse DV and LS protocols; know their key differences.
*   When analyzing updates, pay attention to the specific information exchanged (e.g., routing tables vs. link states).
*   Focus on the scenario details to avoid overcomplicating the problem.

### Quick Summary

*   **Distance Vector Routing**:
    *   Exchanges routing table information with neighbors
    *   Uses Dijkstra's algorithm for shortest paths
*   **Link State Routing**:
    *   Shares link state information with all routers
    *   Also uses Dijkstra's algorithm but focuses on link weights