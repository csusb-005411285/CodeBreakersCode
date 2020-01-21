class Solution:
  def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <= 1:
      return 0
    # initalize two pointers: end_window and start_window
    end_window, start_window = 0,0
    # initialize a variable to store the number of subarrays
    _max, max_product = 0, 1
    # loop through the list
    for end_window in range(len(nums)):
      # calculate the product so far
      max_product *= nums[end_window]
      # while the product so far is greater than or equal to k
      while max_product >= k:
        max_product /= nums[start_window]
        start_window += 1
      
      _max += end_window - start_window + 1
      
    return _max
