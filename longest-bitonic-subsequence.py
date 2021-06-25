def find_LBS_length(nums):
  cache = [[1, 1] for _ in range(len(nums))] 
  max_len = 0
  find_increasing_subsequence(nums, cache)
  find_decreasing_subsequence(nums, cache)
  for i, num in enumerate(cache):
    max_len = max(max_len, cache[i][0] + cache[i][1] - 1)
  return max_len

def find_increasing_subsequence(nums, cache):
  for i, num in enumerate(nums[1:], start = 1):
    for j in range(0, i):
      if nums[j] < nums[i]:
        cache[i][0] = max(cache[i][0], cache[j][0] + 1)

def find_decreasing_subsequence(nums, cache):
  for i in range(len(nums) - 2, -1, -1):
    for j in range(len(nums) - 1, i, -1):
      if nums[j] < nums[i]:
        cache[i][1] = max(cache[i][1], cache[j][1] + 1)
