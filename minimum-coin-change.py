# top-down
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self._coin_change(coins, amount, 0)
        return res if res != float('inf') else -1 
    
    def _coin_change(self, coins, amt, i):
        if i >= len(coins) or amt < 0:
            return float('inf')
        if amt == 0:
            return 0
        include = float('inf')
        if amt >= coins[i]:
            include = 1 + self._coin_change(coins, amt - coins[i], i)
        exclude = self._coin_change(coins, amt, i + 1)
        return min(include, exclude)
      
def count_change(denominations, total):
  min_change = _count_change(denominations, total, 0, 0)
  return min_change

def _count_change(denominations, total, i, curr):
  if total == 0:
    return curr
  if i == len(denominations) or total < 0:
    return float('inf')
  include = float('inf')
  if denominations[i] <= total:
    include = _count_change(denominations, total - denominations[i], i, curr + 1)
  exclude = _count_change(denominations, total, i + 1, curr)
  return min(include, exclude)

# bottom-up
def count_change(denominations, total):
  cache = [[float('inf') for _ in range((total + 1))] for _ in range(len(denominations) + 1)]
  cache[0][0] = 1
  # when amount is 0, return 0. This comes from the base case of top-down approach.
  for row in range(len(cache)):
    cache[row][0] = 0
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      cache[row][col] = cache[row - 1][col]
      if col >= denominations[row - 1]:
        if cache[row][col - denominations[row - 1]] != float('inf'):
          cache[row][col] = min(cache[row][col], 1 + cache[row][col - denominations[row - 1]])
  return cache[-1][-1] if cache[-1][-1] != float('inf') else -1
