import unittest
from main import max_arrows


class TestMaxArrows(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(max_arrows(3, 3, [1, 2, 3]), 2)

    def test_example_2(self):
        self.assertEqual(max_arrows(5, 7, [5, 4, 2, 2, 3]), 3)

    def test_example_3(self):
        self.assertEqual(max_arrows(7, 7, [5, 4, 2, 2, 1, 1, 1]), 5)

    def test_example_4(self):
        self.assertEqual(max_arrows(7, 7, [5, 4, 2, 2, 2, 1, 1]), 4)

    def test_example_5(self):
        self.assertEqual(max_arrows(7, 1, [5, 4, 2, 2, 2, 1, 1]), 1)

    def test_example_6(self):
        self.assertEqual(max_arrows(3, 1, [5, 4, 2]), 0)


if __name__ == "__main__":
    unittest.main()
