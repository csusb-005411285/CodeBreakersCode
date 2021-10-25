class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # init vars
        max_len = 0
        left = right = 0
        # initial checks
        if len(nums) == 1:
            return nums[0]
        while right < len(nums): 
            val = nums[right] 
            # if the number is 0, 
            if val == 0:
                # make left and right pointers the same
                left = right # 1
                # move both the pointers ahead
                left += 1 
                right += 1 
                # continue
                continue
            # if the number is 1,
            if val == 1: 
                # calculate the max len
                max_len = max(max_len, right - left + 1) 
                # move the right pointer ahead
                right += 1 
        # return
        return max_len
