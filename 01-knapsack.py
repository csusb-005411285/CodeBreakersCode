# without memoization
class Solution:
    def solve(self, weights, values, capacity):
        return self._solve(weights, values, capacity, 0)

    def _solve(self, weights, values, capacity, i):
        if i >= len(weights):
            return 0
        if capacity < 0:
            return 0
        include = 0
        if capacity >= weights[i]:
            include = values[i] + self._solve(weights, values, capacity - weights[i], i + 1)
        exclude = self._solve(weights, values, capacity, i + 1)
        return max(include, exclude)
    
# top-down
class Solution:
    def solve(self, weights, values, capacity):
        cache = {}
        return self._solve(weights, values, capacity, 0, cache)

    def _solve(self, weights, values, capacity, i, cache):
        if (i, capacity) in cache:
            return cache[(i, capacity)]
        if i >= len(weights):
            return 0
        if capacity < 0:
            return 0
        include = 0
        if capacity >= weights[i]:
            include = values[i] + self._solve(weights, values, capacity - weights[i], i + 1, cache)
        exclude = self._solve(weights, values, capacity, i + 1, cache)
        cache[(i, capacity)] = max(include, exclude)
        return max(include, exclude)

# Alternte top-down
class Solution:
   def solve(self, weights, values, capacity):
       cache = defaultdict(int)
       return self.get_max_value(weights, values, capacity, 0, 0, cache)
  
   def get_max_value(self, weights, values, max_capacity, i, curr_capacity, cache):
       if (i, curr_capacity) in cache:
           return cache[(i, curr_capacity)]
       if i == len(weights) or curr_capacity > max_capacity:
           return 0
       include = 0
       if curr_capacity + weights[i] <= max_capacity:
           include = self.get_max_value(weights, values, max_capacity, i + 1, curr_capacity + weights[i], cache) + values[i]
       exclude = self.get_max_value(weights, values, max_capacity, i + 1, curr_capacity, cache)
       cache[(i, curr_capacity)] = max(include, exclude)
       return max(include, exclude)

    
# bottom-up
class Solution:
    def solve(self, weights, values, capacity):
        cache = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
        cache[0][0] = 0
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                exclude = cache[row - 1][col]
                include = 0
                if weights[row - 1] <= col:
                    include = values[row - 1] + cache[row - 1][col - weights[row - 1]]
                cache[row][col] = max(include, exclude)
        return cache[-1][-1]
