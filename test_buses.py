import unittest
from buses import Solution

class MyTestCase(unittest.TestCase):
    def test_3routes(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        S = 1
        T = 6
        answer = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(answer, 2)

    def test_not_possible(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        S = 1
        T = 4
        answer = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(answer, -1)


if __name__ == '__main__':
    unittest.main()
