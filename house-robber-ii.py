# Without memoization. Recursive solution. TLE.
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0] 
        return max(self.rob_helper(nums[0: len(nums) - 1], len(nums) - 2), self.rob_helper(nums[1:], len(nums) - 2))

    def rob_helper(self, nums, i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        return max(nums[i] + self.rob_helper(nums, i - 2), self.rob_helper(nums, i - 1))
