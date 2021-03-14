class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = float('-inf')
        building_indices = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                building_indices.append(i)
                max_height = heights[i] 
        return building_indices[::-1]
