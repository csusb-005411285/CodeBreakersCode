#Educative
def _count_ways(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  return _count_ways(n - 3) + _count_ways(n - 2) + _count_ways(n - 1)


def count_ways(n):
  cache = [0 for _ in range(n + 1)]
  cache[0] = 1
  cache[1] = 1
  cache[2] = 2
  for i in range(3, len(cache)):
    cache[i] = cache[i - 3] + cache[i - 2] + cache[i - 1]
  return cache[-1]

def count_ways(n):
  last = 1
  prev = 1
  curr = 2
  for i in range(3, n+1):
    last_curr = curr
    curr = curr + prev + last
    last = prev
    prev = last_curr
  return curr

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        results = [0 for _ in range(n)]
        results[0] = 1
        results[1] = 2

        for i in range(2, n):
            results[i] = results[i - 1] + results[i - 2]
        
        return results[-1]
