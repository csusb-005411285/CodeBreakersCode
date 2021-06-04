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
  for row in range(len(cache)):
    cache[row][0] = 0
  for col in range(len(cache[0])):
    cache[row][col] = 0
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      cache[row][col] = cache[row - 1][col]
      if col >= denominations[row - 1]:
        if cache[row][col - denominations[row - 1]] != float('inf'):
          cache[row][col] = min(cache[row][col], 1 + cache[row][col - denominations[row - 1]])
  return cache[-1][-1] if cache[-1][-1] != float('inf') else -1
