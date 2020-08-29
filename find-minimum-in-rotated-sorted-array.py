class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        n = nums

        # 1 2 
        while left < right: # 1 1
            mid = left + ((right - left)//2) # 1

            if n[mid] < n[-1]: # 1 < 1
                right = mid # 3
            else:
                left = mid + 1 # 2

        return nums[left]
