def can_partition(num):
  _sum = sum(num)//2
  cache = [[False for _ in range(_sum + 1)] for _ in range(len(num) + 1)]
  cache[0][0] = True
  for row in range(len(cache)):
    cache[row][0] = True
  for row in range(1, len(cache)):
    for col in range(1, len(cache[0])):
      cache[row][col] = cache[row - 1][col]
      if num[row - 1] <= col:
        cache[row][col] |= cache[row - 1][col - num[row - 1]]
  n = len(num)
  sum1 = 0
  for col in range(len(cache[0]) - 1, -1, -1):
    if cache[n][col]:
      sum1 = col
      break
  sum2 = sum(num) - sum1
  return abs(sum2 - sum1)

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
