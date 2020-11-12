class Solution:
    def findMin(self, nums: [int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l)//2

            if nums[l] == nums[r]:
                l += 1
            elif nums[m] <= nums[-1]:
                r = m
            else:
                l = m + 1

        return nums[l]
