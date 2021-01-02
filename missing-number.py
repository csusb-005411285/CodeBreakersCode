class Solution:
    def missingNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            val = nums[i]
            if i != val and val < len(nums):
               nums[i], nums[val] = nums[val], nums[i]
            else:
                i += 1
        for i, num in enumerate(nums):
            if i != num: return i
        return len(nums)            
