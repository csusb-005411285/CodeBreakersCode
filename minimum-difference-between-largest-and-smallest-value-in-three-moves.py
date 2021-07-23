class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        nums.sort()
        option1 = option2 = option3 = option4 = float('inf')
        option1 = nums[-1] - nums[3]
        option2 = nums[-4] - nums[0]
        option3 = nums[-2] - nums[2]
        option4 = nums[-3] - nums[1]
        return min(option1, option2, option3, option4)
        
