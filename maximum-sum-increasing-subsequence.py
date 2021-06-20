def find_MSIS(nums):
  cache = {}
  max_sum = 0
  for i, num in enumerate(nums):
    cache[i] = num
  for i, num in enumerate(nums):
    for j in range(i):
      if nums[i] > nums[j]:
        cache[i] = max(cache[i], nums[i] + cache[j])
      max_sum = max(max_sum, cache[i])
  return max_sum
