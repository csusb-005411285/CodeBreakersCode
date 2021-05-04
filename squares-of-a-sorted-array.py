class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                res = [nums[left]*nums[left]] + res
                left += 1
            else:
                res = [nums[right]*nums[right]] + res
                right -= 1
        return res
