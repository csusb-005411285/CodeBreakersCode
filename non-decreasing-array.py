class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        count = 0


        for i in range(len(nums) - 1): # 4
            if nums[i] > nums[i + 1]: # 4 < 3

                if i - 1 < 0 or nums[i - 1] <= nums[i + 1]: 
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
            
                count += 1 # 1
                
                if count > 1:
                    return False
        
        return True
