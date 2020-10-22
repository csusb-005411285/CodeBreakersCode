class Solution:
    def jump(self, nums: [int]) -> int:
        if nums[0] == 0 or len(nums) == 1:
            return 0
        max_jump = float('-inf')
        index_prev_max_jump = 0
        num_jumps = 0
        for i in range(len(nums)):
            if i >= len(nums) - 1:
                return num_jumps
            if nums[i] + i > max_jump:
                max_jump = nums[i] + i
            if i == index_prev_max_jump:
                num_jumps += 1 
                index_prev_max_jump = max_jump
        return num_jumps

