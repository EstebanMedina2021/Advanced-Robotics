def find_clusters(n, connections):
    """
    Find Atod clusters in a given star connection network.

    Args:
        n (int): The number of stars in the sky.
        connections (list of tuple): List of star connections represented as tuples (Ai, Bi).

    Returns:
        list of int: A list of cluster sizes in non-decreasing order.
    """
    parents = list(range(n + 1))
    cluster_sizes = [0] * (n + 1)

    for a, b in connections:
        union(parents, a, b)

    for i in range(1, n + 1):
        root = find_root(parents, i)
        cluster_sizes[root] += 1

    clusters = [size for size in cluster_sizes if size > 0]
    clusters.sort()

    return clusters


def find_root(parents, node):
    """
    Find the representative (root) of the set to which 'node' belongs.

    Args:
        parents (list of int): List of parent nodes representing disjoint sets.
        node (int): The node for which to find the representative.

    Returns:
        int: The representative (root) of the set to which 'node' belongs.
    """
    if parents[node] != node:
        parents[node] = find_root(parents, parents[node])
    return parents[node]


def union(parents, a, b):
    """
    Union operation to merge two sets by updating their parent nodes.

    Args:
        parents (list of int): List of parent nodes representing disjoint sets.
        a (int): Node 'a' belonging to one set.
        b (int): Node 'b' belonging to another set.

    Returns:
        None
    """
    root_a = find_root(parents, a)
    root_b = find_root(parents, b)
    if root_a != root_b:
        parents[root_a] = root_b
