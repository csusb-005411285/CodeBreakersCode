class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_map = {}
        result = []

        # [8,1,2,2,3]
        for i in range(len(nums)):
            num_map[nums[i]] = -1 # {8:0, 1:0, 2:0, 3:0}
        
        sorted_nums = sorted(nums) # [1, 2, 2, 3, 8]

        for i in range(len(sorted_nums)): # 1
            n = sorted_nums[i] # 2

            if num_map[n] == -1: # {1: 0, 2: 0}
                num_map[n] = i # {1: 0, 2: 1}
        
        for i in range(len(nums)):
            n = nums[i]

            if n in num_map:
                result.append(num_map[n])
        
        return result
