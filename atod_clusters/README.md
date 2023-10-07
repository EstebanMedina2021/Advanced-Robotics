# Atod Clusters

## Problem Statement

In the mystical world of Atod, two powerful beings, Invoker and Puck, have created a celestial tapestry by connecting radiant stars with magical lines. This tapestry forms intricate patterns known as Atod Clusters. The challenge is to determine how many connections each Atod Cluster comprises. Two stars are considered part of the same Atod Cluster if they are connected either directly or through other stars.

## Input

The input consists of the following:

- The first line contains two integers separated by a space: `N` and `M`, representing the number of stars in the sky and the number of magical connections drawn, respectively.
- The subsequent `M` lines each contain two integers: `Ai` and `Bi`, representing the star number that Invoker identified and the star number that Puck identified in a connection.

## Output

The output consists of the following:

1. An integer `K`, representing the total number of Atod Clusters formed.
2. `K` lines listing the number of connections each Atod Cluster has, in non-descending order.

## Constraints

- 1 ≤ `N`, `M` ≤ 10^4
- 1 ≤ `Ai`, `Bi` ≤ `N` 
- A ≠ B

## Examples

### Sample 1

Input:
5 3
1 2
2 3
4 5

Output:
2
1
2


## Usage

You can use this algorithm to analyze celestial patterns and identify Atod Clusters within a starry sky. Simply provide the input as described above, and the program will output the cluster information.

## Implementation

The algorithm to find Atod Clusters is implemented in Python using union-find (disjoint set) data structures. It efficiently connects stars and calculates cluster sizes.

To find Atod Clusters in your own code, you can use the `find_clusters` function provided in the `atod_clusters.py` module. The module contains helper functions for union-find operations.

## Contributing

Contributions to improve the code or add features are welcome! Please fork the repository, create a new branch, and submit a pull request. Ensure that your code is well-documented and passes any existing unit tests.

