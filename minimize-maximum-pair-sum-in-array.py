class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # init vars
        # store the max pair sum
        max_pair_sum = float('-inf')
        # two pointers
        left = 0
        right = len(nums) - 1
        # inital checks
        # if length of nums is 2
        
        # process
        # sort the input
        nums.sort()
        # use while loop, loop until the pointers meet
        while left < right:
            # calculate the sum
            _sum = nums[left] + nums[right]
            # compute the max value
            max_pair_sum = max(max_pair_sum, _sum)            
            # move pointers
            left += 1
            right -= 1
        # return max pair sum
        return max_pair_sum
