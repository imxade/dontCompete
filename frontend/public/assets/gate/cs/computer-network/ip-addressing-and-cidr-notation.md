**IP Addressing and CIDR Notation**
=====================================

### Introduction

IP addressing is a crucial aspect of computer networking, enabling devices to communicate with each other over the internet. Classless Inter-Domain Routing (CIDR) notation provides a more efficient way to represent IP addresses by allowing subnetting without using classful networks. This note covers the theoretical concepts and CIDR notation required for GATE CS exam.

### Core Concepts

#### Binary Number System

IP addresses are represented in binary, which is a base-2 number system consisting of only two digits: 0 and 1. Understanding binary representation is essential for calculating IP addresses.

#### Subnet Mask (Subnetting)

A subnet mask determines the number of bits used to represent the network ID in an IP address. It's denoted by the `/` symbol followed by a number, e.g., `192.168.1.0/24`. The value of the subnet mask is used to calculate the number of hosts on a network.

#### CIDR Notation

CIDR notation is an extension of the previous method (IP addressing and subnetting) for representing IP addresses. It combines routing prefixes with subnetting, allowing more efficient routing. In CIDR notation:

* The `/` symbol separates the address from its prefix length.
* The prefix length determines the number of bits used to represent the network ID.

#### Supernetting

Supernetting is a technique that allows multiple networks to share the same IP address space by aggregating them into a single, larger subnet. This reduces routing table sizes and minimizes administrative tasks.

### Key Formulas/Theorems

**Subnet Mask Calculation**

Given a prefix length (`p`), calculate the subnet mask as follows:

$$
\text{subnet mask} = (2^p - 2) / (2^{32 - p} + 1)
$$

For example, with `p=24`, we get:

$$
\text{subnet mask} = (2^{24} - 2) / (2^{8} + 1) = 255.255.255.0
$$

### Problem Solving Patterns

1. **CIDR Prefix Representation**: Given an IP address range, determine the exact CIDR prefix that represents it.
2. **Subnet Mask Determination**: Calculate the subnet mask given a prefix length or an IP address range.

### Examples with Solutions

**Example 1: CIDR Prefix Representation**

Given the IP address range `10.12.2.0` to `10.12.3.255`, determine the exact CIDR prefix that represents it.

```mermaid
graph LR
A[Start] --> B[Calculate number of hosts]
B --> C[Number of hosts = 256]
C --> D[Determine network ID]
D --> E[Network ID = 10.12.2.0/24]
E --> F[Exact CIDR prefix is 10.12.2.0/23]
```

**Solution**: The exact CIDR prefix representing the given IP address range is `10.12.2.0/23`.

### Common Pitfalls

1. **Forgetting to calculate the subnet mask**: Always determine the subnet mask when working with IP addresses and CIDR notation.
2. **Misinterpreting the number of hosts**: Be aware that the number of hosts depends on the subnet mask, not just the prefix length.

### Quick Summary

* Binary representation is essential for understanding IP addresses.
* Subnet mask determines the number of bits used to represent the network ID.
* CIDR notation combines routing prefixes with subnetting.
* Supernetting allows multiple networks to share a single, larger subnet.

**This theory note covers all theoretical concepts and formulas required for solving GATE CS exam questions related to IP addressing and CIDR notation.