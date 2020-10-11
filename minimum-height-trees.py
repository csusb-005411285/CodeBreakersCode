class Solution:
    def findMinHeightTrees(self, n: int, edges: [[int]]) -> [int]:
        adj_list = defaultdict(list)
        indegrees = defaultdict(int)
        root = []
        stack = deque()
        no_of_leaves = n

        if n == 1:
            return [0]

        if n <= 2:
            return edges[0]
        
        # populate indegrees
        for i in range(n):
            indegrees[i] = 0

        # build adj list
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
            indegrees[src] += 1
            indegrees[dest] += 1

        # get all the leaf nodes
        nodes_with_one_indegree = []
        for k, v in indegrees.items():
            if v == 1:
                nodes_with_one_indegree.append(k)
        stack.append(nodes_with_one_indegree)
        
        while no_of_leaves > 2 and stack:
            nodes = stack.pop()
            no_of_leaves = no_of_leaves - len(nodes)
            nodes_with_one_indegree = []
            for node in nodes:
                for vert in adj_list[node]:
                    indegrees[vert] -= 1
                    if indegrees[vert] == 1:
                        nodes_with_one_indegree.append(vert)
            if nodes_with_one_indegree:
                stack.append(nodes_with_one_indegree)

        return stack.pop() 
