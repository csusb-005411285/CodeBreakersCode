# O(n) time and O(1) space in a single pass. This is the preferred solution.
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        nums = arr
        max_len = 0
        if len(arr) < 3: return 0
        for k in range(1, len(arr)):
            if k + 1 < len(nums) and nums[k] > nums[k - 1] and nums[k] > nums[k + 1]:
                curr_count = 0
                left = k - 1
                right = k + 1
                while left - 1 >=0:
                    if  nums[left - 1] < nums[left]:
                        left -= 1
                    else:
                        break
                while right + 1 < len(nums):
                    if nums[right + 1] < nums[right]:
                        right += 1
                    else:
                        break
                curr_count = (right - left) + 1
                max_len = max(max_len, curr_count)
        return max_len

class Solution:
  def longestMountain(self, A: List[int]) -> int:
    # initialize two pointers up and down, both have the length equal to the size of the List, and they all have 0 as value
    up = [0] * len(A)
    down = [0] * len(A)
    # initalize a variable to store the max value
    _max = 0
    # loop from the end
    for i in range(len(A) - 2, 0, -1):
      # if the current element is greater than the next element then increment the down pointer by 1
      if A[i] > A[i + 1]:
        down[i] = down[i+1] + 1
    # loop from the beginning
    for j in range(1, len(A)):
      # if the current pointer is greater than the previous pointer then increment the up pointer by 1
      if A[j] > A[j - 1]:
        up[j] = up[j - 1] + 1
      # if the up and down pointer for that index is greater than 0
      if up[j] > 0 and down[j] > 0:
        # if the sum of the up and down values for that index is greater than the previous max then this is the new max
        _max = max(_max, up[j] + down[j] + 1)
    
    # return the result
    return _max
