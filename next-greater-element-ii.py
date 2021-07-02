class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                index, val = stack.pop()
                res[index] = num
            stack.append((i, num))
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                index, val = stack.pop()
                res[index] = num
        return res
