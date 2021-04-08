class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        mod = 10 ** 9 + 7
        res = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                res += pow(2, r - l, mod)
                l += 1
            else:
                r -= 1
        return res % mod
