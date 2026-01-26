**Network Layer**
================

### Introduction
----------------

The Network Layer is responsible for routing data between different networks using logical addresses. It ensures that data reaches its destination by selecting the best path and handling packet forwarding, fragmentation, and reassembly.

### Core Concepts
-----------------

#### Subnetting and CIDR Notation
--------------------------------

Subnetting involves dividing a network into smaller sub-networks to conserve IP addresses and improve routing efficiency. Classless Inter-Domain Routing (CIDR) notation is used to represent subnet masks in the form `IP address/Prefix length`.

#### Routing Tables
-------------------

A routing table is a data structure that stores routes to destinations on the internet. It contains information such as next-hop routers, interface addresses, and metrics.

### Key Formulas/Theorems
-------------------------

#### Subnet Mask Calculation
--------------------------------

Given an IP address `IP` and prefix length `n`, the subnet mask can be calculated using:

$$\text{Subnet Mask} = \text{Default Subnet Mask} \land (2^{32-n}-1)$$

where $\land$ represents bitwise AND.

#### Fragmentation
-------------------

When a packet exceeds the Maximum Transmission Unit (MTU) of an interface, it must be fragmented. The maximum fragment size is determined by:

$$\text{Max Fragment Size} = \min(\text{MTU}, 536)$$

### Problem Solving Patterns
-----------------------------

#### Route Aggregation
---------------------

When multiple routes have the same next-hop router and metric, they can be aggregated into a single route.

*   **Pattern**: Multiple routes with the same next-hop router and metric.
*   **Solution**: Select the route with the longest prefix length (most specific).

#### NAT and IP Header Modification
-----------------------------------

Network Address Translation (NAT) modifies the source IP address of packets leaving an internal network. The destination IP address remains unchanged.

*   **Pattern**: Packet leaving an internal network via a NAT device.
*   **Solution**: Modify the source IP address to match the NAT mapping.

### Examples with Solutions
---------------------------

#### Example 1: Route Aggregation

Given:

| Subnet | Mask | Next-Hop |
| --- | --- | --- |
| 12.20.168.0 | 255.255.254.0 | R1 |
| 12.20.166.0 | 255.255.254.0 | R1 |
| ... | ... | ... |

Aggregate the routes to find the aggregated subnet and mask.

*   **Solution**: Select the route with the longest prefix length (most specific). In this case, it is `12.20.168.0/20`.

#### Example 2: NAT and IP Header Modification

Given a packet leaving an internal network via a NAT device:

| Source IP | Destination IP |
| --- | --- |
| 192.168.1.100 | 8.8.8.8 |

NAT modifies the source IP address to match the NAT mapping.

*   **Solution**: Modify the source IP address to `10.0.0.1` (assuming a valid NAT mapping).

### Common Pitfalls
-------------------

*   Failing to recognize route aggregation opportunities.
*   Incorrectly modifying destination IP addresses during NAT.
*   Overlooking packet fragmentation requirements.

### Quick Summary
----------------

*   Understand subnetting and CIDR notation.
*   Familiarize yourself with routing tables and metrics.
*   Recognize route aggregation patterns.
*   Apply NAT rules to modify IP headers correctly.

This comprehensive theory note covers all the necessary concepts, formulas, and problem-solving patterns for the Network Layer. It ensures that you are well-prepared to tackle questions on subnetting, routing tables, fragmentation, and NAT.