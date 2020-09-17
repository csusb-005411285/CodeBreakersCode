class Solution:
    def __init__(self):
        self.cache = {0: 1, 1: 1}

    def numTrees(self, n: int) -> int:
        return self.num_trees_helper(n)
    
    def num_trees_helper(self, n):
        if n in self.cache:
            return self.cache[n]
        
        prod = 0
        for i in range(n):
            lc = self.num_trees_helper(i)
            rc = self.num_trees_helper(n - 1 - i)
            prod += lc * rc
        
        self.cache[n] = prod 

        return self.cache[n]
