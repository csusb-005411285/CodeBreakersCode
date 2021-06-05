# brute force
def count_ribbon_pieces(ribbonLengths, total):
  return _count_ribbon_pieces(ribbonLengths, total, 0, 0)

def _count_ribbon_pieces(ribbonLengths, total, i, curr):
  if total < 0:
    return 0
  if total == 0:
    return curr
  if i >= len(ribbonLengths):
    return 0
  include = _count_ribbon_pieces(ribbonLengths, total - ribbonLengths[i], i, curr + 1)
  exclude = _count_ribbon_pieces(ribbonLengths, total - ribbonLengths[i], i + 1, curr + 1)
  return max(include, exclude)

# bottom-up
def count_ribbon_pieces(ribbonLengths, total):
  cache = [[float('-inf') for _ in range(total + 1)] for _ in range(len(ribbonLengths) + 1)]
  for row in range(len(cache)):
    cache[row][0] = 0
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      cache[row][col] = cache[row - 1][col]
      if ribbonLengths[row - 1] <= col:
        if cache[row][col - ribbonLengths[row - 1]] != float('-inf'):
          cache[row][col] = max(cache[row][col], cache[row][col - ribbonLengths[row - 1]] + 1)
  return cache[-1][-1] if cache[-1][-1] != float('-inf') else -1
