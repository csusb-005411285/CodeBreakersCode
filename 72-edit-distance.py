def find_min_operations(s1, s2):
  return _find_min_operations(s1, s2, 0, 0)

def _find_min_operations(s1, s2, i, j):
  if i >= len(s1) and j >= len(s2):
    return 0
  if i >= len(s1) and j < len(s2):
    return len(s2) - j
  if i < len(s1) and j >= len(s2):
    return len(s1) - i    
  if s1[i] == s2[j]:
    return _find_min_operations(s1, s2, i + 1, j + 1)
  insert = _find_min_operations(s1, s2, i, j + 1)
  delete = _find_min_operations(s1, s2, i + 1, j)
  replace = _find_min_operations(s1, s2, i + 1, j + 1)
  return 1 + min(insert, delete, replace)

# bottom-up
def find_min_operations(s1, s2):
  cache = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
  for row in range(len(cache)):
    cache[row][0] = row
  for col in range(len(cache[0])):
    cache[0][col] = col
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      if s1[row - 1] == s2[col - 1]:
        cache[row][col] = cache[row - 1][col - 1]
      else:
        insert = cache[row][col - 1]
        delete = cache[row - 1][col]
        replace = cache[row - 1][col - 1]
        cache[row][col] = 1 + min(insert, delete, replace)
  return cache[-1][-1]
