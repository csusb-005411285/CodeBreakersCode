def find_minimum_deletions(nums):
  cache = [1 for _ in range(len(nums))]
  max_len = 0
  for i in range(1, len(nums)):
    for j in range(0, i):
      if nums[j] < nums[i]:
        cache[i] = max(cache[i], cache[j] + 1)
      max_len = max(max_len, cache[i])
  return len(nums) - max_len
