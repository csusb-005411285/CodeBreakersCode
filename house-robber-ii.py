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

  # Recursive solution with memoization.
class Solution:
    def __init__(self):
        self.cache = defaultdict(int) 

    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0] 
        max_option_1 = self.rob_helper(nums[0: len(nums) - 1], len(nums) - 2)
        self.cache = defaultdict(int)
        max_option_2 = self.rob_helper(nums[1:], len(nums) - 2)
        return max(max_option_1, max_option_2)

    def rob_helper(self, nums, i):
        if i in self.cache:
            return self.cache[i]
        if i == 0:
            self.cache[i] = nums[0]
            return self.cache[i]
        if i == 1:
            self.cache[i] = max(nums[0], nums[1])
            return self.cache[i]
        self.cache[i] = max(nums[i] + self.rob_helper(nums, i - 2), self.rob_helper(nums, i - 1))
        return self.cache[i]
    
 # Iterative solution with memoization.
class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        option_1 = nums[0: len(nums) - 1]
        option_2 = nums[1:]
        return max(self.rob_helper(option_1), self.rob_helper(option_2))
    
    def rob_helper(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0] 
        cache = defaultdict(int)
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cache[i] = max(nums[i] + cache[i - 2], cache[i - 1])
        return cache[len(nums) - 1]
