# Without memoization
def can_partition(num, sum):
   cache = [[False for _ in range(sum + 1)] for _ in range(len(num) + 1)]
   for row in range(len(cache)):
      cache[row][0] = True
   for row in range(1, len(cache)):
      for col in range(1, len(cache[0])):
         cache[row][col] = cache[row - 1][col]
         if num[row - 1] <= col:
            cache[row][col] |= cache[row - 1][col - num[row - 1]]
   return cache[-1][-1]

# top-down
def can_partition(num, sum):
  cache = {}
  return _can_partition(num, sum, 0, cache)

def _can_partition(num, sum, i, cache):
   if (i, sum) in cache:
      return cache[(i, sum)]
   if i >= len(num):
      return False
   if sum == 0:
      return True
   if sum < 0:
      return False
   include = _can_partition(num, sum - num[i], i + 1, cache)
   exclude = _can_partition(num, sum, i + 1, cache)
   cache[(i, sum)] = include or exclude
   return include or exclude
  
# bottom-up  
def can_partition(num, sum):
   cache = [[False for _ in range(sum + 1)] for _ in range(len(num) + 1)]
   cache[0][0] = True
   for row in range(1, len(cache)):
      for col in range(1, len(cache[0])):
         cache[row][col] = cache[row - 1][col]
         if num[row - 1] <= col:
            cache[row][col] |= cache[row - 1][col - num[row - 1]]
   return cache[-1][-1]
