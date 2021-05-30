class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1, -1)]
        max_area = 0
        for i, num in enumerate(heights):
            while stack[-1][0] != -1 and num <= stack[-1][1]:
                _, height = stack.pop()
                width = i - stack[-1][0] - 1
                max_area = max(max_area, width * height)
            stack.append((i, num))
        while stack[-1][0] != -1:
            _, height = stack.pop()
            last_index = len(heights) 
            width = last_index - stack[-1][0] - 1
            max_area = max(max_area, width * height)
        return max_area
