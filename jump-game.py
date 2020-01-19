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
