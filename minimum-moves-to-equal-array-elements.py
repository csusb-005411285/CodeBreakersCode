class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        min_moves = 0
        start = nums[0]
        for i, num in enumerate(nums[1:], start = 1):
            min_moves += num - start
        return min_moves
