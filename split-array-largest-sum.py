class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = -1
        while left <= right:
            mid = left + ((right - left)//2)
            if self.can_split_array_into_less_than_m_parts(nums, m, mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
    
    def can_split_array_into_less_than_m_parts(self, nums, m, num):
        count = 0
        sums = 0
        for i, val in enumerate(nums):
            sums += val
            if sums > num:
                count += 1
                sums = val
        return count + 1 <= m # + 1 is for the last partition
