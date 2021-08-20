class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # init vars
        answers = [0 for _ in range(len(queries))]
        degree_list = [0 for _ in range(n + 1)] # 1
        edge_map = defaultdict(int)
        #check for invalid inputs
        
        #build degree list
        for edge in edges: # 3
            src, dest = edge
            degree_list[src] += 1
            degree_list[dest] += 1
        #create a frequency map for edges in the edges list
        for edge in edges: # 2
            src = min(edge)
            dest = max(edge)
            edge_map[(src, dest)] += 1
        sorted_degree_list = sorted(degree_list) # 4
        #loop through queries, process
        for index, query in enumerate(queries):
            degree = 0
            right = n
            for left in range(1, n):
                right = max(left, right)
                while left < right:
                    if sorted_degree_list[left] + sorted_degree_list[right] > query:
                        right -= 1 # 5
                degree += n - right
            #reduce the count for the duplicate edge
            for key, value in edge_map.items():
                i, j = key
                if degree_list[i] + degree_list[j] - value <= query < degree_list[i] + degree_list[j]:
                    degree -= 1
            answers[index] = degree
        #return
        return answers
'''
1. n + 1 to keep the array 1-index
2. To keep the edges in a consistent format. For e.g (a, b) or (b, a) should end up being (a, b)
3. build degree list.
4. sorting will work here because we need to use all the edges -- not only the ones that are connected.
5. Inspired from two-sum solution.
'''
