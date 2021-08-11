class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        op = 0
        prev = 0
        for num in target:
            op += max(num - prev, 0)
            prev = num
        return op
