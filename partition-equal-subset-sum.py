class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        cache = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        cache[0][0] = True
        for row in range(1, len(nums) + 1):
            for col in range(target + 1):
                num = nums[row - 1]
                if col < num:
                    cache[row][col] = cache[row - 1][col]
                else:
                    cache[row][col] = cache[row - 1][col] or cache[row - 1][col - num]
        return cache[-1][-1]
