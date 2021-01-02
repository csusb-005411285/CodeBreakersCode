class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            val = nums[i]
            if val - 1 < len(nums) and val != nums[val - 1]:
                nums[i], nums[val - 1] = nums[val - 1], nums[i]
            else:
                i += 1
        for i, num in enumerate(nums):
            if num != i + 1: return num
        return len(nums)
