# top-down
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        cache = defaultdict(int)
        return self._can_partition(nums, 0, 0, target, cache)
        
    def _can_partition(self, nums, i, _sum, target, cache):
        if (i, _sum) in cache:
            return cache[(i, _sum)]
        if _sum == target:
            return True
        if i >= len(nums):
            return False
        include = self._can_partition(nums, i + 1, _sum + nums[i], target, cache)
        exclude = self._can_partition(nums, i + 1, _sum, target, cache)
        cache[(i, _sum)] = include or exclude 
        return cache[(i, _sum)]

# bottom-up
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        cache = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for row in range(len(cache)):
            cache[row][0] = True
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                exclude = cache[row - 1][col]
                include = False
                if col >= nums[row - 1]:
                    include = cache[row - 1][col - nums[row - 1]]
                cache[row][col] = include or exclude
        return cache[-1][-1]
