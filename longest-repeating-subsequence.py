def find_LRS_length(str):
  return _find_lrs(str, str, 0, 0)

def _find_lrs(s1, s2, i, j):
  if i == len(s1) or j == len(s2):
    return 0
  if i != j and s1[i] == s2[j]:
    return 1 + _find_lrs(s1, s2, i + 1, j + 1)
  return max(_find_lrs(s1, s2, i + 1, j), _find_lrs(s1, s2, i, j + 1))

# bottom-up
def find_LRS_length(str):
  cache = [[0 for _ in range(len(str) + 1)] for _ in range(len(str) + 1)]
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      if row != col and str[row - 1] == str[col - 1]:
        cache[row][col] = 1 + cache[row - 1][col - 1]
      else:
        cache[row][col] = max(cache[row - 1][col], cache[row][col - 1]) 
  return cache[-1][-1]
