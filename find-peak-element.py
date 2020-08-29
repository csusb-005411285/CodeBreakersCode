class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # 1 2 3 1
        while left < right: # 2 2
            mid = left + ((right - left)//2) # 2 + (3 - 2)//2 = 2

            if nums[mid] > nums[mid + 1]: # 3 > 1
                right = mid # 2
            else:
                left = mid + 1 # 2
            
        return left 
