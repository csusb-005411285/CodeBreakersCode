def find_SPM_count(str, pat):
  return _find_spm_count(str, pat, 0, 0)

def _find_spm_count(str, pat, i, j):
  if j == len(pat):
    return 1
  if i == len(str):
    return 0
  a = 0
  if str[i] == pat[j]:
    a =  _find_spm_count(str, pat, i + 1, j + 1)
  b = _find_spm_count(str, pat, i + 1, j)
  return a + b

# bottom-up
def find_SPM_count(str, pat):
  cache = [[0 for _ in range(len(pat) + 1)] for _ in range(len(str) + 1)]
  cache[0][0] = 1
  for row in range(len(cache)):
    cache[row][0] = 1
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      if str[row - 1] == pat[col - 1]:
        cache[row][col] = cache[row - 1][col - 1]
      cache[row][col] += cache[row - 1][col]
  return cache[-1][-1]
