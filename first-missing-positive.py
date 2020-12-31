class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            if 0 < num < len(nums) and nums[i] != nums[num - 1]:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
            else:
                i += 1
        for j, num in enumerate(nums):
            if j + 1 != num: return j + 1
        return len(nums) + 1
