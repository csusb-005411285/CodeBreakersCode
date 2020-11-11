class Solution:
    def __init__(self):
        self.path = []

    def findItinerary(self, tickets: [[str]]) -> [str]:
        if not tickets: return []
        graph = defaultdict(list)
        for ticket in tickets:
            # the graph is directed
            src, dest = ticket
            graph[src].append(dest)
        for k, v in graph.items(): 
            # we perform the sort in the reversed order because when we pop, we pop from the end.
            # graph is a type of defaultdict(list) and not defaultdict(deque)
            graph[k] = sorted(v, reverse=True)
        self.find_itinerary_helper(graph, 'JFK')
        return self.path[::-1]

    def find_itinerary_helper(self, graph, vert):
        while graph[vert]:
            neigh_vert = graph[vert].pop()
            self.find_itinerary_helper(graph, neigh_vert)
        # Pay attention here.
        # insert vertex only after all of its neigbhors are visited
        # this is because the source always appears before the destination.
        self.path.append(vert)
        return
