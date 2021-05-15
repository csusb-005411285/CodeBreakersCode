class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        while right - 1 >= 0 and nums[right - 1] >= nums[right]:
            right -= 1
        if right == 0:
            return nums.reverse()
        swap_from = right - 1
        right = len(nums) - 1
        while right >= 0 and nums[right] <= nums[swap_from]:
            right -= 1
        swap_to = right
        nums[swap_from], nums[swap_to] = nums[swap_to], nums[swap_from]
        left = swap_from + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
