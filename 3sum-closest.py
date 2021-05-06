class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        i = 0
        for i in range(len(nums)):
            while i - 1 >= 0 and i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right] 
                if abs(target - three_sum) < abs(target - closest):
                    closest = three_sum
                if three_sum < target:
                    left += 1 
                elif three_sum > target:
                    right -= 1
                else:
                    return three_sum
        return closest
