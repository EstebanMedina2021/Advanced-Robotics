import unittest
from main import find_clusters


class TestFindClusters(unittest.TestCase):
    def test_find_clusters_example_1(self):
        n = 5
        connections = [(1, 2), (2, 3), (4, 5)]
        clusters = find_clusters(n, connections)
        clusters = [c - 1 for c in clusters]
        self.assertEqual(clusters, [1, 2])

    def test_find_clusters_example_2(self):
        n = 6
        connections = [(1, 2), (3, 4)]
        clusters = find_clusters(n, connections)
        clusters = [c - 1 for c in clusters]
        self.assertEqual(clusters, [0, 0, 1, 1])


if __name__ == "__main__":
    unittest.main()
