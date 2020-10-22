class Solution:
    def jump(self, nums: [int]) -> int:
        if nums[0] == 0 or len(nums) == 1:
            return 0
        max_jump = float('-inf')
        increment_jump_at_index = 0
        num_jumps = 0
        for i in range(len(nums)):
            if i >= len(nums) - 1:
                return num_jumps
            if nums[i] + i > max_jump:
                max_jump = nums[i] + i
            # all indices before this and until the last increment_jump_at_index will have the same jump value.
            if i == increment_jump_at_index:
                num_jumps += 1 
                increment_jump_at_index = max_jump
        return num_jumps

# DP
class Solution:
    def jump(self, nums: [int]) -> int:
        # define a cache. init it to 0's
        cache = {} # [0 0 0 0 0]
        for i in range(len(nums)):
            cache[i] = float('inf') 
        cache[0] = 0
        # loop through the jumps
        # [2,3,1,1,4]
        for i in range(len(nums)): # 3
            # loop from the start to the current jump
            for j in range(0, i): # 1
                prev = nums[j] # 3
                # check if we can reach the current index from the previous index
                if prev + j >= i: # 3 + 1 >= 3
                    # get the number of jumps at the previous index + 1
                    # before storing the value in the cache, check for the min. value
                    cache[i] = min(cache[i], cache[j] + 1) # [0 1 1 2]
        # return the value in the final index
        return cache[len(nums) - 1
