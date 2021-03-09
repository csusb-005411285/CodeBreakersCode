class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)% 2 != 0:
            return False
        target = sum(nums)//2
        cache = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        cache[0][0] = True
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                num = nums[row - 1]
                if num == col:
                    cache[row][col] = True
                elif col > num:
                    cache[row][col] = cache[row - 1][col] or cache[row - 1][col - num]
                else:
                    cache[row][col] = cache[row - 1][col]
        return cache[-1][-1]
