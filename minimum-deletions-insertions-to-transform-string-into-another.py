def find_MDI(s1, s2):
  cache = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
  max_len = 0
  for row in range(1, len(cache)):
    for col in range(len(cache[0])):
      if s2[row - 1] == s1[col - 1]:
        cache[row][col] = 1 + cache[row - 1][col - 1]
      else:
        cache[row][col] = max(cache[row - 1][col], cache[row][col - 1])
      max_len = cache[row][col]
  c1 = max_len
  print("Minimum deletions needed: " + str(len(s1) - c1))
  print("Minimum insertions needed: " + str(len(s2) - c1))
