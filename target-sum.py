class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = defaultdict(int)
        return self.get_number_of_expressions(nums, 0, target, 0, cache)
    
    def get_number_of_expressions(self, nums, i, target, val, cache):
        if (i, val) in cache:
            return cache[(i, val)]
        # base case
        # if i > len of nums
        if i > len(nums):
            return 0
        # if i == len of nums
        if i == len(nums):    
            # if val equals target
            if val == target:
                return 1
            return 0
        # add '+'
        add = self.get_number_of_expressions(nums, i + 1, target, val + nums[i], cache)
        # add '-'
        sub = self.get_number_of_expressions(nums, i + 1, target, val - nums[i], cache)
        # return the sum of previous calls
        cache[(i, val)] = add + sub
        return add + sub
