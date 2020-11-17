# Optimized solution. Use this over the other.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr = nums
        left = 0
        right = len(arr) - 1
        # Template 2
        while left < right:
            mid = left + ((right - left)//2)
            if arr[mid] == target:
                return mid
            elif arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        
        if arr[pivot] == target:
            return pivot
        elif target <= arr[-1]:
            left = pivot
            right = len(arr) - 1
        elif target > arr[-1]:
            right = pivot
            left = 0

        while left <= right:
            mid = left + ((right - left)//2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target in nums else -1 

        left = 0
        right = len(nums) - 1
        pivot = 0
        mid = 0

        while left <= right: # 3, 4
            mid = left + ((right - left)//2) # 4

            if nums[mid] >= nums[0]: # 0 > 4 ??
                left = mid + 1 # 
            else:
                right = mid - 1# 3 ??
        
        if left == len(nums):
            pivot = 0
        else:
            pivot = left # 4 
        
        if target < nums[0]:
            left = pivot # 
            right = len(nums) - 1
        elif pivot == 0:
            left = 0
            right = len(nums) - 1
        else:
            right = pivot 
            left = 0

        while left <= right: # 4, 4
            mid = left + (right - left)//2 # 4

            if target == nums[mid]: # 4 == 4
                return mid
            elif target < nums[mid]: # 0 > 1 
                right = mid - 1 # 4
            else:
                left = mid + 1 # 

        return -1 
