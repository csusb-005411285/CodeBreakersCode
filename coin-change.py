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
