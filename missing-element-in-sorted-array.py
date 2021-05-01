class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = self.get_count_missing_elements(0, len(nums) - 1, nums)
        if k > missing:
            offset = k - missing
            return nums[-1] + offset
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = left + (right - left)//2
            count_missing = self.get_count_missing_elements(left, mid, nums)
            if count_missing >= k:
                # when the  count of missing numbers is larger than k, then check the left half
                right = mid
            else:
                left = mid
                k -= count_missing
        return nums[left] + k
    
    def get_count_missing_elements(self, start, end, nums):
        return (nums[end] - nums[start]) - (end - start)
