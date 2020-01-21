class Solution:
  def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <= 1:
      return 0
    # define a pointer for the end of the window and the start of the window
    start_window, end_window = 0, 0
    # define a var to store the results
    result = 0
    product = 1
    # loop through the list
    for end_window in range(len(nums)):  
      # calculate the product of all elements 
      product *= nums[end_window]
      # loop until the start window and end window meet #?
      while product >= k:
        # calculate the product by removing one element from the start of the window 
        product /= nums[start_window]
        # move the start of window forward
        start_window += 1
      
      # store the result
      result += end_window - start_window + 1
      
      end_window += 1
  
    return result
      
