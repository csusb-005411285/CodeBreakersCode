# top-down
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self._change(amount, coins, 0)
    
    def _change(self, amt, coins, i):
        if amt == 0:
            return 1
        if amt < 0 or i >= len(coins):
            return 0
        include = 0
        if amt >= coins[i]:
            include = self._change(amt - coins[i], coins, i)
        exclude = self._change(amt, coins, i + 1)
        return include + exclude

# top-down with memoization      
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = defaultdict(int)
        return self._change(amount, coins, 0, cache)
    
    def _change(self, amt, coins, i, cache):
        if (amt, i) in cache:
            return cache[(amt, i)]
        if amt == 0:
            return 1
        if amt < 0 or i >= len(coins):
            return 0
        include = 0
        if amt >= coins[i]:
            include = self._change(amt - coins[i], coins, i, cache)
        exclude = self._change(amt, coins, i + 1, cache)
        cache[(amt, i)] = include + exclude
        return include + exclude

# bottom-up with memoization
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for row in range(len(cache)):
            cache[row][0] = 1
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                cache[row][col] = cache[row - 1][col]
                if col >= coins[row - 1]:
                    cache[row][col] += cache[row][col - coins[row - 1]]
        return cache[-1][-1]
