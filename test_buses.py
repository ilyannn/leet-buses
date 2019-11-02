import unittest
from buses import Solution

routes = [[1, 2, 7], [3, 6, 7]]
S = 1


class MyTestCase(unittest.TestCase):
    def test_3routes(self):
        T = 6
        answer = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(answer, 2)

    def test_not_possible(self):
        T = 4
        answer = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(answer, -1)

    def test_same_stop(self):
        T = 1
        answer = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(answer, 0)


if __name__ == '__main__':
    unittest.main()
