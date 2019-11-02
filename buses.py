from collections import defaultdict


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        routes_at = defaultdict(set)
        for route_id, route in enumerate(routes):
            for stop in route:
                routes_at[stop].add(route_id)

        edges = defaultdict(set)
        for route_set in routes_at.values():
            for a in route_set:
                edges[a].update(route_set)

        previous = set()
        current = routes_at[S]
        target = routes_at[T]
        step = 1

        while current.isdisjoint(target):
            if len(current) == len(previous):
                return -1

            new_elements = current.difference(previous)
            previous = current.copy()
            for stop in new_elements:
                current.update(edges[stop])
            step += 1

        return step
