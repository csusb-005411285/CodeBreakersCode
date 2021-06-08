def count_ways(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 1
  if n == 3:
    return 2
  return count_ways(n - 4) + count_ways(n - 3) + count_ways(n - 1)

def count_ways(n):
  cache = [0 for _ in range(n + 1)]
  cache[0] = 1
  cache[1] = 1
  cache[2] = 1
  cache[3] = 2
  for i in range(4, n + 1):
    cache[i] = cache[i - 4] + cache[i - 3] + cache[i - 1]
  return cache[-1]
