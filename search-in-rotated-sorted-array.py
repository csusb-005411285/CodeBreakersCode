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
        # pay attention to <= in the step below
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
