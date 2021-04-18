class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_map = defaultdict(int)
        max_ones = 0
        left = 0
        for right, num in enumerate(nums):
            num_map[num] += 1
            while num_map[0] > k and left <= right:
                num_map[nums[left]] -= 1
                left += 1
            max_ones = max(max_ones, right - left + 1)
        return max_ones
