from atod_clusters import find_clusters

if __name__ == "__main__":
    """
    Entry point of the program for finding Atod Clusters.

    This code reads input from the user, processes it, and prints the resulting clusters.

    Usage:
        $ python main.py

    Input:
        - Two integers separated by a space: N and M
        - M lines each containing two integers representing connections: Ai and Bi

    Output:
        - The total number of Atod Clusters, K
        - K lines listing the number of connections each Atod Cluster has, in non-descending order
    """
    n, m = map(int, input().split())
    connections = [tuple(map(int, input().split())) for _ in range(m)]

    clusters = find_clusters(n, connections)

    print(len(clusters))
    for cluster in clusters:
        connections_cluster = cluster - 1
        print(connections_cluster)
