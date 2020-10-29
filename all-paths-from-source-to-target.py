class Solution:
    def __init__(self):
        self.paths = []

    def allPathsSourceTarget(self, graph: [[int]]) -> [[int]]:
        visited = set()
        dest = len(graph) - 1
        # call the helper method
        self.all_paths_source_target_helper(graph, 0, visited, dest, [0])
        # return the list of paths
        return self.paths

    def all_paths_source_target_helper(self, graph, vert, visited, dest, path): 
        # if vert is already visited 
        if vert in visited:
            return
        # if vert is dest
        if vert == dest:
            self.paths.append(path)
            return

        visited.add(vert) 
        # find neighbors
        neighbors = graph[vert] 
        for neighbor in neighbors: 
            # call the recursive method
            self.all_paths_source_target_helper(graph, neighbor, visited, dest, path + [neighbor]) # 3, (0, 1), 3 [0, 1, 3]
        # set the vert as not visited
        visited.remove(vert) 
        return
