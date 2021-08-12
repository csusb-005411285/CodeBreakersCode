class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # init vars
        left = max(nums)
        right = sum(nums)
        # check for invalid inputs
        if m == 1:
            return sum(nums) # 3
        # binary search
        while left < right:
            mid = left + (right - left)//2
            if self.get_number_of_splits(nums, mid) <= m:
                right = mid # 1
            else:
                left = mid + 1
        # return
        return right
    
    def get_number_of_splits(self, nums, limit):
        # init vars
        count = 0
        _sum = 0
        # loop, process
        for i, val in enumerate(nums):
            # sum
            _sum += val
            # check if sum > val
            if _sum > limit:
                # incr. count
                count += 1
                # reset sum
                _sum = val
        return count + 1 # 2
        
'''
1. if the number of splits are less than or equal to k, then we need to check the left half. This is because the smaller the number, the more number of splits we can get.
2. + 1 is for the last split.
3. if m == 1, it means the array is not split. So, the max value is sum of all values. 
'''
