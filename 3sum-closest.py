class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 
        nums = sorted(nums)
        closest_sum = float('inf')

        # 1,1,1,0
        # 0,1,1,1
        for i in range(len(nums) - 1): # 0
            left = i + 1 # 1
            right = len(nums) - 1 # 3

            while left < right: # 2 < 3
                sum_num = nums[left] + nums[i] + nums[right] # 1 + 0 + 1 = 2

                if abs(target - sum_num) < abs(closest_sum): # (100 - (2)) < 98 
                    closest_sum = target - sum_num # 98
                
                if sum_num > target: # 2 > 100
                    right -= 1 # 
                elif sum_num < target: # 2 < 100
                    left += 1 # 3
                elif sum_num == target:
                    return sum_num
                
        return  target - closest_sum 
