class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        mid = 0
        while left <= right: 
            mid = left + (right - left)//2 
            if arr[mid] - mid - 1 >= k: 
                right = mid - 1 
            else:
                left = mid + 1 
        return left + k
