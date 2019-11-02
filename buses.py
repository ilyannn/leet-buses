from collections import defaultdict


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        direct = defaultdict(set)
        for route in routes:
            for stop in route:
                direct[stop].update(route)

        previous = set()
        current = set([S])
        step = 0

        while T not in current:
            if len(current) == len(previous):
                return -1

            step += 1
            new_elements = current.difference(previous)
            previous = current.copy()
            for stop in new_elements:
                current.update(direct[stop])

        return step
