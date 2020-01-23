class Solution:
  def canJump(self, nums: List[int]) -> bool:
    if len(nums) <= 1:
      return True
    # initialize a pointer that calculates max jump from an index
    max_jump = 0
    # loop through the list:
    for curr in range(len(nums) - 1):
      # the second pointer, curr; stores the current index
      # if the curr pointer is greater than the max jump pointer, it means max jump is stuck, hence return false
      if curr > max_jump: #?
        return False
      # choose the max jump from that index; the max jump is the furthest index we can reach from the current location
      max_jump = max(max_jump, nums[curr] + curr)
    # return true or false if max_jump is greater than the last index of the list
    return max_jump >= len(nums) - 1

  # 2nd attempt
  class Solution:
  def canJump(self, nums: List[int]) -> bool:
    # initializee a variable to store the max jump
    max_jump = 0

    jump_from_pos = 0
    # loop through the list
    for i in range(len(nums)):  
      # if the loop variable is ahead of max jump variable 
      if i > max_jump:  
        # return false
        return False
      # for each value: add the index
      jump_from_pos = i + nums[i]
      # calculate the max jump
      max_jump = max(max_jump, jump_from_pos)
      
    # return true
    return True
