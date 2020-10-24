# Without memoization. TLE.
class Solution:
    def __init__(self):
        self.cache = defaultdict(int)
        self.count = 0
        self.combinations = []

    def combinationSum4(self, nums: [int], target: int) -> int:
        nums.sort()
        # define a helper method
        self.combination_sum_helper(nums, target, 0, [])
        # return the count of the results
        return self.count

    def combination_sum_helper(self, nums, target, next_index, candidates):
        if sum(candidates) > target:
            return
        if sum(candidates) == target:
            self.count += 1
            return       
        for i in range(len(nums)):
            self.combination_sum_helper(nums, target, i, candidates + [nums[i]])
        return
