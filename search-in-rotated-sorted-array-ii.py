class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left < right: 
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            mid = left + (right - left)//2 
            if nums[mid] <= nums[right]: 
                right = mid
            else:
                left = mid + 1
        pivot = left
        if nums[pivot] <= target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
