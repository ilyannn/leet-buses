from collections import defaultdict


def prepareGraph(routes, S, T):
    """ Returns the edges of the graph as well as the source and target sets
    """
    # Which bus routes go through this stop?
    routes_at = defaultdict(set)

    # We'll use `enumerate` to assign each bus an id in order (0, 1, ...)
    for route_id, route in enumerate(routes):
        for stop in route:
            # And fill `routes_at` for each stop.
            routes_at[stop].add(route_id)

    # What are the edges of our graph?
    edges = defaultdict(set)
    for route_set in routes_at.values():
        # Each stop gives an edge between all routes that pass through it.
        for a in route_set:
            edges[a].update(route_set)

    # Now return the edges, source and target sets.
    return edges, routes_at[S], routes_at[T]


class Solution(object):

    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """

        # Short-circuit the obvious case.
        if S == T:
            return 0

        # Let's treat the buses as nodes of the graph.
        edges, current, target = prepareGraph(routes, S, T)

        # Now we can use the search for the shortest path.
        previous = set()
        step = 1

        # We'll stop when we reach one of the target buses.
        while current.isdisjoint(target):
            if len(current) == len(previous):
                return -1

            new_elements = current.difference(previous)
            previous = current.copy()
            for stop in new_elements:
                current.update(edges[stop])
            step += 1

        # Found it!
        return step
