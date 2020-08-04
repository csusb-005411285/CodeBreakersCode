class Solution:
    def maxWidthRamp(self, A: [int]) -> int:
        a = A
        max_ramp = 0 
        stack = deque()

        for i in range(len(a)):
            if not stack or a[stack[-1]] > a[i]:
                stack.append(i)
        
        for j in range(len(a) - 1, -1, -1):
            while stack and a[j] >= a[stack[-1]]:
                max_ramp = max(max_ramp, j - stack[-1])
                stack.pop()

        return max_ramp
