# brute force
def count_change(denominations, total):
  return _count_change(denominations, total, 0)

def _count_change(denominations, total, i):
  if total == 0:
    return 1
  if i >= len(denominations) or total < 0:
    return 0
  include = _count_change(denominations, total - denominations[i], i)
  exclude = _count_change(denominations, total, i + 1)
  return include + exclude

# top-down
 def change(amount: int, coins: List[int]) -> int:
        return _change(amount, coins, 0, defaultdict(int))
    
    def _change(amt, coins, i, cache):
        if (i, amt) in cache:
            return cache[(i, amt)]
        if amt == 0:
            return 1
        if i == len(coins) or amt < 0:
            return 0
        # 0
        # 1
        include = _change(amt - coins[i], coins, i, cache)
        exclude = _change(amt, coins, i + 1, cache)
        cache[(i, amt)] = include + exclude 
        return include + exclude

# Bottom-up
def count_change(denominations, total):
  cache = [[0 for _ in range(total + 1)] for _ in range(len(denominations) + 1)]
  cache[0][0] = 1
  for row in range(len(cache)):
    cache[row][0] = 1
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      cache[row][col] = cache[row - 1][col]
      if denominations[row - 1] <= col:
        cache[row][col] += cache[row][col - denominations[row - 1]]
  return cache[-1][-1]

class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        # initialize a list of size amount + 1 [float('inf'), float('inf'), ...]
        min_coins = [float('inf') for _ in range(amount + 1)]
        # initialize the 0th position
        min_coins[0] = 0

        # loop throuhg the denominations
        for coin in coins: # 2
            # loop throuhg the amounts
            for amt in range(amount + 1): # 3
                # the value of each cells is the minimum of the value of the cell and value of the cell
                # excluding the current denomination  + 1
                if coin <= amt:
                    min_coins[amt] = min(min_coins[amt], min_coins[amt - coin] + 1)

        # return the last cell value. If the last cell value is inf then return -1
        return min_coins[-1] if min_coins[-1] != float('inf') else -
