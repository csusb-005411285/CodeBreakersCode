class Solution:
    def maxSubArray(self, nums: [int]) -> bool:
        if len(nums) == 1:
            return nums[0]

        largest_sum = nums[0] 
        max_sum_so_far = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            max_sum_so_far = max(max_sum_so_far + num, num)
            largest_sum = max(largest_sum, max_sum_so_far)
        
        return largest_sum
