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

# bottom-up
class Solution:
    def solve(self, weights, values, capacity):
        cache = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights))]
        return self._solve(weights, values, capacity, 0, cache)

    def _solve(self, weights, values, capacity, i, cache):
        if i >= len(weights) or capacity <= 0:
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]
        profit1 = 0
        if weights[i] <= capacity:
            profit1 = values[i] + self._solve(weights, values, capacity - weights[i], i + 1, cache)
        profit2 = self._solve(weights, values, capacity, i + 1, cache)
        cache[i][capacity] = max(profit1, profit2) 
        return cache[i][capacity]
