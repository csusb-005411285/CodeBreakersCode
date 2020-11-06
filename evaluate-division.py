class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict) 
        ans = []
        for index, equation in enumerate(equations):
            source, dest = equation
            graph[source][dest] = values[index] 
            graph[dest][source] = 1/values[index]
        for k, v in enumerate(queries):
            # this is the key step
            visited = set()
            res = self.calc_equation_helper(graph, v[0], visited, v[1], 1.0)
            ans.append(res)
        return ans
    
    def calc_equation_helper(self, graph, source, visited, dest, res):
        if dest not in graph or source not in graph:
            return -1.0
        if source == dest:
            return 1.0
        if source in visited:
            # this step took a long time to figure out
            return -1.0
        if dest in graph[source]:
            return res * graph[source][dest] 
        visited.add(source)
        for n_dest, val in graph[source].items():
            ans = self.calc_equation_helper(graph, n_dest, visited, dest, res*val)
            # a source(n_dest) can have multiple values, choose the valid answer.
            if ans != -1.0:
                return ans 
        visited.remove(source)
        return -1.0
    
