class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(len(nums) - 1):
            if nums[right] != nums[right + 1]:
                left += 1
                nums[left] = nums[right + 1]
        return left + 1
      
class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    # initalize the curr index to point at the first index
    slow_pointer = 1
    # loop through all the numbers
    for curr_pointer in range(0, len(nums) - 1):
      # if the current number is not equal to the next number
      if nums[curr_pointer] != nums[curr_pointer + 1]:
        # store the next number in the index which equals the value of curr index 
        nums[slow_pointer] = nums[curr_pointer + 1]
        slow_pointer += 1
    # return the length of array
    return slow_pointer
    
