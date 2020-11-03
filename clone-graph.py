class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        stack = deque()
        stack.append(node)
        copy_graph = defaultdict(Node)
        visited = set()
        while stack:
            vert = stack.pop()
            if vert in visited: continue
            # as you pop each node, store them in a map
            # with the key being the original node and the value would be a copy of the new
            if vert not in copy_graph: copy_graph[vert] = Node(vert.val)
            copy_neigh = []
            visited.add(vert)
            # For the neighbors, create a copy of each neighbor as you visit them
            for neighbor in vert.neighbors:
                stack.append(neighbor)
                if neighbor not in copy_graph:
                    copy_graph[neighbor] = Node(neighbor.val)
                copy_neigh.append(copy_graph[neighbor])
            copy_graph[vert].neighbors = copy_neigh
        return copy_graph[node]
