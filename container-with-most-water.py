class Solution:
    def maxArea(self, height: [int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = float('-inf')

        while l < r:
            min_height = min(height[l], height[r])
            max_area = max(max_area, min_height * (r - l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
