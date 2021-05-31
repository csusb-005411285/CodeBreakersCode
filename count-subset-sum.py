def count_subsets(num, sum):
  cache = {}
  return _count_subsets(num, sum, 0, cache)

def _count_subsets(num, sum, i, cache):
  if (i, sum) in cache:
    return cache[(i, sum)]
  if sum == 0:
    return 1
  if i == len(num) or sum < 0:
    return 0
  include = _count_subsets(num, sum - num[i], i + 1, cache)
  exclude = _count_subsets(num, sum, i + 1, cache)
  cache[(i, sum)] = include + exclude
  return include + exclude
  

def count_subsets(num, sum):
  cache = [[0 for _ in range(sum + 1)] for _ in range(len(num) + 1)]
  cache[0][0] = 1
  for row in range(len(cache)):
    cache[row][0] = 1
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      cache[row][col] = cache[row - 1][col]
      if num[row - 1] <= col:
        cache[row][col] += cache[row - 1][col - num[row - 1]]
  return cache[-1][-1]
